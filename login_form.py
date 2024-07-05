import streamlit as st
import database
from time import sleep
from st_pages import hide_pages

hide_pages(['line'])

def main():
    st.title("login form")
    with st.form("my_form"):
        st.write("Login to view the covid-19 analysis")
        username = st.text_input("USERNAME")
        password = st.text_input("PASSWORD",type='password')
        submitted = st.form_submit_button("Submit")
        if submitted:
            if username == "":
                st.info("username is not mentioned..")
            elif password =="":
                st.info("password is not mentioned..")
            else:        
                output = database.admin_login((username,password))
                if output:
                    st.success("sucessfully logined....")
                    sleep(0.3)
                    st.experimental_set_query_params(page='line')
                else:
                    st.error("login details are incorrect..")    


if __name__ == "__main__":
    main()
