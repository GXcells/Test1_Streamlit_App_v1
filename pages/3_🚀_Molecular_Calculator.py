import streamlit as st
import time

st.set_page_config(page_title="Molecular Calculator", page_icon="🚀")

st.title("Molecular calculator")

with st.form(key='molecular calculator'):
    container_da = st.container(border=True)
    dacol1,dacol2 = container_da.columns(2)
    molec_da_inp = dacol1.number_input("Molecular weight",value=None, format="%.2f",step=0.01,placeholder="Enter molecular weight")
    molec_da_sel = dacol2.selectbox("unit", options=["Daltons (g/mol)","kDa"],key="molec_unit")
    st.divider()
    container_mo = st.container(border=True)
    mocol1,mocol2,mocol3,mocol4,mocol5 = container_mo.columns(5)
    mo_weight_inp= mocol1.text_input("Weight input", "")
    mo_weight_sel= mocol2.selectbox("Weight unit",options=["g","mg","µg","ng","pg"],index=2)
    mo_weight_sep= mocol3.text("--    in   --")
    mo_vol_inp= mocol4.text_input("volume input", "")
    
    mo_vol_sel= mocol5.selectbox("volume unit",options=["L","mL","µL"],index=1)
    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    mo_res_title= mocol3.text("Concentration")
    mo_res_sel= mocol5.selectbox("concentration unit",options=["M","mM","µM","nM","pM"],index=2)

    vect_size = st.number_input('Vector size in bp',value=None, step=1,placeholder="Type vector size")
    vect_amt = st.number_input('Vector amount in ng',value=None, format="%.1f",step=0.1, placeholder="Type vector amount")
    insert_size = st.number_input('Insert size in bp',value=None, step=1,placeholder="Type insert size")
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


  #use ast.literal_eval to convert 1:3 to an operation+
