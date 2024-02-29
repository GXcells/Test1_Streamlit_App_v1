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
if "k_mol_sel" not in st.session_state:#k_mol_sel is the key for the molarity concentration unit selector
    st.session_state["k_mol_sel"]="M"
if "molarity_result" not in st.session_state:#we create "molarity result" session_state variable to store the result
    st.session_state["molarity_result"]=""

#   ~ MAIN CONTAINER OF MOLARITY CALCULATOR
mola_container=st.container(border=True)

#   ~ Container for the MOLECULAR WEIGHT part
container_da = mola_container.container(border=True)
dacol1,dacol2 = container_da.columns(2)
mo_da_in = dacol1.number_input("Molecular weight",value=None, format="%.2f",step=0.01,placeholder="Enter molecular weight")
mo_da_se = dacol2.selectbox("unit", options=["Daltons (g/mol)","kDa"],key="k_molec_unit")
#st.divider()

#   ~ Container for the mass volume and result
form_molarity=mola_container.container(border=True)




#   ~ empty placeholder for error message
error_message=form_molarity.empty()#i create an empty container to avoid duplication of the error message in my "try" functions


#   ~ elements for user input( weight and volume)
with form_molarity:
    
    mocol1,mocol2,mocol3,mocol4,mocol5 = st.columns(5)
    mo_w_in= mocol1.text_input("Weight input", "",placeholder="Enter number")
    mo_w_se= mocol2.selectbox("Weight unit",options=["g","mg","µg","ng","pg"],index=2)

    mo_weight_sep= mocol3.text("--    in   --")

    mo_v_in= mocol4.text_input("volume input", "",placeholder="Enter number")
    mo_v_se= mocol5.selectbox("volume unit",options=["L","mL","µL"],index=1)

    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    mo_res_emptyxol= mocol3.text(" ")
    submit = st.button('Calculate Molarity')
    
#   ~ empty placeholder for the Result of calculation
mo_res_title= form_molarity.text("Concentration")
mola_val=form_molarity.empty()#I make empty container because I have multiple time callign of the calculation and otherwise it was creating multiple time the result widget
#       ~ Populate the empty placeholder with value from session_state of a global variable
mola_val.text(st.session_state["molarity_result"])

#   ~ Main function for calculating the molarity
def calc_molarity():
    tmp_mass=float(mo_w_in)*dict_unit["mass"][mo_w_se]
    tmp_MW=float(mo_da_in)*dict_unit["MW"][mo_da_se]
    tmp_vol=float(mo_v_in)*dict_unit["vol"][mo_v_se]
    tmp_M_unit=float(dict_unit["molarity_unit"][st.session_state["k_mol_sel"]])

    #st.session_state["molarity_result"]=f'{round((tmp_mass)/(tmp_MW)/(tmp_vol)*(tmp_M_unit),5):.6f}'#this is to format the number to  6  decimal and remove scientific notation when it appears
    st.session_state["molarity_result"]=f'{round((tmp_mass)/(tmp_MW)/(tmp_vol)*(tmp_M_unit),5)}'    
 
#   ~ Callback from the "calculate Molarity" button when pushed
if submit:
    try:
        calc_molarity()
        mola_val.text(st.session_state["molarity_result"])
        #mola_val.text(str(round(((int(mo_w_in)*dict_unit["mass"][mo_w_se]/(int(mo_da_in)*dict_unit["MW"][mo_da_se]))/(int(mo_v_in)*dict_unit["vol"][mo_v_se]))*(int(dict_unit["molarity_unit"][mo_res_sel])),5)))
    except Exception as error:
        error_message.error("Please fill all required fields with a number", icon="🚨")
        print("An exception occurred 1:", error)
        st.session_state["molarity_result"]=""
        mola_val.text(st.session_state["molarity_result"])

#   ~ Function callback fro mthe concentration unit selector box      
def change_molarity():#Need to modify it so that it uses only session.state in order to be able to put bac k the functio nat the beginning of the script
    try:
        if  (st.session_state["molarity_result"]=="") or (mo_da_in==None) or (mo_w_in==None) or (mo_w_in=="") or (mo_v_se==None) or (mo_v_se=="") :
            print("Nothing to change")
            st.session_state["molarity_result"]=""
            mola_val.text(st.session_state["molarity_result"])
        else:
        
            print(st.session_state["k_mol_sel"])
            print(int(dict_unit["molarity_unit"][st.session_state["k_mol_sel"]]))
            calc_molarity()
            mola_val.text(st.session_state["molarity_result"])
    except Exception as error:
        print("An exception occurred:", error)

    

mo_res_sel= form_molarity.selectbox("concentration unit",options=["M","mM","µM","nM","pM"],index=0, key="k_mol_sel", on_change=change_molarity())




####Need to make calculation as a function. Need to implement change the unit of molarity    

