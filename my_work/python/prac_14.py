from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json

with open("config.json") as json_file:
    conn_params = json.load(json_file)
session = Session.builder.configs(conn_params).create()
#session.sql("show integrations").show()
#session.sql("show stages").show()
files = session.sql("list @aws_s3_stage").collect()
for file in files:
    print(file["name"])
#session.sql("select * from directory(@aws_s3_stage)").show()