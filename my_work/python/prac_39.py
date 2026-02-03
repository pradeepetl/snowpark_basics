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
@udf(
    return_type=IntegerType(),
    input_types=[IntegerType()],
    is_permanent=True,
    name="square_udf",
    replace=True,
    stage_location="@int_stage/functions/",
    packages=["snowflake-snowpark-python"]   
)
def square(x):
    return x * x
session.close()