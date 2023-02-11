import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title = "Projects and Assignments", page_icon = ":mortar_board:", layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Assets
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_whatsapp = Image.open("images/pngtree-whatsapp-icon-png-image_6315990.png")
img_instagram = Image.open("images/pngtree-instagram-icon-png-image_6315974.png")
img_telegram = Image.open("images/telegram-logo-4.png")
img_gmail = Image.open("images/google-gmail-logo-620D76A63C-seeklogo.com.png")

# Header
with st.container():
    st.subheader("Hi, I am Kiran :wave:")
    st.title("All types of Projects and Assignments")
    st.write("We have a great team with all experienced in thier respective fields. We provide help in all type of projects and Assignments.")

with st.container():
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("What we provide")
        st.write("##")
        st.write("""
                We help students and individuals around the world in:
                - Projects based on all Programming Languages.
                - University Projects.
                - Assignments, Quiz and Courses.
                - Creative Writing, Certifications.
                - Python Language Tutoring.
                - Exams based on Education, Placements, etc.
                
                If you need help in any of these, just contact us.
                """)

    with right_col:
        st_lottie(lottie_coding,width= 300,height = 400, key="coding")
    
with st.container():
    st.header("Contact Details")
    st.write("##")
    image_col_1,text_col_1 = st.columns((1,30))
    with image_col_1:
        st.image(img_whatsapp, width= 40)
    with text_col_1:
        st.write("[click here >](https://wa.me/+917981121028)")
    image_col_2,text_col_2 = st.columns((1,30))
    with image_col_2:
        st.image(img_instagram, width= 40)
    with text_col_2:
        st.write("[click here >](https://instagram.com/kiran_naidu_pspk?igshid=YzgyMTM2MGM=)")
    image_col_3,text_col_3 = st.columns((1,30))
    with image_col_3:
        st.image(img_telegram, width= 40)
    with text_col_3:
        st.write("[click here >](https://t.me/KiranKatakamsetti)")
    image_col_4,text_col_4 = st.columns((1,30))
    with image_col_4:
        st.image(img_gmail, width= 40)
    with text_col_4:
        st.write("kirankatakamsetti@gmail.com")