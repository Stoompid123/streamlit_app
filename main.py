import login_form
import my_form
import streamlit as st

pages_dict = {
	"Login": login_form, 
	"Form": my_form

} 
st.sidebar.title ("Navigation")
choices= st.sidebar.radio("Go To", tuple(pages_dict.keys()))
if choices == "Form":
	my_form.app()
else:
	login_form.app()