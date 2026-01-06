# 🔍 Semantic Question Search Engine

AI-powered search engine using Sentence Transformer and FAISS for finding similar questions across 100K+ Quora questions.

## 🎯 Features
- **Semantic Search**: Retrieves questions based on intent and meaning rather than keywords
- **Fast Retrieval**: Sub-100ms search latency using FAISS vector indexing
- **Scalable**: Efficiently handles large question corpora (100K+ questions)
- **Interactive UI**: Clean and intuitive Streamlit web interface



## 🧩 Components

1. **Sentence-Transformer (all-MiniLM-L6-v2)** for semantic embeddings (384-dim)

2. **FAISS (IndexFlatIP)** for efficient similarity search

3. **Streamlit** for web-based interaction

4. **Hugging Face Spaces** for deployment

## 📊 Evaluation

The system was evaluated using human-judged Precision@K, where the top-K retrieved questions for each query were manually assessed for semantic relevance. Evaluation was performed on a small set of representative, in-domain queries, reflecting real-world semantic search behavior in the absence of labeled ranking data(Manual relevance testing on 15 diverse queries with top-5 results per query).

## ⚡ Performance

- **Average Search Latency:** <100ms

- **Corpus Size:** ~100,000 questions

- **Embedding Model:** all-MiniLM-L6-v2

- **Mean Precision@5:** 84% (human-judged, in-domain evaluation)

Note: Precision may vary for open-domain queries, which is a known challenge in semantic retrieval systems.

## 🚀 Live Demo



## 💻 Local Setup
```bash

git clone https://github.com/srinija0208/Semantic-Question-Search-Engine.git
```

```
cd Semantic-Question-Search-Engine
``` 

```
pip install -r requirements.txt
```

```
streamlit run app.py
```




## 🛠️ Tech Stack
- Python 3.9+
- Sentence-Transformers
- FAISS
- Streamlit
- Pandas, NumPy



## 📈 Future Enhancements
- Hybrid search (dense + sparse / TF-IDF + embeddings)

- Multi-language semantic search

- Query expansion techniques

- User feedback–driven relevance tuning

