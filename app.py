from context_pruning import prune_context

documents = open("dataset.txt").read().split("\n\n")

question = input("Ask your question: ")

result = prune_context(question, documents)

print("\nRelevant Answer:")
print(result)
