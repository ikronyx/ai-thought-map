import streamlit as st
from modules import sentence_splitter, embedder, clustering, visualizer, summarizer
from utils import exporter
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Thought Mapping", layout="wide")
st.title("🧠 AI Research Companion: Thought Mapping")
st.write("Paste messy notes. Get a visual web of ideas.")

text_input = st.text_area("Paste your unstructured research notes here:", height=300)

with st.sidebar:
    st.header("⚙️ Clustering Settings")
    eps = st.slider("Clustering threshold (DBSCAN - eps)", 0.1, 1.0, 0.5)
    min_samples = st.slider("Minimum samples per cluster", 1, 10, 2)
    n_clusters = st.slider("Number of clusters (KMeans)", 2, 10, 3)
    summarize = st.checkbox("Generate AI summaries for each cluster", value=False)

if st.button("🧠 Generate Thought Map") and text_input:
    with st.spinner("Processing text..."):
        sentences = sentence_splitter.split_sentences(text_input)
        embeddings = embedder.get_embeddings(sentences)
        labels = clustering.cluster_embeddings(embeddings, eps, min_samples, n_clusters)

        # Check if clustering is working correctly
        st.write("Cluster Labels:", labels)

        html_path = visualizer.generate_graph(sentences, labels)
        components.html(open(html_path, 'r', encoding='utf-8').read(), height=600, scrolling=True)

        st.subheader("🧩 Clustered Ideas")
        cluster_dict = {}
        for s, l in zip(sentences, labels):
            cluster_dict.setdefault(l, []).append(s)

        for label, group in cluster_dict.items():
            with st.expander(f"Cluster {label} ({len(group)} ideas)"):
                if summarize:
                    summary = summarizer.summarize_cluster(group)
                    st.markdown(f"**AI Summary:** {summary}")
                for idea in group:
                    st.markdown(f"- {idea}")

        json_export = exporter.export_json(sentences, labels)
        md_export = exporter.export_markdown(sentences, labels)

        st.subheader("📥 Export Your Map")
        st.download_button("Download JSON", json_export, file_name="thought_map.json")
        st.download_button("Download Markdown", md_export, file_name="thought_map.md")
