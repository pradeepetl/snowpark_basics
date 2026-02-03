from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json

with open("config.json") as f:
    connection_config = json.load(f)
session = Session.builder.configs(connection_config).create()
session.use_role("ACCOUNTADMIN")
session.use_warehouse("MY_WAREHOUSE")
session.use_database("MY_DB")
session.use_schema("MY_SCHEMA")
file_name = "@aws_s3_stage/json/employee_object.json"
session.read.option("format_name", "JSON_FILE_FORMAT").\
    json(file_name).select_expr(("$1:employee_id"),"$1:employee_name","$1:position").show()