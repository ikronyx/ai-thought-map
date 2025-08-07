from sklearn.cluster import DBSCAN, AgglomerativeClustering, KMeans

def cluster_embeddings(embeddings, eps=0.5, min_samples=2, n_clusters=None):
    # Use DBSCAN or Agglomerative Clustering with proper parameters
    if n_clusters:
        clustering = KMeans(n_clusters=n_clusters, random_state=42).fit(embeddings)
    else:
        clustering = DBSCAN(eps=eps, min_samples=min_samples)
        clustering.fit(embeddings)
    return clustering.labels_
