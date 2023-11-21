from controllers.utils import extract_id
from controllers.youtube_api import fetch_comments_from_youtube_api
from controllers.azuretext_api import detect_language_for_column
from controllers.translator import translate_df
from controllers.recognize_hate_messages import recognize_hate_messages


def extract_comments_and_languages(video_link):
    """
    The function "extract_comments_and_languages" takes a video link as input, extracts the video ID
    from the link, and returns a DataFrame containing comments and their detected languages.

    :param video_link: The video_link parameter is a string that represents the link to a video
    :return: a pandas DataFrame containing two columns: "text" and "Detected_Language".
    """
    video_id = extract_id(video_link)
    df = fetch_comments_from_youtube_api(video_id)
    df = detect_language_for_column(df)
    df = translate_df(df)
    df = recognize_hate_messages(df)
    return df
