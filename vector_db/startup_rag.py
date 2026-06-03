from vector_db.chroma_client import (
    startup_collection
)

from services.embedding_service import (
    create_embedding
)


def store_startup_research(
    startup_id,
    idea,
    report
):

    document = f"""
    Startup Idea:
    {idea}

    Startup Report:
    {report}
    """

    embedding = create_embedding(
        document
    )

    startup_collection.add(

        ids=[
            str(startup_id)
        ],

        embeddings=[
            embedding
        ],

        documents=[
            document
        ],

        metadatas=[
            {
                "idea": idea
            }
        ]
    )

    return True


def find_similar_startups(
    query,
    n_results=5
):

    query_embedding = create_embedding(
        query
    )

    results = startup_collection.query(

        query_embeddings=[
            query_embedding
        ],

        n_results=n_results
    )

    return results


def get_all_records():

    return startup_collection.get()