from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def get_project_root() -> Path:
    """
    Return the project root directory (where this script's parent folder lives).

    This uses only relative-style paths based on this file's location, so you
    don't need to hard-code any absolute paths.
    """
    return Path(__file__).parent.parent


def get_pdf_path() -> Path:
    """Return the path to the FAQ PDF inside the data/ folder."""
    return get_project_root() / "data" / "faq.pdf"


def load_pdf_pages(pdf_path: Path):
    """
    Load the PDF into a list of page documents using PyPDFLoader.

    Each item in the returned list has a .page_content attribute containing
    the text for that page.
    """
    loader = PyPDFLoader(str(pdf_path))
    return loader.load()


def main() -> None:
    pdf_path = get_pdf_path()

    if not pdf_path.exists():
        print(f"PDF not found at: {pdf_path}")
        print("Make sure you have placed your FAQ file at data/faq.pdf")
        return

    print(f"Loading PDF from: {pdf_path}")
    pages = load_pdf_pages(pdf_path)

    print(f"Loaded {len(pages)} page(s). Showing a short preview:")
    print("-" * 40)

    # Show a small text sample from the first few pages
    max_pages_to_show = 3
    max_chars_per_page = 500

    for i, page in enumerate(pages[:max_pages_to_show], start=1):
        print(f"\n--- Page {i} ---")
        text = page.page_content[:max_chars_per_page]
        print(text if text.strip() else "[No text detected on this page]")


if __name__ == "__main__":
    main()
