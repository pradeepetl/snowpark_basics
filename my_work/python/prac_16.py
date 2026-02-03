from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json

with open("config.json") as f:
    connection_config = json.load(f)
session = Session.builder.configs(connection_config).create()
#print(session.sql("SELECT CURRENT_VERSION()").collect())
data = session.create_dataframe([1,2,3,4,5],schema=["numbers"])
data.show()