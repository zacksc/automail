import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
import re

nltk.download('stopwords')
nltk.download('rslp')

stop_words = set(stopwords.words('portuguese'))

stemmer = RSLPStemmer()

def preprocessar_texto(texto):
    texto = texto.lower()

    texto = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", texto)

    palavras = texto.split()

    palavras_filtradas = [
        stemmer.stem(p)
        for p in palavras
        if p not in stop_words
    ]

    return " ".join(palavras_filtradas)