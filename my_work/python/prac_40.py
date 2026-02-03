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
    return_type=StringType(),
    input_types=[StringType()],
    is_permanent=True,
    name="greet_sproc",
    replace=True,
    stage_location="@int_stage/procedures/",
    packages=["snowflake-snowpark-python"]   
)
def greet_sproc(session: Session, name: str) -> str:
    return f"Hello, {name}!"
data = session.call("greet_sproc", "SIVA")
print(data)
session.close()