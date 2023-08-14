# Lab 1 Retrieval Augmented Generation (RAG)

Retrieval Augmented Generation (RAG) is a technique for generating text that combines a large language model (LLM) with an information retrieval (IR) system. The LLM is used to generate text, and the IR system is used to retrieve relevant documents from a knowledge base. 

RAG works by first taking an input prompt and using the LLM to generate a set of candidate sentences. The IR system is then used to retrieve relevant documents from the knowledge base that are consistent with the candidate sentences. The LLM is then used to refine the candidate sentences based on the retrieved documents. This process is repeated until the LLM generates a text that is both factual and informative.

Below are some benefits of using RAG:

* Factual consistency: RAG can access and process information from a knowledge base, which helps to ensure that the generated text is factual and consistent with reality.
* Reliability: RAG can retrieve relevant documents from a knowledge base, which helps to improve the reliability of the generated text.
* Mitigation of hallucination: RAG can help to mitigate the problem of "hallucination" in language models, where the model generates text that is not based on any real knowledge.
* Fine-tuning and updating: RAG models can be fine-tuned and updated with new knowledge, which makes them more adaptable to new tasks and domains

# TODO: Repo Module Overview

## [API](./api/)

## [GLUE](./glue/)

## [STREAMLIT](./streamlit-app/)

