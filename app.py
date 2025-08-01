# app.py

import streamlit as st
import cv2
import numpy as np
from PIL import Image
from deepface import DeepFace

from morphing.emotion_morpher import morph_emotion
from morphing.age_morpher import morph_age

st.set_page_config(page_title="FaceMorph AI", layout="centered")

st.title("🎭 FaceMorph AI")
st.subheader("Real-Time Age & Emotion Morphing")

uploaded_file = st.file_uploader("Upload a face image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Convert to numpy
    img_np = np.array(image.convert("RGB"))

    with st.spinner("Analyzing..."):
        try:
            result = DeepFace.analyze(img_np, actions=['emotion', 'age'], enforce_detection=True)[0]
            emotion = result['dominant_emotion']
            age = result['age']

            st.success(f"Detected Emotion: **{emotion.capitalize()}** | Age: **{age}**")

            # Morphing
            morphed_img = morph_emotion(image, emotion)
            morphed_img = morph_age(morphed_img, age)

            st.image(morphed_img, caption="Morphed Image", use_column_width=True)

        except Exception as e:
            st.error(f"Error: {str(e)}")
