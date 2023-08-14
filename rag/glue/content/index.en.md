---
title: "Data Goverance"
weight: 0
---

In this workshop, we will use AWS Glue Data Quality and AWS Lake Formation to ensure data quality and govern the access to data in our data lake. 

We will then query the data and verify our data quality and security with Amazon Athena.

The following are the high-level steps that you will cover in this lab:

1.Create data quality rules – Build a set of data quality rules using the DQDL builder by choosing built-in rulesets that you configure.

2.Configure a data quality job – Define actions based on the data quality results and output options.

3.Save and run a job with data quality – Create and run a job. Saving the job will save the rule sets you created for the job.

4.Monitor and review the data quality results – Review the data quality results after the job run is complete. Optionally, schedule the job for a future date.

AWS Glue Data Quality

AWS Glue Data Quality evaluates and monitors the quality of your data based on rules that you define. This makes it easy to identify the data that needs action. 

In AWS Glue Studio, you can add data quality nodes to your visual job to create data quality rules on tables in your Data Catalog. Then you can monitor and evaluate changes to your data sets as they evolve over time.

AWS Lake Formation

Moving your data into a data lake can provide better flexibility, cost savings, and scalability. However, manually setting up and managing data lakes can be a complex and time-consuming process. 

AWS Lake Formation makes it easier to centrally govern, secure, and globally share data for analytics and machine learning. With Lake Formation, you can centralize data security and governance using the AWS Glue Data Catalog, letting you manage metadata and data permissions in one place with familiar database-style features. It also enables fine-grained data access control, so you can ensure users have access to the right data down to the row and column level.

Amazon Athena

Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run. Athena is easy to use. Simply point to your data in Amazon S3, define the schema, and start querying using standard SQL and Spark. Most results are delivered within seconds. 

With Athena, there’s no need for complex ETL jobs to prepare your data for analysis. This makes it easy for anyone with SQL and Spark skills to quickly analyze large-scale datasets. 

Athena is out-of-the-box integrated with AWS Glue Data Catalog, allowing you to create a unified metadata repository across various services, crawl data sources to discover schemas and populate your Catalog with new and modified table and partition definitions, and maintain schema versioning.

</br>


---

**Expected Duration**: 1 Hours

**Cost**:  This workshop is performed in a Worshop Studio account provided by AWS at no costs.

**Account**: This workshop is performed in a Worshop Studio account provided by AWS .

**Audience**: This workshop is intended for IT managers, employees, or anyone else interested in learning more about the listed AWS services.

---















