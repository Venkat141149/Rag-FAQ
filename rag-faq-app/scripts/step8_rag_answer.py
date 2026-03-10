import os
from dotenv import load_dotenv

from supabase import create_client
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

load_dotenv()

# Initialize Supabase client (once)
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_KEY")
)

# Initialize embedding model (once)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Initialize LLM (once)
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def get_rag_answer(user_question: str) -> str:
    """
    Takes a user question, retrieves relevant chunks from Supabase,
    and generates a final answer using GPT.
    """

    # 1. Convert question to embedding
    query_embedding = embeddings.embed_query(user_question)

    # 2. Retrieve relevant chunks from Supabase
    response = supabase.rpc(
        "match_documents",
        {
            "query_embedding": query_embedding,
            "match_count": 3
        }
    ).execute()

    # 3. Build context from retrieved chunks
    context = "\n\n".join(
        [row["content"] for row in response.data]
    )

    # 4. Construct prompt
    prompt = f"""
You are an assistant for a housing society.

Answer the question using ONLY the context below.
If the answer is not present in the context, say "Information not available."

Context:
{context}

Question:
{user_question}
"""

    # 5. Generate answer
    result = llm.invoke(prompt)

    return result.content
