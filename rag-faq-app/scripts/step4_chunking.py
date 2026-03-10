from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def load_documents():
    pdf_path = get_project_root() / "data" / "faq.pdf"
    loader = PyPDFLoader(str(pdf_path))
    return loader.load()


def split_into_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)


def main():
    documents = load_documents()
    chunks = split_into_chunks(documents)

    print("Total pages:", len(documents))
    print("Total chunks:", len(chunks))

    print("\n--- SAMPLE CHUNK ---\n")
    print(chunks[0].page_content)


if __name__ == "__main__":
    main()
