from transformers import pipeline
summarizer = pipeline("summarization", model="t5-small")

def summarize_cluster(sentences):
    joined = " ".join(sentences)
    return summarizer(joined, max_length=30, min_length=5, do_sample=False)[0]['summary_text']