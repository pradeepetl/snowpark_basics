from numpy import select
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
file_name = "/home/asvreddy/Downloads/car-sales.json"
stage_file = session.file.put(file_name,'@int_stage/files/json', auto_compress=False, overwrite=True)
print(stage_file)
df = session.read.options({"type":'json','strip_outer_array':True}).json('@int_stage/files/json/car-sales.json')
df = df.select(col("$1").alias("CAR_SALES_DATA"))
df.select(col("CAR_SALES_DATA")["customer"],col("CAR_SALES_DATA")["date"], \
          col("CAR_SALES_DATA")["dealership"],col("CAR_SALES_DATA")["salesperson"], \
            col("CAR_SALES_DATA")["vehicle"]).show()
df.join_table_function("flatten", col("CAR_SALES_DATA")["customer"]) \
    .select(col("value")["address"].as_("address"), \
            col("value")["name"].as_("name"), \
            col("value")["phone"].as_("phone"), \
            col("CAR_SALES_DATA")["date"].as_("date"),
            col("CAR_SALES_DATA")["dealership"].as_("dealership"),
            col("CAR_SALES_DATA")["salesperson"].as_("salesperson"),
            col("CAR_SALES_DATA")["vehicle"].as_("vehicle")).show()
session.close()
