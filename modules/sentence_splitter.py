import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def split_sentences(text):
    return [s.strip() for s in sent_tokenize(text) if len(s.strip()) > 0]