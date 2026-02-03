from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
import json

with open("config.json") as json_data:
    config = json.load(json_data)
session = Session.builder.configs(config).create()
session.sql("select current_timestamp()").show()
df = session.table("emp")
df.show()
session.close()