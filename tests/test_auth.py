import json
import tempfile
import unittest
from pathlib import Path

from auth import AuthService, UserAlreadyExists, UserStore, ValidationError


class AuthServiceTest(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.user_dir = Path(self.temp_dir.name) / "users"
        self.store = UserStore(self.user_dir)
        self.auth = AuthService(self.store)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_register_and_authenticate(self):
        self.auth.register("andy", "correct-horse", "correct-horse")

        self.assertTrue(self.auth.authenticate("andy", "correct-horse"))
        self.assertFalse(self.auth.authenticate("andy", "wrong-password"))
        self.assertFalse(self.auth.authenticate("missing", "correct-horse"))

    def test_password_is_not_stored_as_plaintext(self):
        password = "correct-horse"
        self.auth.register("andy", password, password)

        files = list(self.user_dir.glob("*.json"))
        self.assertEqual(len(files), 1)
        raw = files[0].read_text(encoding="utf-8")
        self.assertNotIn(password, raw)

        record = json.loads(raw)
        self.assertEqual(record["algorithm"], "pbkdf2_sha256")
        self.assertNotIn("user_password", record)

    def test_duplicate_user_is_rejected(self):
        self.auth.register("andy", "correct-horse", "correct-horse")

        with self.assertRaises(UserAlreadyExists):
            self.auth.register("andy", "another-pass", "another-pass")

    def test_password_confirmation_and_minimum_length_are_validated(self):
        with self.assertRaises(ValidationError):
            self.auth.register("andy", "password-one", "password-two")

        with self.assertRaises(ValidationError):
            self.auth.register("andy", "short", "short")

    def test_change_password_invalidates_old_password(self):
        self.auth.register("andy", "old-password", "old-password")
        self.auth.change_password("andy", "new-password", "new-password")

        self.assertFalse(self.auth.authenticate("andy", "old-password"))
        self.assertTrue(self.auth.authenticate("andy", "new-password"))

    def test_user_id_cannot_escape_storage_directory(self):
        user_id = "../../outside"
        self.auth.register(user_id, "correct-horse", "correct-horse")

        files = list(self.user_dir.glob("*.json"))
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0].parent, self.user_dir)
        self.assertTrue(self.auth.authenticate(user_id, "correct-horse"))


if __name__ == "__main__":
    unittest.main()
