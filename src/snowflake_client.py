"""Single place that opens Snowflake connections and runs SQL."""
import snowflake.connector
from src.config import get_snowflake_settings


def get_connection():
    return snowflake.connector.connect(**get_snowflake_settings())


def run_query(sql: str) -> list[dict]:
    conn = get_connection()
    try:
        cur = conn.cursor(snowflake.connector.DictCursor)
        cur.execute(sql)
        return cur.fetchall()
    finally:
        conn.close()