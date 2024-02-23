import streamlit as st
import time
st.set_page_config(page_title="Page 2", page_icon="🚀")

st.title("Ligation Calculator")
with st.form(key='ligation_calculator'):
    vect_size = st.number_input('Vector size in bp',value=None, format="%.1f",placeholder="Type vector size")
    vect_amt = st.number_input('Vector amount in ng',value=None, format="%.1f", placeholder="Type vector amount")
    insert_size = st.number_input('Insert size in bp',value=None, format="%.1f",placeholder="Type insert size")
    vect_ratio = st.selectbox("Vector:insert ratio", options=["1:1","1:2","1:3","1:4","1:5","1:7"],key="kvect_ratio")
    
    #b = st.number_input('b')
    submit = st.form_submit_button('Calculate')
    if submit:
        submit_toast=st.toast("Thanks")

  