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
add_two = sproc(lambda session, x: int(session.sql(f"select {x} + 2").collect()[0][0]),
                return_type=IntegerType(),
                input_types=[IntegerType()],
                name="add_two",
                replace=True,
                packages=["snowflake-snowpark-python"],
                stage_location="@int_stage/sprocs/procdure/"
                )
dt = session.call("add_two", 10)
print(f"Result from stored procedure: {dt}")