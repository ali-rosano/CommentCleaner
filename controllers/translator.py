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
    """
    The function `translate_df` takes a DataFrame as input, checks the detected language of each row's
    text, and translates the text to English if it is in Spanish, otherwise it keeps the text as is if
    it is in English, and drops any rows with missing translated text.

    :param df: The parameter "df" is a pandas DataFrame that contains the data to be translated. It is
    assumed that the DataFrame has the following columns:
    :return: the input DataFrame `df` with an additional column called "Translated_Text". The values in
    this column are the translated versions of the "text" column if the detected language is Spanish, or
    the original "text" values if the detected language is English. Any rows with missing values in the
    "Translated_Text" column are dropped from the DataFrame before returning it.
    """
    df["Translated_Text"] = df.apply(
        lambda row: translate_text(row["text"])
        if row["Detected_Language"] == "Spanish"
        else row["text"]
        if row["Detected_Language"] == "English"
        else None,
        axis=1,
    )
    df = df.dropna(subset=["Translated_Text"])
    return df


"""
    Después de investigar la implementación de modelos de Hugging Face y de realizar pruebas para traducir nuestros textos 
    únicamente del español al inglés, descubrimos que existen modelos capaces de traducir desde cualquier idioma al inglés 
    sin depender de una API para determinar el idioma. Esta capacidad no solo simplifica el desarrollo, sino que también mejora 
    la eficiencia del proceso.

    Si bien por motivos formativos actualmente estamos utilizando la API de Azure, que traduce únicamente desde un idioma detectado,
    hemos tomado la decisión de en un futuro incluir en nuestro proyecto el uso de modelos que permiten la traducción desde 
    cualquier idioma al inglés. Reconocemos que esta solución es más completa y beneficiosa para nuestro objetivo final


    from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
    model_name = "facebook/mbart-large-50-many-to-many-mmt"
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name)

    texts_to_translate = [
        "Hola, este es un ejemplo de texto en español.",
        "Bonjour, ceci est un exemple de texte en français.",
        "Hallo, dies ist ein Beispieltext auf Deutsch."
    ]

    for text in texts_to_translate:
        translated_ids = tokenizer(text, return_tensors="pt").input_ids
        translated = model.generate(translated_ids, decoder_start_token_id=model.config.decoder.pad_token_id, max_length=128, num_beams=4)
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

"""
