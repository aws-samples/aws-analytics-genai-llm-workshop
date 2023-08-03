import sys
from awsglue.transforms import *
from awsglue.context import GlueContext
from awsglue.job import Job
import boto3
from pyspark import SparkContext, SparkConf
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import when
#from pyspark.sql.functions import *
from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import col, concat, lit, length, concat_ws

'''

Glue PySpark job that prepares the med Q & A dataset for downstream consumption
The job used the records that passes DQ checks

Required Input Parameters 
--INPUT_RECORDS_PATH
--OUTPUT_RECORDS_PATH

'''


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME',"INPUT_RECORDS_PATH","OUTPUT_RECORDS_PATH"])

input_records_path = args["INPUT_RECORDS_PATH"]
output_records_path=args["OUTPUT_RECORDS_PATH"]

conf = SparkConf()
sc = SparkContext.getOrCreate(conf=conf)
spark = SparkSession(sc)

df = spark.read \
    .format("xml") \
    .option("rowTag", "record") \
    .load(input_records_path)

df = df.select(concat(col("Question._VALUE"),lit("\n"),col("Answer")))

df.write.option("lineSep", "\n\z\n").text(output_records_path)

