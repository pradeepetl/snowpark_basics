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
df_group = df.group_by(col("DEPTNO")).agg(sum(col("SAL")).alias("TOTAL_SAL"),\
                                          max(col("SAL")).alias("MAX_SAL"), \
                                          min(col("SAL")).alias("MIN_SAL"))
df_group.filter(col("TOTAL_SAL") > 9500).show()