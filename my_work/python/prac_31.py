from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json

with open('config.json') as f:
    connection_parameters = json.load(f)
session = Session.builder.configs(connection_parameters).create()
session.use_role("ACCOUNTADMIN")
session.use_warehouse("MY_WAREHOUSE")
session.use_database("MY_DB")
session.use_schema("MY_SCHEMA")
df = session.table("employees")
df_pivot = df.pivot(col("DEPARTMENT"),["PRESIDENCE", "IT", "FINANCE"]).sum(col("SALARY"))
df_pivot.show()
last_id = df_pivot.select(last_query_id()).collect()[0][0]
print(f"Last Query ID: {last_id}")
session.close()