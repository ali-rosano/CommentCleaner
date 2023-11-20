from transformers import MarianMTModel, MarianTokenizer


def translate_text(text_to_translate, model_name="Helsinki-NLP/opus-mt-es-en"):
    # Cargar el modelo y el tokenizador
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenizar el texto
    tokens = tokenizer(text_to_translate, return_tensors="pt")

    # Traducir el texto
    translated = model.generate(**tokens)
    translated_sentence = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_sentence


def translate_df(df):
    mask = df["Detected_Language"] == "Spanish"
    df.loc[mask, "Translated_Text"] = df[mask]["text"].apply(translate_text)
    return df
