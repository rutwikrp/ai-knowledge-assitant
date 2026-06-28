from retrieval.pipeline import retrieve
from llm.prompt_builder import PromptBuilder
from llm.provider_factory import get_provider


class ResponseGenerator:

    def __init__(self):
        self.provider = get_provider()

    def generate(self, query):

        retrieved_chunks = retrieve(query)

        prompt = PromptBuilder.build(
            query,
            retrieved_chunks
        )

        answer = self.provider.generate(prompt)

        return {
            "question": query,
            "answer": answer,
            "sources": retrieved_chunks
        }