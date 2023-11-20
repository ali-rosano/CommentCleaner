from transformers import pipeline


def recognize_hate_messages(df):
    print(df)
    classifier = pipeline(
        "text-classification", model="Hate-Speech-CNERG/dehatebert-mono-english"
    )

    # Extraer los textos a clasificar del DataFrame
    texts_to_classify = df["Translated_Text"].tolist()

    # Clasificar los textos
    results = classifier(texts_to_classify)

    # Extraer las etiquetas de odio
    hate_labels = [result["label"] for result in results]

    # Agregar las columnas con los resultados al DataFrame
    df["Hate_Label"] = hate_labels

    return df[["Translated_Text", "Hate_Label"]]
