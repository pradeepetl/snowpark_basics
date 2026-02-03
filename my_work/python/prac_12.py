from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json

with open("config.json") as json_file:
    conn_params = json.load(json_file)
session = Session.builder.configs(conn_params).create()
data = [(1,'siva',34,['SQL','ORACLE']),(2,'reddy',33,['SNOWFLAKE','PYTHON']),(3,'meera',33,['ANDROID'])]
df = session.create_dataframe(data, schema=['ID', 'NAME', 'AGE', 'SKILLS'])
df.show()