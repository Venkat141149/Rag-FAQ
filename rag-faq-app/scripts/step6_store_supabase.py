from pathlib import Path
import os
from dotenv import load_dotenv

from supabase import create_client
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def load_and_chunk():
    """
    Load ALL PDF files from the data/ folder and split them into chunks.
    """
    data_dir = get_project_root() / "data"
    all_chunks = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )

    for pdf_file in data_dir.glob("*.pdf"):
        print(f"Processing file: {pdf_file.name}")

        loader = PyPDFLoader(str(pdf_file))
        documents = loader.load()

        chunks = splitter.split_documents(documents)

        # Attach file name to metadata
        for chunk in chunks:
            chunk.metadata["file_name"] = pdf_file.name

        all_chunks.extend(chunks)

    return all_chunks


def main():
    # Connect to Supabase
    supabase = create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_KEY")
    )

    # Initialize embedding model
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # Load and chunk all PDFs
    chunks = load_and_chunk()

    print(f"Total chunks to store: {len(chunks)}")

    # Store chunks in Supabase
    for chunk in chunks:
        vector = embeddings.embed_query(chunk.page_content)

        supabase.table("documents").insert({
            "content": chunk.page_content,
            "embedding": vector,
            "metadata": {
                "file_name": chunk.metadata.get("file_name"),
                "page": chunk.metadata.get("page")
            }
        }).execute()

    print("All chunks stored successfully in Supabase.")


if __name__ == "__main__":
    main()
 