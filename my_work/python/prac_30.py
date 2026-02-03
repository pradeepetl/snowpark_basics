from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json

file_name = '/home/asvreddy/Downloads/employees.csv'
with open('config.json') as f:
    connection_parameters = json.load(f)
session = Session.builder.configs(connection_parameters).create()
session.use_role("ACCOUNTADMIN")
session.use_warehouse("MY_WAREHOUSE")
session.use_database("MY_DB")
session.use_schema("MY_SCHEMA")
session.file.put(file_name,'@int_stage/files/csv/',auto_compress=False,overwrite=True)
df = session.read.option("header", True).csv('@int_stage/files/csv/employees.csv')
df.write.mode("overwrite").save_as_table("employees")
print("Data loaded into employees table")
session.close()