import streamlit as st
from PIL import Image
from io import BytesIO
import base64
import replicate
import os

st.set_page_config(layout="wide", page_title="Age Progression")
st.write("# Age Progression")

st.sidebar.write("## Upload and download :gear:")


# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = image
    col2.write("Aged image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image(r"face-aging-caae\data\UTKFace\1_0_0_20161219140623097.jpg.chip.jpg")

os.environ["REPLICATE_API_TOKEN"] = '6e020aa7780cda0b711d75de41356b5ac4703f0d'


model = replicate.models.get("yuval-alaluf/sam")
version = model.versions.get("9222a21c181b707209ef12b5e0d7e94c994b58f01c7b2fec075d2e892362f13c")

inputs = {
    # facial image
    'image': my_upload,

    # age of the output image

    'target_age': st.slider("Select an age", 0,100),
}
output = version.predict(**inputs)
st.image(output)

