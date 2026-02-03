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
data = session.read.option("format_name", "csv_parse_header").\
        csv("@int_stage/files/csv/swiggy_data.csv.gz")
data.select(col('"State"'), col('"City"')).show()