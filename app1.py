import streamlit as st

st.title("Belajar Python")
st.write("Penambahan")

value_a = st.number_input("Angka Pertama", step=1)
value_b = st.number_input("Angka Kedua", step=1)

submit_btn = st.button(label="Tambahkan")

if submit_btn:
    st.write(f"Total jumlahnya: {value_a + value_b}")
