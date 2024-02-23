import streamlit as st
import time
st.set_page_config(page_title="Page 2", page_icon="🚀")

st.title("Ligation Calculator")
with st.form(key='ligation_calculator'):
    vect_size = st.number_input('Vector size in bp',value=None, format="%.0f",placeholder="Type vector size")
    vect_amt = st.number_input('Vector amount in ng',value=None, format="%.1f", placeholder="Type vector amount")
    insert_size = st.number_input('Insert size in bp',value=None, format="%.0f",placeholder="Type insert size")
    vect_ratio = st.selectbox("Vector : insert ratio", options=["1:1","1:2","1:3","1:4","1:5","1:7"],key="kvect_ratio")
    
    #b = st.number_input('b')
    submit = st.form_submit_button('Calculate amount of insert')
    container = st.container(border=True)
    container.write("Required insert amount in ng")
    if submit:
        if ((vect_size !=None and vect_size>0 ) and (vect_amt!=None and vect_amt>0) & (insert_size !=None and insert_size>0 )):
            submit_toast=st.toast("Calculation done")
            container.metric(label="",value=round(((vect_amt/(vect_size/insert_size))*int(vect_ratio.split(":")[1])),1))#the vect_ratio.split(":")[1] allows to get the number of insert from the selection menu to use for multiplication
        else:
            error_message=container.error("Please fill all required fields", icon="🚨")


  #use ast.literal_eval to convert 1:3 to an operation