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
@sproc(
    name="add_three",
    replace=True,
    is_permanent=True,
    stage_location="@int_stage/sprocs/procedure/",
    input_types=[IntegerType()],
    return_type=IntegerType(),
    packages=["snowflake-snowpark-python"],
)
def add_three(session: Session, x: int) -> int:
    return int(session.sql(f"select {x} + 3").collect()[0][0])

dt = session.call("add_three", 10)
print(f"Result from stored procedure: {dt}")