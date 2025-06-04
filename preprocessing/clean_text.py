import re
import nltk
from nltk.corpus import stopwords

stop_words_en = set(stopwords.words('english'))

def clean_text_for_ner(text):
    """
    Limpia el texto eliminando URLs y caracteres especiales innecesarios,
    manteniendo las mayúsculas para el NER.
    """
    text = re.sub(r'http\S+', '', text)  # Elimina URLs
    text = re.sub(r'[^a-zA-Z\s.,!?"\'()]', '', text) # Mantiene letras, espacios y signos de puntuación comunes
    text = re.sub(r'@\s*@\s*@\s*@\s*', '', text) # Elimina secuencias de @ repetidas con espacios opcionales
    return text

def remove_stopwords(text):
    """Elimina las stopwords del texto."""
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words_en] # Convertir a minúsculas para la comparación
    return " ".join(filtered_words)

def clean_news_items(news_items):
    cleaned = []
    for item in news_items:
        raw_text = item['text']
        no_stopwords = remove_stopwords(raw_text)
        cleaned_text = clean_text_for_ner(no_stopwords)

        cleaned.append({
            'id': item['id'],
            'cleaned_text': cleaned_text,
            'font': item['font'],
        })
    return cleaned