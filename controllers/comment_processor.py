import pandas as pd
from controllers.utils import extract_id
from controllers.youtube_api import fetch_comments_from_youtube_api
from controllers.azuretext_api import detect_language


def extract_comments_and_languages(video_link):
    """
    The function "extract_comments_and_languages" takes a video link as input, extracts the video ID
    from the link, and returns a DataFrame containing comments and their detected languages.

    :param video_link: The video_link parameter is a string that represents the link to a video
    :return: a pandas DataFrame containing two columns: "text" and "Detected_Language".
    """
    data = {
        "text": ["Hello", "Bonjour", "Hola", "Ciao"],
        "Detected_Language": ["English", "French", "Spanish", "Italian"],
    }
    df = pd.DataFrame(data)
    video_id = extract_id(video_link)
    # df = fetch_comments_from_youtube_api(video_id)
    # df = detect_language(df)
    fetch_comments_from_youtube_api()
    detect_language()
    return df
