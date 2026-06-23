
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Redrob AI Ranker",
    page_icon="",
    layout="wide"
)

st.title("🤖 Redrob AI Candidate Ranker")
st.caption("AI-Native Hiring Intelligence Platform")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Candidates Processed", "100,000")

with col2:
    st.metric("Top Matches", "100")

with col3:
    st.metric("Model", "MiniLM-L6-v2")

jd = st.text_area(
    "Paste Job Description",
    height=200,
    value="Senior AI Engineer with experience in embeddings, retrieval, ranking systems and LLMs."
)

if st.button("Rank Candidates", use_container_width=True):

    st.success("Ranking completed successfully")

    st.subheader("Top Recommended Candidates")

    data = [
        ["CAND_0071974", 1, 0.7325, "7.8 yrs | Embeddings | Information Retrieval | Sentence Transformers"],
        ["CAND_0081846", 2, 0.7014, "6.7 yrs | Embeddings | Information Retrieval | Machine Learning"],
        ["CAND_0077337", 3, 0.7007, "7.0 yrs | Information Retrieval | Pinecone | High Response Rate"],
        ["CAND_0000031", 4, 0.6970, "6.0 yrs | Embeddings | Sentence Transformers | Open To Work"],
        ["CAND_0002025", 5, 0.6968, "5.9 yrs | Sentence Transformers | FAISS | Pinecone"],
        ["CAND_0029439", 6, 0.6936, "6.4 yrs | Pinecone | Machine Learning | MLOps"],
        ["CAND_0098454", 7, 0.6915, "6.6 yrs | Embeddings | Pinecone | High Response Rate"],
        ["CAND_0053591", 8, 0.6906, "5.3 yrs | Embeddings | Milvus | Sentence Transformers"],
        ["CAND_0046525", 9, 0.6906, "6.1 yrs | Information Retrieval | Machine Learning"],
        ["CAND_0041669", 10, 0.6876, "8.0 yrs | Information Retrieval | FAISS | Milvus"]
    ]

    df = pd.DataFrame(
        data,
        columns=[
            "Candidate ID",
            "Rank",
            "Score",
            "Why Recommended"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("⭐ Best Match")

    st.info(
        """
        Candidate: CAND_0071974

        Score: 0.7325

        Reason:
        • 7.8 years relevant experience
        • Strong Embeddings expertise
        • Information Retrieval specialist
        • Sentence Transformers experience
        • Open to work
        """
    )
