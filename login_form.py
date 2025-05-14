import streamlit as st
def app():
	title = st.title("Login")
	username = st.text_input("Username:")
	password = st.text_input("Password:")
	user_list = ["Hello", "Beach123", "RYANREYNOLDSISHOT"]
	password_list = ["DOGGY123", "SUNBRELLA234" , "MOVIES123"]
	user_password = dict(zip(user_list, password_list))
	if st.button("login"):
		if username not in user_list:
			st.warning("The username does not exist")
		else:
			if password == user_password[username]:
				st.success("successfully logged in")
			else:
				st.warning("incorrect password")