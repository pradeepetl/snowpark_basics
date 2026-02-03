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
stage_name = 'aws_s3_stage/json'
stage_files = list(session._list_files_in_stage('@' + stage_name))
for file in stage_files:
    file_name = '@' + file.replace("a/files/json",stage_name)
    print(file_name)
    session.read.option("format_name", "JSON_FILE_FORMAT").\
        json(file_name).show()