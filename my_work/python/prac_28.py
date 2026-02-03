from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json

with open('config.json') as f:
    connection_parameters = json.load(f)

session = Session.builder.configs(connection_parameters).create()
print(session._session_id)
print(session.get_current_role())
print(session.sql("select current_user()").collect()[0][0])