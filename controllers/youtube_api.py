from controllers.connection import YOUTUBE_DEVELOPER_KEY
import googleapiclient.discovery
import pandas as pd


def build_youtube_client():
    """
    The function `build_youtube_client` builds and returns a client to interact with the YouTube API.
    :return: a client object that can be used to interact with the YouTube API.
    """
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = YOUTUBE_DEVELOPER_KEY
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )
    return youtube


def fetch_comments(youtube, video_id):
    """
    The function fetch_comments retrieves comments from a YouTube video using a YouTube client.

    :param youtube: The "youtube" parameter is the client object that is used to interact with the
    YouTube API. It should be an instance of the YouTube API client, which is typically created using
    the Google API client library
    :param video_id: The video_id parameter is the unique identifier of the YouTube video for which you
    want to fetch the comments. It is a string that represents the video's ID
    :return: a list of comment details extracted from the YouTube API response.
    """
    request = youtube.commentThreads().list(
        part="snippet", videoId=video_id, maxResults=100
    )
    response = request.execute()
    comments = extract_comment_details(response)
    return comments


def extract_comment_details(response):
    """
    The function `extract_comment_details` extracts relevant details from comments in an API response.

    :param response: The response parameter is the response received from the API call. It is expected
    to be in JSON format and contain information about comments
    :return: a list of lists, where each inner list contains the following details of a comment:
    - Comment text (textDisplay)
    - Author display name (authorDisplayName)
    - Published date and time (publishedAt)
    - Updated date and time (updatedAt)
    - Number of likes (likeCount)
    """
    comments = []
    for item in response.get("items", []):
        snippet = item.get("snippet", {}).get("topLevelComment", {}).get("snippet", {})
        comments.append(
            [
                snippet.get("textDisplay", ""),
                snippet.get("authorDisplayName", ""),
                snippet.get("publishedAt", ""),
                snippet.get("updatedAt", ""),
                snippet.get("likeCount", 0),
            ]
        )
    return comments


def create_comments_dataframe(comments):
    """
    The function `create_comments_dataframe` creates a Pandas DataFrame from a list of comments.

    :param comments: A list of dictionaries containing information about comments. Each dictionary
    should have the following keys:
    :return: a Pandas DataFrame that contains the comments data.
    """
    df = pd.DataFrame(
        comments,
        columns=["text", "author", "published_at", "updated_at", "like_count"],
    )
    return df


def fetch_comments_from_youtube_api(video_id):
    """
    The function fetch_comments_from_youtube_api fetches comments from the YouTube API for a given video
    ID and returns them as a dataframe.

    :param video_id: The video_id parameter is the unique identifier of the YouTube video for which you
    want to fetch the comments
    :return: a DataFrame object containing the comments fetched from the YouTube API.
    """
    youtube_client = build_youtube_client()
    comments = fetch_comments(youtube_client, video_id)
    comments_df = create_comments_dataframe(comments)
    return comments_df
