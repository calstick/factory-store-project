"""Data processing utilities.

This module provides string normalization helpers and a small example of how
database configuration should be sourced from the environment rather than
hardcoded in source control.
"""

from __future__ import annotations

import os
from typing import Iterable, List, Optional


def get_db_connection_string(env_var: str = "DB_CONNECTION_STRING") -> str:
    """Return the database connection string from the environment.

    Credentials must never be hardcoded in source. They are loaded from an
    environment variable (or a secrets manager in production).

    Args:
        env_var: Name of the environment variable holding the connection string.

    Returns:
        The connection string.

    Raises:
        KeyError: If the environment variable is not set.
    """
    try:
        return os.environ[env_var]
    except KeyError as exc:
        raise KeyError(
            f"Required environment variable '{env_var}' is not set."
        ) from exc


def normalize_to_uppercase(
    items: Iterable[str], skip_invalid: bool = False
) -> List[str]:
    """Return a new list with each string item uppercased.

    Args:
        items: An iterable of strings to normalize.
        skip_invalid: If True, non-string items are skipped instead of raising.

    Returns:
        A new list containing the uppercased strings.

    Raises:
        TypeError: If ``items`` is not iterable, or if an item is not a string
            and ``skip_invalid`` is False.
    """
    try:
        iterator = iter(items)
    except TypeError as exc:
        raise TypeError(
            f"Expected an iterable, got {type(items).__name__}"
        ) from exc

    result: List[str] = []
    for item in iterator:
        if not isinstance(item, str):
            if skip_invalid:
                continue
            raise TypeError(f"Expected str, got {type(item).__name__}")
        result.append(item.upper())
    return result
