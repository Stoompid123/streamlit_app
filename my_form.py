import streamlit as st
def app():
	title = st.title("House Buying Form")
	name = st.text_input("Name")
	age = st.text_input("Age")
	adress = st.text_input("Adress of house")
	purpose = st.write("What is your purpose of buying?")
	op1 = st.checkbox("renting")
	op2 = st.checkbox("buying")
	op3 = st.checkbox("buisness")
	op4 = st.checkbox("industrial")
	if st.button("Submit"):
		if name == "" or age == "" or adress =="":
			st.warning("Some fields are missing, try again")
		else:
			st.success("Your form has been submitted sucessfully")
		if op1 == True or op2 == True or op3 == True or op4 == True:
			st.info("purpose has been selected")

