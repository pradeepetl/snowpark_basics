from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json

file_name = "/home/asvreddy/Desktop/work/files/json/sample_data.json"
stage_name = "int_stage"
with open('config.json') as f:
    connection_parameters = json.load(f)
session = Session.builder.configs(connection_parameters).create()
session.use_role("ACCOUNTADMIN")
session.use_warehouse("MY_WAREHOUSE")
session.use_database("MY_DB")
session.use_schema("MY_SCHEMA")
stage_fname = '@'+stage_name+'/files/json'
session.file.put(file_name, stage_fname, overwrite=True,auto_compress=False)
df = session.read.json(stage_fname)
df = df.select_expr(col("$1"[0]).alias("data"))
df.show()