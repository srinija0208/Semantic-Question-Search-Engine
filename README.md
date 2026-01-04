# 🔍 Semantic Question Search Engine

AI-powered search engine using Sentence Transformer and FAISS for finding similar questions across 100K+ Quora questions.

## 🎯 Features
- **Semantic Search**: Understanding meaning, not just keywords
- **Fast Retrieval**: Sub-100ms search using FAISS indexing
- **Scalable**: Handles 100K+ questions efficiently
- **Interactive UI**: Clean Streamlit interface



**Components:**
1. Sentence-Transformer for embeddings (384-dim)
2. FAISS for similarity search (IndexFlatIP)
3. Streamlit for web interface
4. HuggingFace Spaces for deployment

## 📊 Performance
- **Search Speed**: <100ms average
- **Index Size**: 100,000 questions
- **Model**: all-MiniLM-L6-v2

## 🚀 Live Demo



## 💻 Local Setup
\`\`\`bash

git clone (https://github.com/srinija0208/Semantic-Question-Search-Engine.git)

cd semantic-search-engine

pip install -r requirements.txt

streamlit run app.py

\`\`\`



## 🛠️ Tech Stack
- Python 3.9+
- Sentence-Transformers
- FAISS
- Streamlit
- Pandas, NumPy



## 📈 Future Enhancements
- Hybrid search (dense + sparse)
- Multi-language support
- Query expansion
- User feedback loop

