import chromadb

client = chromadb.PersistentClient(
    path="./chroma_storage"
)

startup_collection = client.get_or_create_collection(
    name="startup_knowledge"
)