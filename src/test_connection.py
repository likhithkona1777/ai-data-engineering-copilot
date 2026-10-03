from src.snowflake_client import run_query

rows = run_query("""
    SELECT CURRENT_VERSION()   AS version,
           CURRENT_USER()      AS user_name,
           CURRENT_ROLE()      AS role_name,
           CURRENT_WAREHOUSE() AS warehouse,
           CURRENT_DATABASE()  AS database_name,
           CURRENT_SCHEMA()    AS schema_name
""")
print("✅ Connected to Snowflake")
for k, v in rows[0].items():
    print(f"   {k:<14} {v}")