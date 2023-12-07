import streamlit as st
from PIL import Image
from rembg import remove as rembg_remove
import base64
import io

# Function to generate styled download link
def get_styled_binary_file_downloader_html(bin_file, file_label='File', button_text='Download Image'):
    b64 = base64.b64encode(bin_file.read()).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="output.png" style="text-decoration: none; padding: 10px; color: #ffffff; background-color: #4CAF50; border-radius: 5px; border: 2px solid #45a049; cursor: pointer;">{button_text}</a>'

# Centered layout using st.write
st.title("Background Remover")
st.write("This app removes the background from images and allows you to support the creator with an Ethereum donation.")
st.write("Author: *Lothar Tjipueja*")


# Image upload section
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display uploaded image
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

    # Remove background button
    if st.button("Remove Background"):
        # Perform background removal using rembg library
        with io.BytesIO() as buf:
            buf.write(uploaded_image.read())
            buf.seek(0)

            # Apply background removal
            input_image = Image.open(buf)
            output_image = rembg_remove(input_image)

        st.success("Background removed successfully!")

        # Save output image
        output_buf = io.BytesIO()
        output_image.save(output_buf, format="PNG")
        st.image(output_buf, caption="Image with Background Removed.", use_column_width=True)

        # Allow user to download the output image with a styled button
        st.markdown(get_styled_binary_file_downloader_html(output_buf, 'Download Image'), unsafe_allow_html=True)

# Ethereum donation section
st.subheader("Support the Creator with an Ethereum Donation")

# Ethereum donation address (replace with your own Ethereum address)
ethereum_address = "0x3cA9046B349c7f1C49e65304aA257BC67dCa05a5"

# Display Ethereum address
st.write(f"Ethereum Address: {ethereum_address}")

# Donate with Ethereum button
if st.button("Donate with Ethereum"):
    st.write("Please send your donation to the provided Ethereum address. Thank you for your support!")
