# Retrieval strategies: dense (used for RAGAS baseline), then +BM25 (Best Matching 25), then hybrid search (combine dense with BM25), then +rerank
import chromadb
from pipeline.embeddings import embed 

chroma_client = chromadb.PersistentClient(path="chroma_db")   # persistent Client and collection 
collection = chroma_client.get_or_create_collection(name="wiki-rag")  

def retrieve(question: str , article_title: str , n_results: int=5) -> list[dict]:

    embedded_query = embed([question])[0]   #the functon takes a list as argument not a single string. Fix wrap in a list and unwrap by index
    results = collection.query(
        query_embeddings = [embedded_query],
        n_results = 5,
        where={"article_title": article_title}
    ) 
    return results 


print(retrieve("What is computer science?", "Computer science"))