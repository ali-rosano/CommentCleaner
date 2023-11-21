import streamlit as st
from PIL import Image


def app():

    #banner
    st.image(Image.open('Images/socialmedia-banner.jpeg'), width=1380)
    

    #text style
    st.markdown('<h1 style="color: blue; font-size: 36px;">Comment Cleaner</h1>', unsafe_allow_html=True)

    st.title("Comment cleaner")
    st.write("""""
    ###Transformando la Experiencia de YouTube: De la Toxicidad a la Positividad

    **Abordaremos el creciente problema de mensajes de odio en YouTube con una solución NLP innovadora y práctica**
             
    """)

    #place videos in paralel
    col1, col2 = st.beta_columns(2)

    video_file1 = open('Images/pexels-mart-production-7279746 (2160p).mp4', 'rb')
    video_bytes1 = video_file1.read()
    col1.video(video_bytes1)


    video_file2 = open('Images/pexels-darina-belonogova-7971669 (1080p).mp4', 'rb')
    video_bytes2 = video_file2.read()
    col2.video(video_bytes2)



if __name__ == "__main__":
    app()
