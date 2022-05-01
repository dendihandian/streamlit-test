import streamlit as st
st.set_page_config(layout="wide")

import sys
import pkg_resources


installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])


def main_page():
    st.title('Streamlit Test', anchor=None)

    st.write('Environment Information')
    st.table([
        ['Python version',sys.version], 
        ['Streamlit version', st.__version__], 
    ])

    st.write('Installed Packages')
    st.table(installed_packages_list)