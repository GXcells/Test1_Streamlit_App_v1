import streamlit as st
import time

st.set_page_config(page_title="Molecular Calculator", page_icon="🚀")

st.title("Molecular calculator")
dict_unit={
    "MW":{"Daltons (g/mol)":1,"kDa":1000},
    "mass":{"g":1,"mg":10**-3,"µg":10**-6,"ng":10**-9,"pg":10**-12},
    "vol":{"L":1,"mL":10**-3,"µL":10**-6}}
mola_container=st.container(border=True)
container_da = mola_container.container(border=True)
dacol1,dacol2 = container_da.columns(2)
molec_da_inp = dacol1.number_input("Molecular weight",value=None, format="%.2f",step=0.01,placeholder="Enter molecular weight")
molec_da_sel = dacol2.selectbox("unit", options=["Daltons (g/mol)","kDa"],key="molec_unit")
#st.divider()
form_molarity=mola_container.form(key='molecular calculator', border=False)
mola_val=mola_container.empty()
mola_val.metric(label="Molarity Result",value=None,label_visibility="hidden")
error_message=mola_container.empty()
with form_molarity:
    
    mocol1,mocol2,mocol3,mocol4,mocol5 = st.columns(5)
    mo_weight_inp= mocol1.text_input("Weight input", "")
    mo_weight_sel= mocol2.selectbox("Weight unit",options=["g","mg","µg","ng","pg"],index=2)
    mo_weight_sep= mocol3.text("--    in   --")

    mo_vol_inp= mocol4.text_input("volume input", "")
    mo_vol_sel= mocol5.selectbox("volume unit",options=["L","mL","µL"],index=1)

    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    submit = st.form_submit_button('Calculate Molarity')

if submit:
    try:
        mola_val.metric(label="Molarity Result",value=round((int(mo_weight_inp)*dict_unit["mass"][mo_weight_sel]/(int(molec_da_inp)*dict_unit["MW"][molec_da_sel]))/(int(mo_vol_inp)*dict_unit["vol"][mo_vol_sel]),5),label_visibility="hidden")#the vect_ratio.split(":")[1] allows to get the number of insert from the selection menu to use for multiplication
    except:
        error_message.error("Please fill all required fields", icon="🚨")

        #if ((vect_size !=None and vect_size>0 ) and (vect_amt!=None and vect_amt>0) & (insert_size !=None and insert_size>0 )):
            #submit_toast=st.toast("Calculation done")
  #use ast.literal_eval to convert 1:3 to an operation+
def change_molarity():
    if mola_val.metric != None:
        try:
            mola_val.metric(label="",value=round((int(mo_weight_inp)*dict_unit["mass"][mo_weight_sel]/(int(molec_da_inp)*dict_unit["MW"][molec_da_sel]))/(int(mo_vol_inp)*dict_unit["vol"][mo_vol_sel]),5), label_visibility="hidden")
        except:
            error_message.error("Please fill all required fields", icon="🚨")
    else:
        pass
    


mo_res_title= st.text("Concentration")
mo_res_sel= st.selectbox("concentration unit",options=["M","mM","µM","nM","pM"],index=2, on_change =change_molarity())