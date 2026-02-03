from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json
import pandas as pd

file_name = "/home/asvreddy/Desktop/work/oracle/files/EMP.csv"
with open("config.json") as f:
    connection_config = json.load(f)
session = Session.builder.configs(connection_config).create()
pd_df = pd.read_csv(file_name)
sn_df = session.create_dataframe(pd_df)
sn_df.show()
print(sn_df.describe().show())