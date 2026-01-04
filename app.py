import streamlit as st
import numpy as np
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer


st.set_page_config(
    page_title='Semantic Question Search',
    page_icon="🔍",
    layout="wide"
)

# load resources

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

@st.cache_resource
def load_index():
    return faiss.read_index('faiss_index.index')

@st.cache_data
def load_questions():
    return pd.read_csv('ques_emd.csv')['question'].tolist()


model = load_model()
index = load_index()
questions = load_questions()


# UI
st.title("🔍 Semantic Question Search Engine")
st.markdown("Find similar questions using AI-powered semantic search across 100K+ Quora questions")


#search interface
query = st.text_input(
    "Enter your question:",
    placeholder="e.g. How do I learn machine learning?",
    key='search_query'
)

top_k = st.slider("No. of results:", 3,10,5)


if st.button("Search", type="primary") or query:
    if query.strip():
        with st.spinner("Searching..."):
            # Encode query
            query_embedding = model.encode([query], convert_to_numpy=True)
            faiss.normalize_L2(query_embedding)
            
            # Search
            distances, indices = index.search(query_embedding, top_k + 1)
            
            # Display results
            st.subheader("Similar Questions:")
            
            results_count = 0
            for idx, score in zip(indices[0][1:], distances[0][1:]):
                if questions[idx].lower() != query.lower() and results_count < top_k:
                    results_count += 1
                    
                    # Color code by similarity
                    if score > 0.7:
                        color = "🟢"
                    elif score > 0.5:
                        color = "🟡"
                    else:
                        color = "🔴"
                    
                    with st.container():
                        col1, col2 = st.columns([0.9, 0.1])
                        with col1:
                            st.markdown(f"**{results_count}.** {questions[idx]}")
                        with col2:
                            st.markdown(f"{color} {score:.2%}")
                        st.divider()
    else:
        st.warning("Please enter a question to search")

# Sidebar info
with st.sidebar:
    st.header("About")
    st.info(f"""
    **Dataset:** Quora Question Pairs
    
    **Total Questions:** {len(questions):,}
    
    **Model:** Sentence Transformer (all-MiniLM-L6-v2)
    
    **Search Method:** FAISS + Cosine Similarity
    
    **Average Search Time:** <100ms
    """)
    
    st.header("Example Queries")
    examples = [
        "How do I learn Python?",
        "What is the best way to lose weight?",
        "How can I make money online?",
        "What are good books to read?",
    ]
    
    for ex in examples:
        if st.button(ex, key=ex):
            st.session_state.search_query = ex
            st.rerun()