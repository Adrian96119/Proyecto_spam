import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suprimo warnings
import sys
sys.stdout.reconfigure(encoding='utf-8')
from predictor import predecir_mensaje, modelo, scaler, tokenizer
from config import max_len
from googletrans import Translator

def main():
    print("📨 ¡Bienvenido al Detector de SPAM! 🚀")
    print("Introduce un mensaje SMS (en cualquier idioma), y te diré si es SPAM o NO SPAM.\n")
    print("⚠️ Nota: El mensaje debe tener un máximo de 100 palabras. Vamos a ello.\n")

    translator = Translator()  # Inicializo el traductor

    while True:
        sms = input("✉️ Escribe tu mensaje: ").strip()

        # Valido longitud del mensaje
        word_count = len(sms.split())
        if word_count > 100:
            print("⚠️ El mensaje excede las 100 palabras. Por favor, inténtalo de nuevo.")
            continue

        try:
            # Detecto el idioma y traduzco al inglés si es necesario
            detected_lang = translator.detect(sms).lang
            if detected_lang != 'en':
                translation = translator.translate(sms, src=detected_lang, dest='en')
                if translation is None or not hasattr(translation, 'text'):
                    raise ValueError("Error al traducir el mensaje.")
                sms = translation.text
                

            # predicción
            resultado = predecir_mensaje(sms, modelo, scaler, tokenizer)
            print(f"\n🤖 Predicción: {resultado}\n")

        except Exception as e:
            print(f"❌ Ocurrió un error al procesar tu mensaje: {e}")

        # Pregunto si quiere analizar otro mensaje
        otra_vez = input("¿Quieres analizar otro mensaje? (s/n): ").lower()
        if otra_vez != 's':
            print("👋 ¡Gracias por usar el Detector de SPAM! Hasta la próxima. 🛡️")
            break

if __name__ == "__main__":
    main()
