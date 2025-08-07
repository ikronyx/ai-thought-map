import networkx as nx
from pyvis.network import Network
import streamlit.components.v1 as components

def generate_graph(sentences, labels):
    G = nx.Graph()
    clusters = {}

    # Use integer labels to avoid serialization issues
    for idx, (sentence, label) in enumerate(zip(sentences, labels)):
        idx = int(idx)
        label = int(label)  # Ensure label is an int
        G.add_node(idx, label=sentence, group=label)
        clusters.setdefault(label, []).append(idx)

    for cluster_nodes in clusters.values():
        for i in range(len(cluster_nodes)):
            for j in range(i+1, len(cluster_nodes)):
                G.add_edge(int(cluster_nodes[i]), int(cluster_nodes[j]))

    net = Network(notebook=False, height="500px", width="100%")
    net.from_nx(G)
    net.repulsion()

    net.save_graph("graph.html")
    return "graph.html"
