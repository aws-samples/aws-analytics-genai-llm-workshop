import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrameCollection
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame
import concurrent.futures
import re

'''
Glue pyspark code that performs DQ check on the input Q&A data set. 
Requires following input parameters 
--DB_NAME
--TBL_NAME
--RULES 
--DQMETRICS_OUTPUT_PATH 
--DQFAIL_RECORDS_PATH 
--DQ_PASS_RECORDS_PATH 

'''

class GroupFilter:
    def __init__(self, name, filters):
        self.name = name
        self.filters = filters


def apply_group_filter(source_DyF, group):
    return Filter.apply(frame=source_DyF, f=group.filters)


def threadedRoute(glue_ctx, source_DyF, group_filters) -> DynamicFrameCollection:
    dynamic_frames = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_filter = {
            executor.submit(apply_group_filter, source_DyF, gf): gf
            for gf in group_filters
        }
        for future in concurrent.futures.as_completed(future_to_filter):
            gf = future_to_filter[future]
            if future.exception() is not None:
                print("%r generated an exception: %s" % (gf, future.exception()))
            else:
                dynamic_frames[gf.name] = future.result()
    return DynamicFrameCollection(dynamic_frames, glue_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME","DB_NAME","TBL_NAME","RULES","DQMETRICS_OUTPUT_PATH","DQFAIL_RECORDS_PATH","DQ_PASS_RECORDS_PATH"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

database_name = args["DB_NAME"]
table_name = args["TBL_NAME"]
dqdl_string = args["RULES"]
metrics_path = args["DQMETRICS_OUTPUT_PATH"]
dqfail_records_path = args["DQFAIL_RECORDS_PATH"]
dqpass_records_path = args["DQ_PASS_RECORDS_PATH"]


AWSGlueDataCatalog_node1690809364113 = glueContext.create_dynamic_frame.from_catalog(
    database=database_name,
    table_name=table_name,
    transformation_ctx="AWSGlueDataCatalog_node1690809364113",
)


EvaluateDataQuality_node1690808503935_ruleset = """
    Rules = [ 
     {}
     ]
""".format(dqdl_string)

EvaluateDataQuality_node1690808503935 = EvaluateDataQuality().process_rows(
    frame=AWSGlueDataCatalog_node1690809364113,
    ruleset=EvaluateDataQuality_node1690808503935_ruleset,
    publishing_options={
        "dataQualityEvaluationContext": "EvaluateDataQuality_node1690808503935",
        "enableDataQualityCloudWatchMetrics": True,
        "enableDataQualityResultsPublishing": False,
    },
    additional_options={"performanceTuning.caching": "CACHE_NOTHING"},
)

# Script generated for node rowLevelOutcomes
rowLevelOutcomes_node1690808530416 = SelectFromCollection.apply(
    dfc=EvaluateDataQuality_node1690808503935,
    key="rowLevelOutcomes",
    transformation_ctx="rowLevelOutcomes_node1690808530416",
)

# Script generated for node ruleOutcomes
ruleOutcomes_node1690808531874 = SelectFromCollection.apply(
    dfc=EvaluateDataQuality_node1690808503935,
    key="ruleOutcomes",
    transformation_ctx="ruleOutcomes_node1690808531874",
)

# Script generated for node Conditional Router
ConditionalRouter_node1690808673192 = threadedRoute(
    glueContext,
    source_DyF=rowLevelOutcomes_node1690808530416,
    group_filters=[
        GroupFilter(
            name="Failed_Records",
            filters=lambda row: (
                bool(re.match("Failed", row["DataQualityEvaluationResult"]))
            ),
        ),
        GroupFilter(
            name="default_group",
            filters=lambda row: (
                not (bool(re.match("Failed", row["DataQualityEvaluationResult"])))
            ),
        ),
    ],
)

# Script generated for node Failed_Records
Failed_Records_node1690808673238 = SelectFromCollection.apply(
    dfc=ConditionalRouter_node1690808673192,
    key="Failed_Records",
    transformation_ctx="Failed_Records_node1690808673238",
)

# Script generated for node default_group
default_group_node1690808673237 = SelectFromCollection.apply(
    dfc=ConditionalRouter_node1690808673192,
    key="default_group",
    transformation_ctx="default_group_node1690808673237",
)

# Script generated for node Amazon S3
AmazonS3_node1690808619787 = glueContext.write_dynamic_frame.from_options(
    frame=ruleOutcomes_node1690808531874,
    connection_type="s3",
    format="json",
    connection_options={
        "path": metrics_path,
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1690808619787",
)

# Script generated for node Amazon S3
AmazonS3_node1690808735784 = glueContext.write_dynamic_frame.from_options(
    frame=Failed_Records_node1690808673238,
    connection_type="s3",
    format="json",
    connection_options={
        "path": dqfail_records_path,
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1690808735784",
)


pass_df_subset = default_group_node1690808673237.toDF().select("Answer","Question","_pid")
qa_xml_dyf = DynamicFrame.fromDF(pass_df_subset, glueContext, "pass_df_subset")



# Script generated for node Amazon S3
AmazonS3_node1690808701942 = glueContext.write_dynamic_frame.from_options(
    frame=qa_xml_dyf,
    connection_type="s3",
    format="xml",
    connection_options={
        "path": dqpass_records_path,
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1690808701942",
)

job.commit()
