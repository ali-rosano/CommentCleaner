import streamlit as st
from PIL import Image

#text style
st.markdown('<h1 style="color: blue; font-size: 36px;">Comment Cleaner</h1>', unsafe_allow_html=True)

st.title("EDA")



st.header('Comments in each category', divider='rainbow')
st.image(Image.open('Images/Comment_category.png'))



st.header('Number of comments having multiple labels', divider='rainbow')
st.image(Image.open('Images/Multi_toxic.png'))



st.header('Investigate targeted variable - Feature Distribution', divider='rainbow')
st.image(Image.open('Images/distribution.png'))



st.header('WordCloud', divider='rainbow')

st.subheader('Word cloud is a text visualization tool that help’s us to get insights into the most frequent words present in the corpus of the data.', divider='rainbow')
st.image(Image.open('Images/WordCloud.png'))

