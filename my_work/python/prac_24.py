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
df_agg = df.agg(avg(col("SAL")).alias("AVG_SAL"), max(col("SAL")).alias("MAX_SAL"),min(col("SAL")).alias("MIN_SAL"))
df_agg = df.agg({"SAL":"avg","SAL":"max","SAL":"min"})
df_agg.show()