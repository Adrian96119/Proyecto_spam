import regex as re
from listas_varias import spam_words
import nltk
from nltk.corpus import stopwords
import spacy

# Función para calcular características numéricas de los mensajes de texto
def calculate_features(text):
    # Longitud total del texto
    total_chars = len(text)
    if total_chars == 0:
        return [0] * len(feature_columns)  # Si el texto está vacío, retorna ceros para cada característica

    # Conteo de caracteres especiales
    special_characters_pattern = r'[!?.@$%&*()\-+/#:;<>]'
    special_char_count = len(re.findall(special_characters_pattern, text))

    # Conteo de exclamaciones
    exclamation_count = text.count('!')

    # Conteo de números
    number_count = len(re.findall(r'\d+', text))

    # Conteo de emoticonos
    emoticon_pattern = r'[:;=xX][\-~]?[)DdpP(]|<3'
    emoticon_count = len(re.findall(emoticon_pattern, text))

    # Longitud total del mensaje en caracteres
    message_length = total_chars

    # Conteo de palabras de spam comunes
    spam_word_count = sum(1 for word in text.lower().split() if word in spam_words)

    # Conteo y proporción de stop words
    stop_words = set(stopwords.words('english'))
    stop_word_count = sum(1 for word in text.lower().split() if word in stop_words)
    word_count = len(text.split())
    stop_word_ratio = stop_word_count / word_count if word_count > 0 else 0

    # Conteo de palabras en mayúsculas completas
    uppercase_word_count = sum(1 for word in text.split() if word.isupper())

    # Conteo de URLs en el mensaje
    url_regex = r"(http[s]?://\S+|www\.\S+|\S+\.(com|org|net|co\.uk|gov|edu|biz|info|in))"
    url_count = len(re.findall(url_regex, text))

    return [
        special_char_count,
        exclamation_count,
        number_count,
        emoticon_count,
        message_length,
        spam_word_count,
        stop_word_ratio,
        uppercase_word_count,
        url_count
    ]



#Función para preprocesar los sms y limpiarlos

def limpiar_texto_spacy(texto):
  # Cargando el modelo de spaCy en inglés 
  nlp = spacy.load('en_core_web_sm')

  # Normalizo a minúsculas
  texto = texto.lower()

  # Etiqueto URLs como <url>
  texto = re.sub(r'http\S+|www\.\S+', 'url', texto)

  # Etiqueto números como <numero>
  texto = re.sub(r'\b\d+\b', 'number', texto)

  # Eliminación de  cualquier carácter especial restante
  texto = re.sub(r'[^a-zA-Z0-9\s<>\s]', '', texto)

  # Procesar el texto con spaCy
  doc = nlp(texto)

  # Filtro stopwords, puntuación y lematizo
  texto_limpio = " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

  # Elimino palabras con menos de dos caracteres
  texto_limpio = " ".join([word for word in texto_limpio.split() if len(word) > 1])

  return texto_limpio