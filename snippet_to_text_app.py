# trunc8 did this
from io import StringIO
from PIL import Image
import streamlit as st
import pytesseract

st.write("""
         # Image Snippet to Text
         """
         )

st.write("This is a simple web app to read image snippets as continuous text")
file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

if file is None:
    st.text("Please upload an image file")
else:
    # Perform OCR using tesseract
    image = Image.open(file)
    st.image(image, use_column_width=True)
    text = pytesseract.image_to_string(image, lang="eng")

    # Post-processing to form paragraphs of continuous text
    processed_text = "" # Empty string
    for line in StringIO(text):
      if line != "\n":
        line = line.rstrip('\n')
        if line[-1] != "-":
          line += " "
      else:
        line += "\n"
      processed_text += line

    st.write(processed_text)















