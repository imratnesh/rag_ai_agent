import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("docs")

collection.add(
    ids=["doc1"],
    documents=["Artificial Intelligence is the simulation of human intelligence in machines."]
)

results = collection.query(query_texts=["What is AI?"], n_results=1)
print(results)
