## AWS-ANALYTICS-GENAI-LLM-WORKSHOP

### OVERVIEW

This github repository supports AWS 'GenAI Data Foundation Workshop'.

Foundation models are usually trained offline, making the model agnostic to any data that is created after the model was trained. Additionally, foundation models are trained on very general domain corpora, making them less effective for domain-specific tasks. You can use Retrieval Augmented Generation (RAG) to retrieve data from outside a foundation model and augment your prompts by adding the relevant retrieved data in context.

With RAG, the external data used to augment your prompts can come from multiple data sources, such as a document repositories, databases, or APIs. The first step is to convert your documents and any user queries into a compatible format to perform relevancy search. To make the formats compatible, a document collection, or knowledge library, and user-submitted queries are converted to numerical representations using embedding language models. Embedding is the process by which text is given numerical representation in a vector space. RAG model architectures compare the embeddings of user queries within the vector of the knowledge library. The original user prompt is then appended with relevant context from similar documents within the knowledge library. This augmented prompt is then sent to the foundation model. You can update knowledge libraries and their relevant embeddings asynchronously.

Amazon SageMaker Studio provides data scientists, machine learning (ML) engineers, and general practitioners with tools to perform data analytics and data preparation at scale. Analyzing, transforming, and preparing large amounts of data is a foundational step of any data science and ML workflow.

AWS Glue is a serverless, scalable data integration and ETL (extract, transform, and load) service that makes it easier to discover, prepare, move, and integrate data from multiple sources.

AWS Glue uses the AWS Glue Data Catalog to store metadata about data sources, transforms, and targets. The Data Catalog is a drop-in replacement for the Apache Hive Metastore. The AWS Glue Jobs system provides a managed infrastructure for defining, scheduling, and running ETL operations on your data.

Using the metadata in the Data Catalog, AWS Glue can automatically generate Scala or PySpark (the Python API for Apache Spark) scripts with AWS Glue extensions that you can use and modify to perform various ETL operations. For example, you can extract, clean, and transform raw data, and then store the result in a different repository, where it can be queried and analyzed. Such a script might convert a CSV file into a relational form and save it in Amazon Redshift.

AWS Glue Data Quality helps reduce the need for manual data quality work by automatically analyzing your data to gather data statistics. It uses open-source Deequ to evaluate rules and measure and monitor the data quality of petabyte-scale data lakes. It then recommends data quality rules to get started. You can update recommended rules or add new rules. If data quality deteriorates, you can configure actions to alert users and drill down into the issue’s root cause. Data quality rules and actions can also be configured on AWS Glue data pipelines, helping prevent “bad” data from entering data lakes and data warehouses.

### Anatomy of this Repository

#### [Lab1_Retrieval_Augmented_Generation](./Lab1_Retrieval_Augmented_Generation/)

Guides users how to build a RAG based Solution leveraging Amazon SageMaker, Glue and OpenSearch.

#### Other labs coming soon....

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

