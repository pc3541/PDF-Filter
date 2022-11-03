import streamlit as st
import PyPDF2 
import tesserocr
from pdf2image import convert_from_path
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

valid = 0
not_valid = 0

st.sidebar.title("PDF Filter")
input_pdf = st.sidebar.file_uploader("Upload PDF file(s):", type=['pdf'])

def run():
  pdfReader = PyPDF2.PdfFileReader(input_pdf)
  pageObj = pdfReader.getPage(0) 
  PDF_text = pageObj.extractText()
  if "ACORD 25" not in PDF_text:
      if len(PDF_text) == 0:
          pil_image_lst = convert_from_path(f, 500)
          image = pil_image_lst[0]
          api = tesserocr.PyTessBaseAPI()
          api.SetImage(image)
          text = api.GetUTF8Text()
          if "ACORD 25" not in text:
              print(filename)
              not_valid += 1
          else:
              valid += 1
      else:
          print(filename)
          not_valid += 1
  else:
      valid += 1
  st.write("")
  st.write("Valid:",valid)
  st.write("Not valid", not_valid)

if st.sidebar.button("Run filtering"):
    run()
