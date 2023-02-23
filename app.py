import streamlit as st
from PIL import Image
from io import BytesIO
import base64
import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = '5ad134ea87d40839823c345cb48b5eb211890d58'

model = replicate.models.get("yuval-alaluf/sam")
version = model.versions.get("9222a21c181b707209ef12b5e0d7e94c994b58f01c7b2fec075d2e892362f13c")

st.set_page_config(layout="wide", page_title="Age Progression")
st.write("# AgeGenie")
st.success("This is so cool! Want to see how you'll look at 70?")
menu = ["About", "Input image"]
choice = st.sidebar.selectbox("What would you like to do?", menu)
if choice == 'About':
    st.write("This is an app for face aging. It takes a photo of a person as input and generates a modified version of the photo that shows the person's face at an older age.")
else:
    st.sidebar.write("## Upload and download :gear:")
    def convert_image(img):
        st.image(img, caption='Aged Image', use_column_width=True)
        st.sidebar.download_button("Download Aged Image", img, "aged_image.png", "image/png")

    # def convert_image(img):
    #     img_bytes = BytesIO()
    #     img.save(img_bytes, format='PNG')
    #     img_bytes.seek(0)
    # #     st.image(img, caption='Aged Image', use_column_width=True)
    #     st.sidebar.download_button("Download Aged Image", img_bytes.getvalue(), "aged_image.png", "image/png")

    def fix_image(upload):
        image = Image.open(upload)
        col1.write("Original Image :👦🏾")
        col1.image(image)

        col2.write("Aged image :👴🏾:")

    my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    col1, col2 = st.columns(2)
    inputs = {
    # facial image
    'image': my_upload,

    # age of the output image
    'target_age': st.sidebar.slider("Select an age", 0,100),
    }
    if my_upload is not None:
        with col1:
            fix_image(upload=my_upload)

        with col2:
            output = version.predict(**inputs)
            # result = st.image(output)
            convert_image(output)

    else:
        st.warning("Please Upload an Image")

