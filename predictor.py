import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  #Suprimo warnings
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from functions import calculate_features, limpiar_texto_spacy
from listas_varias import messages, numeric_features
from dataset_handler import scaler, X_train
from config import max_words, max_len, modelo_path


# Inicio el Tokenizer y cargo el modelo entrenado
tokenizer = Tokenizer(num_words=max_words, oov_token="<OOV>")
tokenizer.fit_on_texts(X_train['mensaje_limpio'])
modelo = load_model(modelo_path)


def preparar_mensaje(sms, scaler, tokenizer):
    """
    Preparo un mensaje SMS para la predicción:
    1. Limpieza del texto.
    2. Calculo de características numéricas.
    3. Normalización de las características numericas.
    4. Tokenización y aplicación de padding al texto.
    """
    # Limpieza y cálculo de características
    texto_limpio = limpiar_texto_spacy(sms)
    mensaje_caracteristicas = calculate_features(sms)

    # Creo DataFrame temporal para procesar características
    df = pd.DataFrame([mensaje_caracteristicas], columns=numeric_features)
    df[numeric_features] = scaler.transform(df[numeric_features])

    # Tokenización y padding del mensaje limpio
    text_sequence = tokenizer.texts_to_sequences([texto_limpio])
    text_padded = pad_sequences(text_sequence, maxlen=max_len, padding='post', truncating='post')

    return text_padded, df[numeric_features].values


def predecir_mensaje(sms, modelo, scaler, tokenizer):
    
    #preparo mensaje para la predicción
    text_padded, features_array = preparar_mensaje(sms, scaler, tokenizer)

    # Realizo predicción
    prediccion = modelo.predict([text_padded, features_array], verbose=0)[0][0]

    # Formateo el resultado
    probabilidad_spam = f"{prediccion * 100:.2f}"
    probabilidad_no_spam = f"{(1 - prediccion) * 100:.2f}"
    if prediccion > 0.5:
        return f"SPAM ({probabilidad_spam}%)"
    else:
        return f"NO SPAM ({probabilidad_no_spam}%)"


def main():
    """
    Canalizador principal para realizar predicciones en una lista de mensajes. (testeos)
    """
    print("INICIANDO PRUEBAS DE PREDICCION EN LA LISTA DE MENSAJES...\n")

    # Probando todos los mensajes de `messages` y mostrar resultados
    for i, sms in enumerate(messages):
        resultado = predecir_mensaje(sms, modelo, scaler, tokenizer)
        print(f"Mensaje {i+1}: {sms}")
        print(f"Resultado: {resultado}")
        print("-" * 50)

    print("\nPREDICCIONES COMPLETADAS.\n")


if __name__ == "__main__":
    main()



