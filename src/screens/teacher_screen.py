import streamlit as st
from src.components.header import header_dashboard
from src.ui.style_base_layout import style_background_dashboard,style_base_layout
from src.components.footer import footer_login_dashboard



def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    teacher_screen_login()

    # c1 , c2 = st.columns(2,vertical_alignment="center",gap = "xxlarge")
    # with c1:
    #     header_dashboard()

    # with c2:
    #     st.button("Go back to Home", type = "secondary",key ="login_back_button")
    # st.header("Register your teacher profile")

def teacher_screen_login():

    c1 , c2 = st.columns(2,vertical_alignment="center",gap = "xxlarge")
    with c1:
        header_dashboard()

    with c2:
        st.button("Go back to Home", type = "primary",key ="login_back_button",shortcut="control+Enter",width="stretch",icon =":material/home:",icon_position="left")
    st.header("Login here",text_alignment="center")
    st.space()

    #text can visible in black color 
    st.markdown("""
            <style>
             label {
                color: black !important ;
                }
            </style>
        """, unsafe_allow_html=True)

    teacher_username = st.text_input("Enter here Username",placeholder="Enter Username")

    #icon button to view password color :
    

    teacher_password = st.text_input("Enter here Password", type = "password",placeholder="Enter password")
    st.markdown("""
        <style>

        button[data-testid="stTextInputPasswordVisibilityButton"] svg {
            stroke: #5B75F3 !important;
        }

        </style>
        """, unsafe_allow_html=True)

    #creating buttons login and register 
    col1 , col2 =st.columns(2)
    with col1:
        st.button("Login", type="primary",icon=":material/passkey:",icon_position="left",width="stretch")
    with col2:
        st.button("Register", type="secondary", icon=":material/passkey:",icon_position="left",width="stretch")
    # footer 
    footer_login_dashboard()
    


def teacher_screen_register():
    style_background_dashboard()
    style_base_layout()

    c1 , c2 = st.columns(2,vertical_alignment="center",gap = "xxlarge")
    with c1:
        header_dashboard()

    with c2:
        st.button("Go back to Home", type = "secondary",key ="login_back_button")
    st.header("   Register your teacher profile")
