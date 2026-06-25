from llm.response_generator import ResponseGenerator

generator = ResponseGenerator()

print("\nEnterprise AI Knowledge Assistant")
print("-" * 50)

while True:

    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    result = generator.generate(query)

    print("\nAnswer\n")

    print(result["answer"])

    print("\nSources")

    for chunk, score in result["sources"]:

        print(
            f"- {chunk.document_name}"
            f" (Page {chunk.page_number})"
        )