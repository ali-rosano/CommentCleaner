import streamlit as st
import os

os.system("cls")
st.title("Insert a comment")
comment = st.text_input("comment", label_visibility="hidden")
if st.button("Send comment"):
    print(comment)
    # os.system("cls")

    #
    # with open("model.pkl", "rb") as model_file:
    #     model = pickle.load(model_file)

    # with open("preprocessor.pkl", "rb") as preprocessor_file:
    #     preprocessor = pickle.load(preprocessor_file)
    #

    # X_comment_preprocessed = preprocessor.transform(comment)
    # predictions = model.predict(X_comment_preprocessed)
    X_comment_preprocessed = "este es el texto sin procesar"
    predictions = "nunca tiene hate"
    st.info(f"We have found that your comment contains: {predictions}")
