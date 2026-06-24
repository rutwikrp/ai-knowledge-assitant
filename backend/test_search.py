from retrieval.vector_search import search

results = search(
    "How do I create infrastructure as code?"
)

for row in results:
    print("\n-------------------")
    print(f"ID: {row.id}")
    print(f"Distance: {row.distance}")
    print(row.content)