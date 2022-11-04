#Streamlit

import streamlit as st
import PyPDF2 
import pdf2image
from PIL import Image
import easyocr as ocr
import numpy as np
from pathlib import Path

valid = 0
not_valid = 0

st.sidebar.title("PDF Filter")
uploaded_files = st.sidebar.file_uploader(label="Upload PDF file(s):", type=['pdf'], accept_multiple_files=True)

def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model()

st.title("Documents:")

def run():
    for i in range(len(uploaded_files)):
        
        input_pdf = uploaded_files[i]
        pdfReader = PyPDF2.PdfFileReader(input_pdf)
        pageObj = pdfReader.getPage(0) 
        PDF_text = pageObj.extractText()
        if "ACORD 25" not in PDF_text:
            if len(PDF_text) == 0:
                try:
                    pil_image = pdf2image.convert_from_path(Path(input_pdf.name), poppler_path="https://github.com/pc3541/PDF-Filter/tree/main/bin")
                    result = reader.readtext(np.array(pil_image))
                    result_text = []
                    for text in result:
                        result_text.append(text[1])
                    final_text = " ".join([str(x) for x in result_text])
                    if "ACORD 25" not in final_text:
                        st.write(input_pdf.name, "**(bogus)**")
                    else:
                        st.write(input_pdf.name, "(valid)")
                except:
                    st.write("**Error analyzing **", input_pdf.name)
            else:
                st.write(input_pdf.name, "**(bogus)**")
        else:
            st.write(input_pdf.name, "(valid)")
    
if st.sidebar.button("Run filtering"):
    run()
