# Data Processor

A small, secure-by-default data processing utility (`processor-revised.py`),
the revised implementation addressing the issues found in the review of the
original `processor.py`.

## Modules

- `normalize_to_uppercase(items, skip_invalid=False)` — returns a new list with
  each string item uppercased. Raises `TypeError` on non-iterable input or
  non-string items (unless `skip_invalid=True`, which skips them).
- `get_db_connection_string(env_var="DB_CONNECTION_STRING")` — loads the
  database connection string from the environment. Raises `KeyError` if unset.
  **No credentials are hardcoded in source.**

## Configuration

Set the connection string via environment variable before use:

```bash
# PowerShell
$env:DB_CONNECTION_STRING = "user:pass@host/db"

# bash
export DB_CONNECTION_STRING="user:pass@host/db"
```

In production, source this from a secrets manager (Vault, AWS Secrets Manager,
etc.) rather than a plaintext environment variable.

## Processor Tests

Tests are written with `unittest` and also run under `pytest`.

```bash
python -m pytest test_processor_revised.py -v
python -m unittest test_processor_revised -v
```

## Improvements over the original `processor.py`

| Issue in `processor.py` | Resolution |
|---|---|
| Hardcoded credentials (`admin:password123@db.internal`) | Loaded from environment via `get_db_connection_string` |
| Mutable `global user_db` | Removed; dependencies passed explicitly |
| No error handling | Validates iterables and item types, raises clear errors |
| Poor naming (`run_stuff`, `x`, `y`) | Descriptive names and a comprehension-friendly structure |
| No docstrings / type hints | Full docstrings and type annotations added |
