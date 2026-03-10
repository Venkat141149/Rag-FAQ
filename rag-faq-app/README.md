## RAG FAQ App (Python)

This is a beginner-friendly folder structure for a small RAG-style FAQ project in Python. It currently only includes **PDF loading and text extraction**, with no embeddings, databases, APIs, or LLM calls.

### Project structure

- `rag-faq-app/`
  - `venv/` — Python virtual environment (created locally, not committed)
  - `data/` — PDF files used as source documents
    - `faq.pdf` — placeholder FAQ PDF
  - `scripts/` — simple learning / utility scripts
    - `step3_pdf_extract.py` — loads and prints text from `data/faq.pdf`
  - `.env` — environment variables (currently just `OPENAI_API_KEY=`)
  - `requirements.txt` — minimal Python dependencies
  - `README.md` — this file

### 1. Create and activate a virtual environment

From inside the `rag-faq-app` folder:

```bash
python -m venv venv

# On Windows PowerShell
venv\Scripts\Activate.ps1

# On Windows cmd.exe
venv\Scripts\activate.bat

# On macOS / Linux
source venv/bin/activate
```

### 2. Install dependencies

With the virtual environment active:

```bash
pip install -r requirements.txt
```

### 3. Add your FAQ PDF

- Place your actual FAQ PDF file at: `data/faq.pdf`
- The placeholder file is just there so paths work; replace it with your own PDF.

### 4. Run the PDF extraction script

From the `rag-faq-app` folder, with the virtual environment active:

```bash
python scripts/step3_pdf_extract.py
```

What it does:

- Uses `PyPDFLoader` to load `data/faq.pdf`
- Splits the PDF into page-level documents
- Prints a small sample of text to the terminal

### 5. Next steps (optional ideas)

This starter structure is intentionally minimal. Some ideas for what you might add later:

- Extra scripts for cleaning or chunking text
- Simple local search over the extracted text
- LLM-based Q&A (once you are ready), using the text you extracted

For now, this repository only focuses on **loading and reading a PDF file**.
