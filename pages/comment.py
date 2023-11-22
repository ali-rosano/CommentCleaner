import streamlit as st

import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
from controllers.vectorizer import vectorize_comment

model = tf.keras.models.load_model("model/hate_speech2.h5")

max_tokens = 100000
output_sequence_length = 1800

vectorizer = TextVectorization(
    max_tokens=max_tokens,
    output_sequence_length=output_sequence_length,
    output_mode="int",
)

example_comment = "i hate you black bitch"
comments = [example_comment]
vectorizer.adapt(comments)


def predict_toxicity(comment):
    comment = [comment]
    preprocessed_comment = vectorizer(comment)
    predictions = model.predict(preprocessed_comment)
    return predictions[0][0]


st.title("Hate Speech Detector")

comment_input = st.text_area("Enter your comment here:")
if st.button("Predict"):
    if comment_input:
        toxicity_prediction = predict_toxicity(comment_input)
        if toxicity_prediction >= 0.5:
            st.error("The comment contains hate speech.")
        else:
            st.success("The comment does NOT contain hate speech.")
    else:
        st.warning("Please enter a comment to make a prediction.")

