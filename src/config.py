"""Loads Snowflake settings from environment variables. No secrets in code."""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

REQUIRED = [
    "SNOWFLAKE_ACCOUNT", "SNOWFLAKE_USER", "SNOWFLAKE_ROLE",
    "SNOWFLAKE_WAREHOUSE", "SNOWFLAKE_DATABASE", "SNOWFLAKE_SCHEMA",
    "SNOWFLAKE_PRIVATE_KEY_PATH",
]


def get_snowflake_settings() -> dict:
    missing = [k for k in REQUIRED if not os.getenv(k)]
    if missing:
        raise ValueError(f"Missing environment variables: {', '.join(missing)}")
    return {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "role": os.getenv("SNOWFLAKE_ROLE"),
        "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
        "database": os.getenv("SNOWFLAKE_DATABASE"),
        "schema": os.getenv("SNOWFLAKE_SCHEMA"),
        "private_key_file": os.getenv("SNOWFLAKE_PRIVATE_KEY_PATH"),
        "private_key_file_pwd": os.getenv("SNOWFLAKE_PRIVATE_KEY_PASSPHRASE") or None,
    }


if __name__ == "__main__":
    s = get_snowflake_settings()
    print("Config OK:", {k: v for k, v in s.items() if "key" not in k})