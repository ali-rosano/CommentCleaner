import re


def extract_id(link):
    """
    The function `extract_id` takes a YouTube video link as input and returns the video ID if found,
    otherwise it returns None.

    :param link: The link parameter is a string that represents a YouTube video link
    :return: the YouTube video ID extracted from the given link.
    """
    pattern = r"(?:^|\W)(?:youtube(?:-nocookie)?\.com/(?:.*[?&]v=|v/|e(?:mbed)?/|[^/]+/.+/)|youtu\.be/)([\w-]+)"
    matches = re.search(pattern, link)
    if matches:
        return matches.group(1)
    else:
        return None
