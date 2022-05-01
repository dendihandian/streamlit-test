import streamlit as st
from pages.main_page import main_page

selected_page = st.sidebar.selectbox(
    "Select page",   
    (
        "Main Page",
        "About"
    ),
    key=0
)


if selected_page == 'Main Page':
    main_page()
else:
    st.write(1)