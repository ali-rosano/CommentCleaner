import pandas as pd
from controllers.utils import extract_id


def extract_comments_and_languages(video_link):
    data = {
        "text": ["Hello", "Bonjour", "Hola", "Ciao"],
        "Detected_Language": ["English", "French", "Spanish", "Italian"],
    }
    df = pd.DataFrame(data)
    video_link = extract_id(video_link)
    print(video_link)
    return df
