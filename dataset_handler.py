import pandas as pd
from sklearn.model_selection import train_test_split
from listas_varias import columnas_importantes, numeric_features
from sklearn.preprocessing import MinMaxScaler

# Cargo el dataset con los sms limpios
df_sms_limpio = pd.read_csv("sms_procesado.csv")


spam_original = df_sms_limpio[(df_sms_limpio['etiqueta'] == 'spam') & (df_sms_limpio['origen'] == 'original')]
spam_ficticio = df_sms_limpio[(df_sms_limpio['etiqueta'] == 'spam') & (df_sms_limpio['origen'] == 'ficticio')]
not_spam = df_sms_limpio[df_sms_limpio['etiqueta'] == 'ham']

# Division de no spam original en entrenamiento y prueba
not_spam_train, not_spam_test = train_test_split(not_spam, test_size=0.30, random_state=42)

# Dividir spam original entre validación y prueba (aunque solo usaremos prueba para no incluir ficticios)
spam_original_train, spam_original_test = train_test_split(spam_original, test_size=0.50, random_state=42)

# Creando un conjunto de entrenamiento con spam ficticio y una fracción de los no spam originales
train_set = pd.concat([spam_ficticio, not_spam_train, spam_original_train.sample(frac=0.10, random_state=42)])

# Selecciono las columnas que necesito
train_set = train_set[columnas_importantes]

# Relleno los valores nulos en 'mensaje_limpio' con "mensaje_vacio" en el conjunto de entrenamiento por si hay alguno después del preprocesamiento
train_set['mensaje_limpio'] = train_set['mensaje_limpio'].fillna("mensaje_vacio")


scaler = MinMaxScaler()

# Ajustamos y transformamos los datos en el conjunto de entrenamiento
train_set[numeric_features] = scaler.fit_transform(train_set[numeric_features])


X_train = train_set #Nos quedamos solo con el entrenamiento



