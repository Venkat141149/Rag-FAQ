from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings



load_dotenv()


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def load_and_chunk():
    pdf_path = get_project_root() / "data" / "faq.pdf"

    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)


def main():
    chunks = load_and_chunk()

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector = embeddings.embed_query(chunks[0].page_content)

    print("Number of chunks:", len(chunks))
    print("Embedding vector length:", len(vector))
    print("First 10 values of embedding:")
    print(vector[:10])


if __name__ == "__main__":
    main()
