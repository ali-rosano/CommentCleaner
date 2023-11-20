import streamlit as st
import pandas as pd
import os
from controllers.comment_processor import extract_comments_and_languages

st.title("Insert a youtube video link")
video_link = st.text_input("video_link", label_visibility="hidden")
if st.button("Send"):
    df = extract_comments_and_languages(video_link)
    # TODO buscar y mostrar el titulo del video
    # st.title(video_link)
    columns_to_show = ["Translated_Text", "Hate_Label"]
    st.dataframe(df[columns_to_show])
