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
add_one = sproc( lambda session, x: session.sql(f"SELECT {x} + 1").collect()[0][0], return_type=IntegerType(), input_types=[IntegerType()])
dt = add_one(5)
print(f"Result from stored procedure: {dt}")