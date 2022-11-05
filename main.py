#Streamlit

import streamlit as st
import PyPDF2 
import fitz
from PIL import Image
import easyocr as ocr
import numpy as np
import io

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
        pdfReader = PyPDF2.PdfReader(input_pdf)
        for pg in range(len(pdfReader.pages)):
            pageObj = pdfReader.pages[pg]
            PDF_text = pageObj.extractText()
            if "ACORD 25" not in PDF_text:
                if len(PDF_text) == 0:
                    doc = fitz.open(input_pdf, filetype="pdf")
                    for page in doc:
                        pix = page.get_pixmap()
                        result = reader.readtext(np.array(pil_image))
                        result_text = []
                        for text in result:
                            result_text.append(text[1])
                        final_text = " ".join([str(x) for x in result_text])
                        if "ACORD 25" not in final_text:
                            st.write(input_pdf.name, " page ", page, " **(bogus)**")
                        else:
                            st.write(input_pdf.name, "(valid)")
                            continue
                else:
                    st.write(input_pdf.name, " page ", pg, " **(bogus)**")
            else:
                st.write(input_pdf.name, "(valid)")
                continue
    
if st.sidebar.button("Run filtering"):
    run()
