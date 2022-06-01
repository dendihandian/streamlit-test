import tensorflow as tf
import streamlit as st
st.set_page_config(layout="wide")

def tensorflow_test():
    st.title('Tensorflow Test', anchor=None)

    st.write("TensorFlow version: " + str(tf.__version__))