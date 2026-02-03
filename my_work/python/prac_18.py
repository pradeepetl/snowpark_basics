from snowflake.snowpark import Session
from snowflake.snowpark.functions import col, lit
from snowflake.snowpark.types import StructType, StructField, StringType, IntegerType
import json

with open("config.json") as f:
    connection_config = json.load(f)
session = Session.builder.configs(connection_config).create()
session.use_role("ACCOUNTADMIN")
session.use_warehouse("MY_WAREHOUSE")
session.use_database("MY_DB")
session.use_schema("MY_SCHEMA")
files = session.table("information_schema.stages").collect()
for indx,file in enumerate(files):
    stage_name = '@' + file['STAGE_NAME']
    stage_files = session._list_files_in_stage(stage_name)
    for f in stage_files:
        print(stage_name,f)