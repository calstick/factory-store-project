"""Unit tests for processor-revised.py.

The module under test has a hyphen in its filename, so it is loaded
dynamically via importlib.
"""

import importlib.util
import os
import unittest
from pathlib import Path

_MODULE_PATH = Path(__file__).parent / "processor-revised.py"
_spec = importlib.util.spec_from_file_location("processor_revised", _MODULE_PATH)
processor = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(processor)


class NormalizeToUppercaseTests(unittest.TestCase):
    def test_basic_list(self):
        self.assertEqual(
            processor.normalize_to_uppercase(["apple", "banana"]),
            ["APPLE", "BANANA"],
        )

    def test_empty_iterable(self):
        self.assertEqual(processor.normalize_to_uppercase([]), [])

    def test_accepts_generator(self):
        gen = (s for s in ["x", "y"])
        self.assertEqual(processor.normalize_to_uppercase(gen), ["X", "Y"])

    def test_returns_new_list(self):
        original = ["a"]
        result = processor.normalize_to_uppercase(original)
        self.assertIsNot(result, original)
        self.assertEqual(original, ["a"])

    def test_non_string_item_raises(self):
        with self.assertRaises(TypeError):
            processor.normalize_to_uppercase(["ok", 123])

    def test_skip_invalid_skips_non_strings(self):
        self.assertEqual(
            processor.normalize_to_uppercase(["ok", 123, None, "yes"], skip_invalid=True),
            ["OK", "YES"],
        )

    def test_non_iterable_raises(self):
        with self.assertRaises(TypeError):
            processor.normalize_to_uppercase(42)


class GetDbConnectionStringTests(unittest.TestCase):
    def test_reads_from_environment(self):
        os.environ["TEST_DB_CONN"] = "user:pass@host/db"
        try:
            self.assertEqual(
                processor.get_db_connection_string("TEST_DB_CONN"),
                "user:pass@host/db",
            )
        finally:
            del os.environ["TEST_DB_CONN"]

    def test_missing_env_var_raises(self):
        os.environ.pop("DEFINITELY_NOT_SET_VAR", None)
        with self.assertRaises(KeyError):
            processor.get_db_connection_string("DEFINITELY_NOT_SET_VAR")

    def test_no_hardcoded_credentials_in_source(self):
        source = _MODULE_PATH.read_text(encoding="utf-8")
        self.assertNotIn("password123", source)
        self.assertNotIn("admin:password123@db.internal", source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
