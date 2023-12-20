##############################################################################################################
# Filename: app.py
#
# Description: A Streamlit application to test our performance of the model(s),
#
# Copyright © 2023 by TESSA
##############################################################################################################
import streamlit as st
import numpy as np

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
            raw_text = st.text_area("Type Here")
            submit_text = st.form_submit_button(label="Classify")
    except Exception as e:
        st.error(e)


if __name__ == "__main__":
    main()
