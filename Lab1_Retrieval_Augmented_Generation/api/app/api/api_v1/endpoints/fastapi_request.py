import os
import boto3
from enum import Enum
from pydantic import BaseModel

ACCOUNT_ID = boto3.client("sts").get_caller_identity()["Account"]
REGION = boto3.Session().region_name

class Text2TextModel(str, Enum):
    model_name = "flan-t5-xl"

class EmbeddingsModel(str, Enum):
    model_name = "all-minilm-l6-v2"

class VectorDBType(str, Enum):
    OPENSEARCH = "opensearch"
    FAISS = "faiss"

class Request(BaseModel):
    q: str
    max_length: int = 500
    num_return_sequences: int = 1
    top_k: int = 250
    top_p: float = 0.95
    do_sample: bool = False
    temperature: float = 1
    verbose: bool = False
    max_matching_docs: int = 3  
    text_generation_model: Text2TextModel = Text2TextModel.model_name
    embeddings_generation_model: EmbeddingsModel = EmbeddingsModel.model_name
    vectordb_s3_path: str = f"s3://sagemaker-{REGION}-{ACCOUNT_ID}/{os.environ.get('APP_NAME')}/faiss_index/"
    vectordb_type: VectorDBType = VectorDBType.OPENSEARCH

SAGEMAKER_ENDPOINT_MAPPING = {
    Text2TextModel.model_name: os.environ.get('TEXT2TEXT_ENDPOINT_NAME'),
    EmbeddingsModel.model_name: os.environ.get('EMBEDDING_ENDPOINT_NAME'),
}
