from __future__ import annotations

import base64
import hashlib
import hmac
import secrets
from typing import Any

from .storage import UserStore

PBKDF2_ITERATIONS = 310_000
SALT_BYTES = 16
MIN_PASSWORD_LENGTH = 8


class AuthError(Exception):
    pass


class ValidationError(AuthError):
    pass


class UserAlreadyExists(AuthError):
    pass


class InvalidCredentials(AuthError):
    pass


class AuthService:
    def __init__(self, store: UserStore):
        self.store = store

    def register(self, user_id: str, password: str, password_confirm: str) -> None:
        user_id = self._validate_user_id(user_id)
        self._validate_password_pair(password, password_confirm)
        if self.store.exists(user_id):
            raise UserAlreadyExists("已經有此帳號")
        self.store.save(user_id, self._new_record(user_id, password))

    def authenticate(self, user_id: str, password: str) -> bool:
        user_id = user_id.strip()
        if not user_id or not password:
            return False
        record = self.store.load(user_id)
        if not record:
            return False
        try:
            expected = base64.b64decode(record["password_hash"])
            salt = base64.b64decode(record["salt"])
            iterations = int(record["iterations"])
        except (KeyError, TypeError, ValueError):
            return False
        actual = self._derive(password, salt, iterations)
        return hmac.compare_digest(actual, expected)

    def change_password(self, user_id: str, password: str, password_confirm: str) -> None:
        user_id = self._validate_user_id(user_id)
        self._validate_password_pair(password, password_confirm)
        if not self.store.exists(user_id):
            raise InvalidCredentials("找不到帳號")
        self.store.save(user_id, self._new_record(user_id, password))

    @staticmethod
    def _validate_user_id(user_id: str) -> str:
        normalized = user_id.strip()
        if not normalized:
            raise ValidationError("帳號要輸入")
        if len(normalized) > 64:
            raise ValidationError("帳號長度不可超過 64 個字元")
        return normalized

    @staticmethod
    def _validate_password_pair(password: str, password_confirm: str) -> None:
        if password != password_confirm:
            raise ValidationError("密碼與確認密碼不同")
        if len(password) < MIN_PASSWORD_LENGTH:
            raise ValidationError(f"密碼至少需要 {MIN_PASSWORD_LENGTH} 個字元")

    @staticmethod
    def _derive(password: str, salt: bytes, iterations: int) -> bytes:
        return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)

    def _new_record(self, user_id: str, password: str) -> dict[str, Any]:
        salt = secrets.token_bytes(SALT_BYTES)
        password_hash = self._derive(password, salt, PBKDF2_ITERATIONS)
        return {
            "version": 1,
            "user_id": user_id,
            "algorithm": "pbkdf2_sha256",
            "iterations": PBKDF2_ITERATIONS,
            "salt": base64.b64encode(salt).decode("ascii"),
            "password_hash": base64.b64encode(password_hash).decode("ascii"),
        }
