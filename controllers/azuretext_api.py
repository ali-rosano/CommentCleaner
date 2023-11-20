from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from controllers.connection import AZURE_TEXTANALYTICS_KEY, AZURE_TEXTANALYTICS_ENDPOINT


def authenticate_client():
    """
    The function `authenticate_client` authenticates and returns the client for Text Analytics.
    :return: an instance of the TextAnalyticsClient class, which is authenticated and ready to be used
    for Text Analytics tasks.
    """
    key = AZURE_TEXTANALYTICS_KEY
    endpoint = AZURE_TEXTANALYTICS_ENDPOINT
    ta_credential = AzureKeyCredential(key)
    return TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)


def detect_language(text_analytics_client, text):
    """
    The function `detect_language` uses the Text Analytics client to detect the language of a given
    text.

    :param text_analytics_client: The `text_analytics_client` parameter is an instance of the Text
    Analytics client that is used to interact with the Text Analytics service. It is responsible for
    making API calls to perform language detection
    :param text: The text parameter is the input text that you want to detect the language of
    :return: the name of the primary language detected in the given text.
    """
    try:
        response = text_analytics_client.detect_language(
            documents=[text], country_hint="us"
        )[0]
        return response.primary_language.name
    except Exception as err:
        print("Error al detectar el idioma:", err)
        return None


def detect_language_for_column(dataframe):
    """
    The function `detect_language_for_column` detects the language of the text in the "text" column of a
    DataFrame.

    :param dataframe: The parameter "dataframe" is a Pandas DataFrame object that contains a column
    named "text" which contains text data. The function "detect_language_for_column" is designed to
    detect the language of each text in the "text" column using the Azure Text Analytics API. It returns
    the original DataFrame
    :return: the updated DataFrame with an additional column "Detected_Language" that contains the
    detected language for each text in the "text" column.
    """
    text_analytics_client = authenticate_client()

    dataframe["Detected_Language"] = dataframe["text"].apply(
        lambda x: detect_language(text_analytics_client, x)
    )
    return dataframe
