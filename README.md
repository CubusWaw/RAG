# RAG Demo

A minimal Retrieval-Augmented Generation demo running fully locally. Uses **Qwen 2.5** for generation and HuggingFace sentence-transformers for embeddings — no external API keys required.

## Features

- 100% local inference (no OpenAI, no Anthropic, no cloud)
- Qwen 2.5 as the generator model
- HuggingFace embeddings for semantic search
- Local vector store (FAISS / Chroma)
- Simple CLI for indexing documents and asking questions
- Works on CPU; GPU recommended for reasonable speed

## Requirements

- Python 3.10+
- ~8 GB free disk space for model weights
- CUDA-capable GPU recommended (CPU works but is slow)

## Installation

```bash
git clone <repo-url>
cd <repo-folder>

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

Model weights are downloaded automatically from HuggingFace on first run.

## Usage

**1. Index your documents**

Drop your `.txt` / `.md` / `.pdf` files into the `docs/` folder, then build the index:

```bash
python ingest.py --source docs/
```

**2. Ask questions**

```bash
python query.py "What is the main argument of the paper?"
```

Example output:

```
> What is the main argument of the paper?

Answer: The paper argues that ...
Sources:
  - docs/paper.pdf (p. 3)
  - docs/notes.md
```

## Project Structure

```
.
├── ingest.py          # Loads, chunks, and embeds documents
├── query.py           # CLI for asking questions
├── rag/
│   ├── embedder.py    # HuggingFace embedding wrapper
│   ├── store.py       # Vector store interface
│   └── llm.py         # Qwen 2.5 wrapper
├── docs/              # Your source documents
└── requirements.txt
```

## Configuration

Edit `config.yaml` to change models, chunk size, or top-k retrieval:

```yaml
llm_model: Qwen/Qwen2.5-7B-Instruct
embedding_model: sentence-transformers/all-MiniLM-L6-v2
chunk_size: 512
top_k: 4
```

## License

MIT
"# RAG" 
