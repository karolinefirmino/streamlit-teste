# Modules
import pyrebase
import streamlit as st
from datetime import datetime





# Configuration Key 
firebaseConfig = {
    'apiKey': "AIzaSyCo3oG_V66hnU67i6jU23v-bt76tOL4Sl4",
    'authDomain': "elm-firebase-streamlit.firebaseapp.com",
    'projectId': "elm-firebase-streamlit",
    'databaseURL':'https://elm-firebase-streamlit-default-rtdb.firebaseio.com/',
    'storageBucket': "elm-firebase-streamlit.appspot.com",
    'messagingSenderId': "50984170131",
    'appId': "1:50984170131:web:526b2c5604c4902a941366",
    'measurementId': "G-TE13WYC2WR"
}

# Firebase Authentication 
fb = pyrebase.initialize_app(firebaseConfig)
auth = fb.auth()


# Database
db = fb.database()
storage = fb.storage()

st.sidebar.title("Our community app")

# Authentication 

choice = st.sidebar.selectbox('Login/Signup', ['Login', 'Sign Up'])

email = st.sidebar.text_input('Please enter your email address')
password = st.sidebar.text_input('Please enter your password')


if choice == 'Sign Up':
    handle = st.sidebar.text_input('Please input your app handle name', value= 'Default')
    submit = st.sidebar.button('Create my account')

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account was created successfully!')

        # Sign in
        user = auth.sign_in_with_email_and_password(email, password, extra={'uid': '123'})
        db.child(user['localId'].child("Handle").set(handle))
        db.child(user['localId'].child("ID").set('localId'))
        st.title('Welcome' + handle)
        st.info('Login via login drop drown select')
