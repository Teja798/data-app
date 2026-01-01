from sqlalchemy import create_engine


DATABRICKS_SERVER_HOSTNAME = "adb-123456.12.azuredatabricks.net"
DATABRICKS_HTTP_PATH = "/sql/1.0/warehouses/abcd1234"
DATABRICKS_TOKEN = "dapiXXXXXXXXXXXXXXXX"

engine = create_engine(
    url=f"databricks://token:{DATABRICKS_TOKEN}@{DATABRICKS_SERVER_HOSTNAME}?"
        f"http_path={DATABRICKS_HTTP_PATH}"
)