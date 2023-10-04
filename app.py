
import requests
import streamlit as st
# from streamlit_option_menu import option_menu

import pandas as pd
import numpy as np



from streamlit_lottie import st_lottie

from PIL import Image



#configuration



st.set_page_config(page_title= "SetMyCitasApp", page_icon="💈", layout="wide" )

url = "https://d1jj76g3lut4fe.cloudfront.net/saved_colors/76951/qvjIxEl6UiFxHDOD.json"

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = load_lottie(url)

# Css file 

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        

local_css("style/main.css")
email_address = "3d60creations@gmail.com"   

 
#Top Bar

with st.container():
    def streamlit_menu(example=1):
        if example == 1:
        # 1. as sidebar menu
            with st.sidebar:
                selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Projects", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

with st.container():
    st.image("images/topBar.jpg")

#intro page
with st.container():
    st.header("WELCOME TO SET CITAS APP💈", divider='rainbow')
    st.title("Our commitment to our clients is: ")
    st.write("Our unwavering commitment to our clients is the driving force behind all that we do. We are constantly pushing ourselves to go above and beyond, to provide them with unparalleled service and support. It is our honor and privilege to serve our clients with dedication, passion, and excellence.")

    st.write("[For More info >](https://setcitasapp.com/home)")

# about us

with st.container():
    st.header("About", divider='rainbow')
    st.title("")
    st.write("Do magna in eiusmod duis cillum velit pariatur enim enim ipsum consectetur aute duis. Non est velit et do eu enim. Est sit nulla sunt excepteur duis elit. Cillum laboris nulla ea excepteur nulla tempor sint nisi Lorem ad veniam. Qui duis duis excepteur cillum ipsum minim in qui reprehenderit.")

    st.write("[For More info >](https://setcitasapp.com/aboutus)")


#our team    
with st.container():
    
    st.header("Our Team 💈", divider='rainbow')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("Juan")
        st.image("https://images.unsplash.com/photo-1553521041-d168abd31de3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGJhcmJlcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=400&q=60")   
    

    with col2:
        st.header("Rodney")
        st.image("https://images.unsplash.com/photo-1553521041-d168abd31de3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGJhcmJlcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=400&q=60")

    with col3:
        st.header("Roger")
        st.image("https://images.unsplash.com/photo-1553521041-d168abd31de3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGJhcmJlcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=400&q=60")



 # editing column-1
    with col1:
        st.header("Juan")
        st.image('https://images.unsplash.com/photo-1553521041-d168abd31de3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGJhcmJlcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=400&q=60')
# editing column-2
    with col2:
        st.header("Juan")   
        st.image('https://images.unsplash.com/photo-1553521041-d168abd31de3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGJhcmJlcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=400&q=60')
# editing column-3    
    with col3:
        st.header("Juan")
        st.image('https://images.unsplash.com/photo-1553521041-d168abd31de3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGJhcmJlcnxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=400&q=60')       

st.write("[For More info >](https://setcitasapp.com/team)")


#our team    
with st.container():
        st.header("Registration Form", divider='rainbow')
        col1, col2 = st.columns(2)
        with col1: 
         
          
# creating a form
         my_form=st.form(key='form-1')
# creating input fields
        fname=my_form.text_input('First Name:')
        lname=my_form.text_input('Last Name:')
        email=my_form.text_input('Email:')
# creating radio button 
        gender=my_form.radio('Gender',('Male','Female'))
# creating slider 
        age=my_form.slider('Age:',1,120)
# creating date picker
        bday=my_form.date_input('Enter Birthdate:')
# creating a text area
        address=my_form.text_area('Enter Address:')
# creating a submit button
        submit=my_form.form_submit_button('Submit')
# the following gets updated after clicking on submit, printing the details of the fields that are submitted in the form
        st.write('Name is '+fname+' '+lname)
        st.write('Email is '+email)
        st.write('Gender is '+gender)
        st.write('Age is '+str(age))
        st.write('Birthday is '+str(bday))
        st.write('Address is '+address)

with col2:

    # with st.echo():
        st_lottie("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
       

# You can add more features and
        st.write("[For More info >](https://setcitasapp.com/setappointment)")

with st.container():
    st.header("Connect with us 📬", divider='rainbow')
    st.title("")
    st.write("")

    st.write("[For More info >](https://setcitasapp.com/social)")







    
        