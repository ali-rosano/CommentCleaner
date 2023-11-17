import streamlit as st
import pandas as pd
import os
from controllers.youtube_api import extract_comments_and_languages

st.title("Insert a youtube video link")
video_link = st.text_input("video_link", label_visibility="hidden")
if st.button("Send"):
    os.system("cls")
    print(video_link)

    df = extract_comments_and_languages(video_link)
    st.title(video_link)
    columns_to_show = ["text", "Detected_Language"]
    st.dataframe(df[columns_to_show])
