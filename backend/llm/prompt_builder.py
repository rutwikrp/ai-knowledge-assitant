from typing import List


class PromptBuilder:

    SYSTEM_PROMPT = """
You are an Enterprise AI Knowledge Assistant.

Rules:

1. Answer ONLY using the supplied context.

2. If the answer is not present in the context, say:

"I couldn't find this information in the provided documents."

3. Never invent facts.

4. Always mention the document and page number
when referring to information.

5. If multiple documents disagree,
mention both instead of choosing one.

6. Keep answers clear and concise.
"""

    @staticmethod
    def build(question: str, retrieved_chunks: List):

        context = []

        for chunk, score in retrieved_chunks:

            context.append(
                f"""
Document : {chunk.document_name}
Page     : {chunk.page_number}
Score    : {score:.2f}

Content:
{chunk.content}
"""
            )

        context = "\n\n---------------------------\n\n".join(context)

        prompt = f"""
{PromptBuilder.SYSTEM_PROMPT}

================ CONTEXT ================

{context}

=========================================

Question:

{question}

Answer:
"""

        return prompt