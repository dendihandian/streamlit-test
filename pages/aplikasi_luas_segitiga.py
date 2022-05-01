import streamlit as st

st.write("""
# Aplikasi Luas Segitiga
Ini adalah aplikasi menghitung segitiga
""")

alas = st.number_input("Masukan Alas", 8)
tinggi = st.number_input("Masukan Tinggi", 5)
hitung = st.button("Hitung Luas")

if (hitung):
    luas = 0.5 * alas * tinggi
    # st.write("luas segitiganya adalah ", luas)
    st.success(f"luas segitiganya adalah {luas}")
    st.balloons()

"""
streamlit run aplikasi_luas_segitiga.py
"""