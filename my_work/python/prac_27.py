from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
from snowflake.snowpark.window import Window
import json

with open('config.json') as f:
    connection_parameters = json.load(f)
session = Session.builder.configs(connection_parameters).create()
session.use_role("ACCOUNTADMIN")
session.use_warehouse("MY_WAREHOUSE")
session.use_database("MY_DB")
session.use_schema("MY_SCHEMA")
df = session.table("EMP")
win_spec = df.select(col("DEPTNO"),col("ENAME"), col("SAL"),rank().over(Window.partition_by(col("DEPTNO")).order_by(col("SAL").desc())).alias("RANK"))
win_spec.where(col("RANK") == 2).show()