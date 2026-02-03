from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json

with open('config.json') as f:
    connection_parameters = json.load(f)
session = Session.builder.configs(connection_parameters).create()
session.use_role("ACCOUNTADMIN")
session.use_warehouse("MY_WAREHOUSE")
session.use_database("MY_DB")
session.use_schema("MY_SCHEMA")
df = session.table("EMP")
AVG_SAL = df.select(avg(col("SAL")).alias("AVG_SAL")).collect()[0]["AVG_SAL"]
#print("Average Salary is: ", AVG_SAL)
df_group = df.group_by(col("DEPTNO")).agg((avg(col("SAL"))).alias("AVG_SAL"))
df_filtered = df_group.filter(col("AVG_SAL") > AVG_SAL)
df_filtered.show()