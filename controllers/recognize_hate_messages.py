from transformers import pipeline


def recognize_hate_messages(df):
    """
    The function `recognize_hate_messages` takes a DataFrame as input, uses a pre-trained model to
    classify hate speech in the text, and returns a DataFrame with the original text and the
    corresponding hate label.

    :param df: The parameter `df` is expected to be a pandas DataFrame containing the data to be
    classified. It should have a column named "Translated_Text" which contains the text messages to be
    classified as hate or non-hate messages
    :return: a DataFrame with two columns: "Translated_Text" and "Hate_Label".
    """
    classifier = pipeline(
        "text-classification", model="Hate-Speech-CNERG/dehatebert-mono-english"
    )

    texts_to_classify = df["Translated_Text"].tolist()
    results = classifier(texts_to_classify)
    hate_labels = [result["label"] for result in results]
    df["Hate_Label"] = hate_labels
    return df[["Translated_Text", "Hate_Label"]]
