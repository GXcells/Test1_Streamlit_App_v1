
#Everything update each time you change unit for example because I don't use st.form widget
import streamlit as st
import time
import json
st.set_page_config(page_title="Molecular tools", page_icon="🚀")
st.title("Molecular tools")

#   ~ dictionnary to hold data for calculation
dict_unit={
    "MW":{"Daltons (g/mol)":1,"kDa":1000},
    "mass":{"g":1,"mg":10**-3,"µg":10**-6,"ng":10**-9,"pg":10**-12},
    "vol":{"L":1,"mL":10**-3,"µL":10**-6},
    "molarity_unit":{"M":1,"mM":10**3,"µM":10**6,"nM":10**9,"pM":10**12},}


#   ~ define all my session_states
#      ~ for the molarity calculator
if "k_mol_sel" not in st.session_state:#k_mol_sel is the key for the molarity concentration unit selector
    st.session_state["k_mol_sel"]="M"
if "molarity_result" not in st.session_state:#we create "molarity result" session_state variable to store the result
    st.session_state["molarity_result"]=""
#      ~ for the volume calculator
if "k_volres_sel" not in st.session_state:#k_volres_sel is the key for the volume unit selector i nthe Volume calculator
    st.session_state["k_volres_sel"]="mL"
if "volume_result" not in st.session_state:
    st.session_state["volume_result"]=""

wait_spinner=st.empty()
#   ~ MAIN CONTAINER OF MOLARITY CALCULATOR
mola_container=st.container(border=True)

#   ~ Container for the MOLECULAR WEIGHT part
container_da = mola_container.container(border=True)
dacol1,dacol2 = container_da.columns(2)
mo_da_in = dacol1.number_input("Molecular weight",value=None, format="%.2f",step=0.01,placeholder="Enter molecular weight")
mo_da_se = dacol2.selectbox("unit", options=["Daltons (g/mol)","kDa"],key="k_molec_unit")
#st.divider()

#   ~ Title for molarity calculator

mola_container.header("Calculate molarity of a solution")


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
        with st.spinner("Please wait"):
            
            
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
################################################
###############################################
################################################
###############################################

#   ~Title for the volume calculator
mola_container.header("Calculate volume required")


#   ~ Container for the mass volume and result
form_volume=mola_container.container(border=True)


#   ~ empty placeholder for error message
error_messagevol=form_volume.empty()#i create an empty container to avoid duplication of the error message in my "try" functions


#   ~ elements for user input( weight and concentration)
with form_volume:
    
    vocol1,vocol2,vocol3,vocol4,vocol5 = st.columns(5)
    vo_w_in= vocol1.text_input("Weight input", "",placeholder="Enter number", key="k_vo_w_in")
    vo_w_se= vocol2.selectbox("Weight unit",options=["g","mg","µg","ng","pg"],index=2, key="k_vo_w_se")

    vo_weight_sep= vocol3.text("--    in   --")

    vo_c_in= vocol4.text_input("Concentration input", "",placeholder="Enter number", key="k_vo_c_in")
    vo_c_se= vocol5.selectbox("Concentration unit",options=["M","mM","µM","nM","pM"],index=1, key="k_vo_c_se")

    vo_res_emptyxol= vocol3.text(" ")
    vo_res_emptyxol= vocol3.text(" ")
    vo_res_emptyxol= vocol3.text(" ")
    vo_res_emptyxol= vocol3.text(" ")
    submitvol = st.button('Calculate Volume')
    
#   ~ empty placeholder for the Result of calculation
vo_res_title= form_volume.text("Volume")
vol_val=form_volume.empty()#I make empty container because I have multiple time callign of the calculation and otherwise it was creating multiple time the result widget
#       ~ Populate the empty placeholder with value from session_state of a global variable
vol_val.text(st.session_state["volume_result"])

#   ~ Main function for calculating the volume
def calc_volume():
    tmp_mass=float(vo_w_in)*dict_unit["mass"][vo_w_se]
    tmp_MW=float(mo_da_in)*dict_unit["MW"][mo_da_se]
    tmp_conc=float(vo_c_in)*1/(dict_unit["molarity_unit"][vo_c_se])
    tmp_vol_unit=float(dict_unit["vol"][st.session_state["k_volres_sel"]])

    #st.session_state["molarity_result"]=f'{round((tmp_mass)/(tmp_MW)/(tmp_vol)*(tmp_M_unit),5):.6f}'#this is to format the number to  6  decimal and remove scientific notation when it appears
    st.session_state["volume_result"]=f'{round((tmp_mass)/(tmp_MW)/(tmp_conc)/(tmp_vol_unit),5)}'
    print((tmp_mass)/(tmp_MW))   
    print(float(vo_c_in)*dict_unit["molarity_unit"][vo_c_se])
    print((tmp_conc)) 
    print((tmp_vol_unit))
    print(st.session_state["volume_result"])
#   ~ Callback from the "calculate Molarity" button when pushed
if submitvol:
    try:
        calc_volume()
        vol_val.text(st.session_state["volume_result"])
        #mola_val.text(str(round(((int(mo_w_in)*dict_unit["mass"][mo_w_se]/(int(mo_da_in)*dict_unit["MW"][mo_da_se]))/(int(mo_v_in)*dict_unit["vol"][mo_v_se]))*(int(dict_unit["molarity_unit"][mo_res_sel])),5)))
    except Exception as error:
        error_messagevol.error("Please fill all required fields with a number", icon="🚨")
        print("An exception occurred 1:", error)
        st.session_state["volume_result"]=""
        vol_val.text(st.session_state["volume_result"])

#   ~ Function callback fro mthe concentration unit selector box      
def change_volume():#Need to modify it so that it uses only session.state in order to be able to put bac k the functio nat the beginning of the script
    try:
        if  (st.session_state["volume_result"]=="") or (mo_da_in==None) or (vo_w_in==None) or (vo_w_in=="") or (vo_c_in==None) or (vo_c_in=="") :
            print("Nothing to change_changevolume")
            st.session_state["volume_result"]=""
            vol_val.text(st.session_state["volume_result"])
        else:
        
            print(st.session_state["k_volres_sel"])
            print(int(dict_unit["vol"][st.session_state["k_volres_sel"]]))
            calc_volume()
            vol_val.text(st.session_state["volume_result"])
    except Exception as error:
        print("An exception occurred in change_volume:", error)

    

vo_res_sel= form_volume.selectbox("volume unit",options=["L","mL","µL"],index=0, key="k_volres_sel", on_change=change_volume())

