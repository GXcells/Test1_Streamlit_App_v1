############
#############  I HAVE TO MODIFY CALCULATION SO THAT IT USES FLOAT INSTEAD OF INTEGERS OTHERWISE I CANNOT INPUT A VOLUME OR WEIGHT WITH A DECIMAL

import streamlit as st
import time

st.set_page_config(page_title="Molecular CalculatorTEST", page_icon="🚀")
st.title("Molecular calculator")

#   ~dictionnary to hold data for calculation
dict_unit={
    "MW":{"Daltons (g/mol)":1,"kDa":1000},
    "mass":{"g":1,"mg":10**-3,"µg":10**-6,"ng":10**-9,"pg":10**-12},
    "vol":{"L":1,"mL":10**-3,"µL":10**-6},
    "molarity_unit":{"M":1,"mM":10**3,"µM":10**6,"nM":10**9,"pM":10**12}}


#   ~ define all my session_states
if "k_mol_sel" not in st.session_state:
    st.session_state["k_mol_sel"]="M"
if "molarity_result" not in st.session_state:
    st.session_state["molarity_result"]=""

#   ~ MAIN CONTAINER OF MOLARITY CALCULATOR
mola_container=st.container(border=True)

#   ~ Container for the MOLECULAR WEIGHT part
container_da = mola_container.container(border=True)
dacol1,dacol2 = container_da.columns(2)
molec_da_inp = dacol1.number_input("Molecular weight",value=None, format="%.2f",step=0.01,placeholder="Enter molecular weight")
molec_da_sel = dacol2.selectbox("unit", options=["Daltons (g/mol)","kDa"],key="k_molec_unit")
#st.divider()

#   ~ Container for the mass volume and result
form_molarity=mola_container.container(border=False)
mo_res_title= mola_container.text("Concentration")

#   ~ empty placeholder for the Result of calculation
mola_val=mola_container.empty()#I make empty container because I have multiple time callign of the calculation and otherwise it was creating multiple time the result widget
#       ~ Populate the empty placeholder with value from session_state of a global variable
mola_val.text(st.session_state["molarity_result"])

#   ~ empty placeholder for error message
error_message=mola_container.empty()#i create an empty container to avoid duplication of the error message in my "try" functions


#   ~ elements for user input( weight and volume)
with form_molarity:
    
    mocol1,mocol2,mocol3,mocol4,mocol5 = st.columns(5)
    mo_weight_inp= mocol1.text_input("Weight input", "",placeholder="Enter number")
    mo_weight_sel= mocol2.selectbox("Weight unit",options=["g","mg","µg","ng","pg"],index=2)

    mo_weight_sep= mocol3.text("--    in   --")

    mo_vol_inp= mocol4.text_input("volume input", "",placeholder="Enter number")
    mo_vol_sel= mocol5.selectbox("volume unit",options=["L","mL","µL"],index=1)

    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    submit = st.button('Calculate Molarity')

def calc_molarity():
    tmp_mass=float(mo_weight_inp)*dict_unit["mass"][mo_weight_sel]
    tmp_MW=float(molec_da_inp)*dict_unit["MW"][molec_da_sel]
    tmp_vol=float(mo_vol_inp)*dict_unit["vol"][mo_vol_sel]
    tmp_M_unit=float(dict_unit["molarity_unit"][st.session_state["k_mol_sel"]])

    st.session_state["molarity_result"]=str(round((tmp_mass)/(tmp_MW)/(tmp_vol)*(tmp_M_unit),5))      

if submit:
    try:
        calc_molarity()
        mola_val.text(st.session_state["molarity_result"])
        #mola_val.text(str(round(((int(mo_weight_inp)*dict_unit["mass"][mo_weight_sel]/(int(molec_da_inp)*dict_unit["MW"][molec_da_sel]))/(int(mo_vol_inp)*dict_unit["vol"][mo_vol_sel]))*(int(dict_unit["molarity_unit"][mo_res_sel])),5)))
    except Exception as error:
        error_message.error("Please fill all required fields with a number", icon="🚨")
        print("An exception occurred 1:", error)
        st.session_state["molarity_result"]=""
        mola_val.text(st.session_state["molarity_result"])
        #if ((vect_size !=None and vect_size>0 ) and (vect_amt!=None and vect_amt>0) & (insert_size !=None and insert_size>0 )):
            #submit_toast=st.toast("Calculation done")
  #use ast.literal_eval to convert 1:3 to an operation+
        
def change_molarity():#Need to modify it so that it uses only session.state in order to be able to put bac k the functio nat the beginning of the script
    try:
        if  (st.session_state["molarity_result"]=="") or (molec_da_inp==None) or (mo_weight_inp==None) or (mo_weight_inp=="") or (mo_vol_sel==None) or (mo_vol_sel=="") :
            print("Nothing to change")
            st.session_state["molarity_result"]=""
            mola_val.text(st.session_state["molarity_result"])
        else:
        
            print(st.session_state["k_mol_sel"])
            print(int(dict_unit["molarity_unit"][st.session_state["k_mol_sel"]]))
            #st.session_state["molarity_result"]=(str(round(((float(mo_weight_inp)*dict_unit["mass"][mo_weight_sel]/(float(molec_da_inp)*dict_unit["MW"][molec_da_sel]))/(float(mo_vol_inp)*dict_unit["vol"][mo_vol_sel]))*(float(dict_unit["molarity_unit"][st.session_state["k_mol_sel"]])),5)))
            calc_molarity()
            mola_val.text(st.session_state["molarity_result"])
    except Exception as error:
        print("An exception occurred:", error)

    

mo_res_sel= mola_container.selectbox("concentration unit",options=["M","mM","µM","nM","pM"],index=0, key="k_mol_sel", on_change=change_molarity())




####Need to make calculation as a function. Need to implement change the unit of molarity    

