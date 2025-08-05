from sklearn.cluster import DBSCAN

def cluster_embeddings(embeddings, eps=0.5, min_samples=2):
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(embeddings)
    return clustering.labels_