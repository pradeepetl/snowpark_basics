from snowflake.snowpark import Session
from snowflake.snowpark.functions import *
from snowflake.snowpark.types import *
import json

with open("config.json") as json_file:
    conn_params = json.load(json_file)
session = Session.builder.configs(conn_params).create()
file_location = "@aws_s3_stage/csv/Customers.csv"
schema = StructType([
    StructField("ID", IntegerType()),
    StructField("Name", StringType()),
    StructField("Age", IntegerType()),
    StructField("Income", FloatType()),
    StructField("SpendingScore", IntegerType()),
    StructField("Profession", StringType()),
    StructField("workExperience", IntegerType()),
    StructField("FamilySize", IntegerType())
])
options = {
    "skip_header": 1
}
#df = session.read.options(options).schema(schema).csv(file_location)
df = session.read.option("format_name","CSV_SKIP_HEADER").csv(file_location)
df.show()
df.print_schema()
#df.write.mode("overwrite").save_as_table("Customers")
#print("Data written to table Customers successfully.")
session.close()