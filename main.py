import streamlit as st
import easyocr as ocr  #OCR

reader = ocr.Reader(['en'],model_storage_directory='.')

result = reader.readtext("https://raw.githubusercontent.com/pc3541/PDF-Filter/main/outliers.jpeg")

for text in result:
    st.write(text[1])
