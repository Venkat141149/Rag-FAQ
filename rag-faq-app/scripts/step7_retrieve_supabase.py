import os
from dotenv import load_dotenv

from supabase import create_client
from langchain_openai import OpenAIEmbeddings

load_dotenv()


def main():
    # Connect to Supabase
    supabase = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_KEY")
    )

    # Question to test
    user_question = "Are pets allowed in the society?"

    # Create embedding for the question
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    query_embedding = embeddings.embed_query(user_question)

    # Call Supabase vector search function
    response = supabase.rpc(
        "match_documents",
        {
            "query_embedding": query_embedding,
            "match_count": 1
        }
    ).execute()

    print("User question:")
    print(user_question)
    print("\nTop matching chunks:\n")

    for i, row in enumerate(response.data, start=1):
        print(f"{i}. Similarity: {row['similarity']:.4f}")
        print(row["content"])
        print("-" * 50)


if __name__ == "__main__":
    main()
