import streamlit as st
from src.components.header import header_dashboard
from src.ui.style_base_layout import style_background_dashboard,style_base_layout
from src.components.footer import footer_login_dashboard



def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()

def teacher_screen_login():

    c1 , c2 = st.columns(2,vertical_alignment="center",gap = "xxlarge")
    with c1:
        header_dashboard()

    with c2:
        if st.button("Go back to Home", type = "secondary",key ="loginbackbtn", shortcut="control+backspace"):
            st.session_state["login_type"] =None 
            st.rerun()

    st.header("Login Using Password",text_alignment="center")
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
        if st.button("Register Instead", type="secondary", icon=":material/passkey:",icon_position="left",width="stretch"):
            st.session_state.teacher_login_type = "register"
    # footer 
    footer_login_dashboard()
    


def teacher_screen_register():
    style_background_dashboard()
    style_base_layout()

    c1 , c2 = st.columns(2,vertical_alignment="center",gap = "xxlarge")
    with c1:
        header_dashboard()

    with c2:
        if st.button("Go back to Home", type = "primary",key ="loginbackbtn", shortcut="control+backspace"):
            st.session_state["login_type"] =None 
            st.rerun()

    st.space()
    st.header("Register your teacher profile", text_alignment="center")
    
    #text can visible in black color 
    st.markdown("""
            <style>
                label {
                color: black !important ;
                }
            </style>
        """, unsafe_allow_html=True)

    teacher_username = st.text_input("Enter here Username",placeholder="Enter Username")
    teacher_name = st.text_input("Enter Here Name",placeholder="Enter Username")

    teacher_password = st.text_input("Enter here Password", type = "password",placeholder="Enter password")

    teacher_password_confirm =  st.text_input("Confirm You'r Password", type = "password",placeholder="Renter the password")
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
        st.button("Register", type="primary",icon=":material/passkey:",icon_position="left",width="stretch")
    with col2:
        if st.button("Login Instead", type="secondary", icon=":material/passkey:",icon_position="left",width="stretch"):
            st.session_state.teacher_login_type="login"
    # footer 
    footer_login_dashboard()