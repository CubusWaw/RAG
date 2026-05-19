# PDF RAG Reader

A local Retrieval-Augmented Generation (RAG) demo that lets you query PDF documents using a fully offline stack — no cloud APIs required.

Built with LangChain, ChromaDB, HuggingFace sentence transformers, and Ollama.

---

## Demo

The included sample uses the *Ant-Man* press kit PDF.  
Example query:
```
Extract all 3D Stereoscopic people, separate them by comma
```

---

## How it works

```
PDFs  →  text chunks  →  HuggingFace embeddings  →  ChromaDB vector store
                                                              ↓
              query  →  retriever  →  Ollama (local LLM)  →  answer
```

1. **Ingest** — PDFs are loaded, split into overlapping chunks, embedded with a sentence transformer, and persisted in a local Chroma vector store.
2. **Query** — At query time the pipeline retrieves the top-k most relevant chunks and passes them as context to a local Ollama LLM, which returns a grounded answer.

---

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) installed and running locally
- A GPU is recommended (CUDA); CPU works but is slower

### Pull the default LLM

```bash
ollama pull qwen:14b
```

---

## Installation

```bash
git clone https://github.com/<your-username>/pdfReader.git
cd pdfReader
pip install -r requirements.txt
```

---

## Usage

### 1. Run the reader

```bash
python PDF_reader.py
```

You will be prompted for the path to a directory of PDF files.  
Press **Enter** to use the bundled sample in `press_kit/`.

### 2. Ask questions

```
What are you looking for?
> Extract all 3D Stereoscopic people, separate them by comma
```

Type `exit` to quit.

---

## Configuration

All parameters live in [`config.yml`](config.yml):

| Key | Default | Description |
|-----|---------|-------------|
| `CHUNK_SIZE` | `100` | Token chunk size for text splitting |
| `CHUNK_OVERLAP` | `10` | Overlap between consecutive chunks |
| `NUM_RESULTS` | `5` | Top-k chunks retrieved per query |
| `EMBEDDINGS` | `sentence-transformers/all-mpnet-base-v2` | HuggingFace embedding model |
| `VECTOR_DB` | `vectorstore/sparrow` | Path to Chroma persist directory |
| `DEVICE` | `cuda` | `cuda` or `cpu` |
| `LLM` | `qwen:14b` | Ollama model name |
| `VECTOR_SPACE` | `cosine` | Chroma distance metric |

---

## Project structure

```
pdfReader/
├── PDF_reader.py       # Entry point — ingest + interactive query loop
├── ingest.py           # PDF loading, chunking, embedding, vector store creation
├── rag/
│   └── pipeline.py     # RAG pipeline: embeddings, retriever, prompt, QA chain
├── config.yml          # All tunable parameters
├── requirements.txt
├── press_kit/          # Sample PDFs (Ant-Man press kit)
├── data/               # Drop your own PDFs here
└── vectorstore/        # Auto-generated Chroma DB (git-ignored)
```

---

## Stack

| Component | Library |
|-----------|---------|
| Document loading & pipeline | [LangChain](https://github.com/langchain-ai/langchain) |
| Embeddings | [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) |
| Vector store | [ChromaDB](https://www.trychroma.com/) |
| Local LLM | [Ollama](https://ollama.com/) (`qwen:14b` / `zephyr:7b-alpha-q5_K_M`) |

---

## License

[MIT](LICENSE)
