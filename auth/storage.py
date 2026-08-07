from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any


class UserStore:
    """File-backed user store that keeps runtime credentials out of the repository."""

    def __init__(self, directory: Path | str):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)

    def exists(self, user_id: str) -> bool:
        return self._path_for(user_id).exists()

    def load(self, user_id: str) -> dict[str, Any] | None:
        path = self._path_for(user_id)
        if not path.exists():
            return None
        try:
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (OSError, json.JSONDecodeError):
            return None
        if data.get("user_id") != user_id:
            return None
        return data

    def save(self, user_id: str, record: dict[str, Any]) -> None:
        path = self._path_for(user_id)
        temp_path = path.with_suffix(".tmp")
        with temp_path.open("w", encoding="utf-8") as handle:
            json.dump(record, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temp_path, path)

    @staticmethod
    def _filename_for(user_id: str) -> str:
        digest = hashlib.sha256(user_id.encode("utf-8")).hexdigest()
        return f"{digest}.json"

    def _path_for(self, user_id: str) -> Path:
        return self.directory / self._filename_for(user_id)
