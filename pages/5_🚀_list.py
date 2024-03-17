
#Everything update each time you change unit for example because I don't use st.form widget
import streamlit as st
import json
import time
import json
from os import path

st.set_page_config(page_title="List with database", page_icon="🚀")
st.title("List")

listCont=st.container()
dataBase = "./data/dataBase.json"
if path.isfile(dataBase) is False:
  raise Exception("File not found")
dictDB = {}
with open(dataBase, 'r+') as db:
  dictDB = json.load(db)
for i in dictDB["List"]:
  print(dictDB["List"][i])
  listCont.title(dictDB["List"][i])

addItemCont=st.container()

def addItem():
  tempDB = {}
  with open(dataBase, 'r+') as db:
    tempDB = json.load(db)
  i = len(tempDB["List"])
  tempDB["List"][f'key{i+1}']=itemText# to add the content of itemText as value of the key "key{i+1}" to the dictionary tempDB
  
  with open(dataBase, 'w') as json_file:
    json.dump(tempDB, json_file,
                        indent=4,
                        separators=(',',': '))
itemText=addItemCont.text_input(label="Item to add", key="inpText")# 
addItemCont.button("Add item to the list", on_click=addItem)#callback function here must be written addItem and not addItem() otherwise it does not work properly
