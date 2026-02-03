from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json

with open("config.json") as json_file:
    conn_params = json.load(json_file)
session = Session.builder.configs(conn_params).create()
emp_df = session.table("emp")
emp_df.na.drop(subset=["COMM","MGR"]).show()
emp_df.na.fill({"COMM":5000}).show()