def retrieve_relevant_chunks(vectorstore,query,k=1):
    """Retrive Top-k relevant chunks from the vectorstore based on the query."""
    results=vectorstore.similarity_search(query,k=k)
    retrieved=[]
    for doc in results:
        retrieved.append({
            "text":doc.page_content,
            "metadata":doc.metadata
        })

    return retrieved