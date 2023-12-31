from langchain.embeddings import HuggingFaceInstructEmbeddings
from app.components.embeddings.abstract.embeddings import Embeddings


class HuggingfaceInstructEmbeddingsStrategy(Embeddings):
    def __init__(self, model_name: str):
        self.embedding = HuggingFaceInstructEmbeddings(model_name=model_name)

    def get_embedding(self):
        return self.embedding
