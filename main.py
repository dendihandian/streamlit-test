import streamlit as st
from pages.main_page import main_page
from pages.tensorflow_test import tensorflow_test

selected_page = st.sidebar.selectbox(
    "Select page",   
    (
        "Main Page",
        "TensorFlow Test",
        "About"
    ),
    key=0
)


if selected_page == 'Main Page':
    main_page()
elif selected_page == 'TensorFlow Test':
    tensorflow_test()
else:
    st.write(1)