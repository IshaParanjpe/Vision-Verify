import streamlit as st
from prediction import predict_result
import imageio.v3 as iio
from PIL import Image
import random
import os


st.title("Image Forgery Detection")

file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if file is None:
    if st.button("Use Sample Image"):
        sample = random.choice(os.listdir('examples'))
        sample_file = open(f"examples/{sample}", "rb")
        img = iio.imread(sample_file)
        image = Image.fromarray(img)
        original = "Authentic" if sample.startswith("A") else "Forged"
        st.write(f"Original: {original}") 
        predicted, confidence = predict_result(image) 
        st.write(f"Predicted: {predicted} with {confidence}% confidence")
        st.image(f"examples/{sample}", use_column_width=True)

else:
    img = iio.imread(file)
    image = Image.fromarray(img)

    if st.button("Predict"):

        predicted, confidence = predict_result(image) 
        st.write(f"Predicted: {predicted} with confidence {confidence}")
        st.image(image, use_column_width=True)
