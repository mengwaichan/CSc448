##############################################################################################################
# Filename: app.py
#
# Description: A Streamlit application to test our performance of the model(s),
#
# Copyright © 2023 by TESSA
##############################################################################################################
import joblib
import nltk  # Natural Language Processing.
import numpy as np  # Data wrangling.
import pandas as pd  # Data handling.
import re  # Regular expression operations.
import streamlit as st  # Streamlit.

from nltk.stem import (
    WordNetLemmatizer,
)  # Lemmatize using WordNet's built-in morphy function.
from nltk.stem import (
    PorterStemmer,
)  # Remove morphological affixes from words, leaving only the word stem.
from nltk.corpus import stopwords  # Remove stopwaords.
from nltk import word_tokenize  # Tokenize.
from nltk.corpus import wordnet
from tensorflow.keras.models import load_model  # To load the model.
from tensorflow.keras.preprocessing.sequence import (
    pad_sequences,
)  # Transformsa list of sequences into a 2D Numpy array.

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
##############################################################################################################
tokenizer = joblib.load(open("./tokenizer/tokenizer.pickle", "rb"))
label = joblib.load(open("./label_encoder/label_encoder.h5", "rb"))
model = load_model("./neural_network_models/cnn_model.h5")
##############################################################################################################
emotions_emoji_dict = {
    "anger": "😠",
    "fear": "😨",
    "joy": "😂",
    "love": "😍",
    "sadness": "😞",
    "surprise": "😯",
}
##############################################################################################################
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
##############################################################################################################

# Cleaner class is responsible for cleaning the documents using its pipeline function.


class Cleaner:
    def __init__(self):
        pass

    # 1. Make a function that makes all text lowercase.

    def make_lowercase(self, input_string):
        input_string = input_string.split()
        input_string = [y.lower() for y in input_string]
        return " ".join(input_string)

    # 2. Make a function that removes all stopwords.

    def remove_stopwords(self, input_string):
        input_string = [i for i in str(input_string).split() if i not in stop_words]
        return " ".join(input_string)

    # 3. Make a function that removes all numbers.

    def remove_numbers(self, input_string):
        input_string = "".join([i for i in input_string if not i.isdigit()])
        return input_string

    # 4. Make a function that removes all punctuation.

    def remove_punctuation(self, input_string):
        input_string = re.sub(
            "[%s]" % re.escape("""!"#$%&'()*+,،-./:;<=>؟?@[\]^_`{|}~"""),
            " ",
            input_string,
        )
        input_string = input_string.replace(
            "؛",
            "",
        )
        input_string = re.sub("\s+", " ", input_string)
        input_string = " ".join(input_string.split())
        return input_string.strip()

    # 5. Make a function that removes all urls.

    def remove_urls(self, input_string):
        url_pattern = re.compile(r"https?://\S+|www\.\S+")
        return url_pattern.sub(r"", input_string)

    # 6. Make a function for lemmatization.

    def lemmatization(self, input_string):
        lemmatizer = WordNetLemmatizer()
        input_string = input_string.split()
        input_string = [lemmatizer.lemmatize(y) for y in input_string]
        return " ".join(input_string)

    # 7. Make a function that breaks words into their stem words.

    def stem_words(self, input_string):
        porter = PorterStemmer()
        words = word_tokenize(input_string)
        valid_words = []

        for word in words:
            stemmed_word = porter.stem(word)
            valid_words.append(stemmed_word)

        input_string = " ".join(valid_words)

        return input_string

    # 8. Make a pipeline function that applies all the text processing functions you just built.

    def pipeline(self, input_string):
        input_string = self.make_lowercase(input_string)  # 1.
        input_string = self.remove_stopwords(input_string)  # 2.
        input_string = self.remove_numbers(input_string)  # 3.
        input_string = self.remove_punctuation(input_string)  # 4.
        input_string = self.remove_urls(input_string)  # 5.
        input_string = self.lemmatization(input_string)  # 6.
        # input_string = self.stem_words(input_string) # 7.
        return input_string


##############################################################################################################

# Inference function for new user input.


def cnn_inference(user_input):
    # Create an instance of the Cleaner class.

    cleaner = Cleaner()

    # Call the pipeline function on the new user input.

    cleaned_user_input = cleaner.pipeline(user_input)

    # Convert cleaned_user_input into a sequence of integers.

    cleaned_user_input = tokenizer.texts_to_sequences([cleaned_user_input])

    # Pad the sequences to a length of 256.

    cleaned_user_input = pad_sequences(cleaned_user_input, maxlen=256, truncating="pre")

    model_output = model.predict([cleaned_user_input, cleaned_user_input])

    # Model predicts the predicted emotion for the cleaned_user_input.

    output = label.inverse_transform(np.argmax(model_output, axis=-1))[0]

    # Calculate the probability of the predicted result.

    probability = np.max(model_output)

    return output, probability


##############################################################################################################
# Function to apply local CSS.
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


##############################################################################################################
# Main function to create the Streamlit web application.


def main():
    try:
        st.set_page_config(page_title="TESSA | 😠😨😂😍😞😯")

        # Load CSS.
        local_css("styles/style.css")

        # Title.
        title = f"""<h1 align="center" style="font-family: monospace; font-size: 2.1rem; margin-top: -6rem">
                    Text Emotion System Sentiment Analysis</h1>"""
        st.markdown(title, unsafe_allow_html=True)

        # Subtitle.
        title = f"""<h2 align="center" style="font-family: monospace; font-size: 2.3rem; margin-top: -2rem">
                    TESSA</h2>"""
        st.markdown(title, unsafe_allow_html=True)

        # Image.
        image = "./logo.png"
        st.image(image)

        # Margin between the image and the form.
        st.markdown(
            f'<p style="margin-top: 5rem; text-align: center;"></p>',
            unsafe_allow_html=True,
        )

        with st.form(key="my_form", border=True):
            st.markdown(
                "<style>label, .stTextInput { color: red; }</style>",
                unsafe_allow_html=True,
            )
            user_input = st.text_area("Type Here")
            submit_text = st.form_submit_button(label="Classify")

        if submit_text:
            prediction, probability = cnn_inference(user_input=user_input)
            st.success("Prediction Found Below!")
            emoji_icon = emotions_emoji_dict[prediction]

            st.markdown(
                f'<p style="text-align: center;">Predicted Emotion = {prediction.capitalize()}{emoji_icon}</p>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f'<p style="text-align: center;">Confidence = {np.max(probability)}</p>',
                unsafe_allow_html=True,
            )

    except Exception as e:
        st.error(e)


if __name__ == "__main__":
    main()
