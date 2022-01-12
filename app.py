import streamlit as st 
from PIL import Image
import numpy as np
import cv2
import math


st.header("Image Details")
Img = st.file_uploader("Upload here", type=["png","jpg","jpeg"])    
if Img is None:
    st.text("Please upload an image")
else:
    image = Image.open(Img)
    image = np.array(image)
    def variance_of_laplacian(image):
        return cv2.Laplacian(image, cv2.CV_64F).var()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(image)
    text = "Not Blurry"
    if fm < 500:
        text = "Blurry"

    #Calculate image size in bytes
    bytes_data = Img.getvalue()
    file_bytes = len(bytes_data)

    UNITS_MAPPING = [
        (1<<50, ' PB'),
        (1<<40, ' TB'),
        (1<<30, ' GB'),
        (1<<20, ' MB'),
        (1<<10, ' KB'),
        (1, (' byte', ' bytes')),
    ]


    def pretty_size(bytes, units=UNITS_MAPPING):
        for factor, suffix in units:
            if bytes >= factor:
                break
        amount = int(bytes / factor)

        if isinstance(suffix, tuple):
            singular, multiple = suffix
            if amount == 1:
                suffix = singular
            else:
                suffix = multiple
        return str(amount) + suffix

    def dpi(width_p,height_p):
        d = (width_p*width_p)+(height_p*height_p)
        diagonal_p = math.sqrt(d)
        diagonal_inch = diagonal_p*0.0104166667 
        ppi = diagonal_p//diagonal_inch
        ppi = format(ppi, '.0f') #to print only integer value
        return(ppi)
    img_rez = Image.open(Img)

    #extracting image height and width
    width, height = img_rez.size
    width_cm = (width/96)*2.54
    height_cm = (height/96)*2.54 

    #converting Image pixesls into cm
    st.image(Img)
    st.text("Image Details")
    st.text("------------------------------------------------------")
    st.write("1. Image Format : ",img_rez.format)
    st.write("2. Image Dimensions : ",width,"X",height,"Pixels")
    st.write("3. Width : {} cm".format(round(width_cm,2))," &  "," Height : {} cm".format(round(height_cm,2)))
    st.write("4. Image Size : ",pretty_size(file_bytes))
    st.write("5. Image Resolution : ",dpi(width,height),"dpi")
    st.write("6. Status : ",text)




