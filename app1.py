import streamlit as st

def main():
    st.header("Welcomoe to face reconition")
    name = st.text_input("Enter here name")

    col1 , col2 = st.columns(2,gap = "medium")
    with col1:
        if st.button("submit your name ", type="primary", key = "btn1" , width = "stretch"):
            print("Name is : ", name)
    with col2:
        if st.button("submit unkwon ", type="primary", key = "btn2" , width = "stretch"):
            print("Name is unknwon")

    # markdown => help to overwriting the css and html also help to adding the text on websiet 
    st.markdown(
        """
        <style>
        button{
        background-color: orange !important;
        }""", unsafe_allow_html=True)

main()