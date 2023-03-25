from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Page config
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Load assets
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_7X0d6AzODk.json")

img_contact_form = Image.open("images/clock.png")
img_lottie_animation = Image.open("images/bmi1.png")


# Header section
with st.container():
    st.subheader("Hi, I am Max :wave:")
    st.title("A Python Developer")
    st.write("I am passionate about finding ways to use Python")
    st.write("[Learn More>](https://python.org)")

# What i do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            In the search to extend my knowledge of Python I always try to keep something good and discover some use or library that I don't know.
For example Streamlit, with which I have made this page.  
Other libraries of interest:
- Kivy MD
- Tkinter
- Pygame
- And many more...
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

# Projects section
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it.
            """
        )
        st.markdown("[Watch video...](https://youtu.be/TXSOitGoINE)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit website")
        st.write(
            """
            Want to add a contact form to your Streamli website?
            In this video, I'm going to show you how to implement a contact form in you streamlit app using the free service form.
            """
        )

# Contact
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/jmaxbarroso@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()