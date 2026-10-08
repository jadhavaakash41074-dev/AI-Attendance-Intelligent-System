import streamlit as st

from src.components.header import header_dashboard

from src.ui.style_base_layout import style_background_dashboard,style_base_layout

from src.components.footer import footer_login_dashboard

from src.components.subject_card import subject_card

from src.components.create_subject_dialog import create_subject_dialog

from src.database.db import check_techer_exists , create_teacher,teacher_login,get_teacher_subject

from src.components.create_subject_dialog import create_subject_dialog

from src.components.dialog_share_subject import share_subject_dialog


def teacher_screen():

    style_background_dashboard()

    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()

    elif "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type == "login":

        teacher_screen_login()

    elif st.session_state.teacher_login_type == "register":

        teacher_screen_register()

def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    c1 , c2 = st.columns(2, vertical_alignment="center", gap ="xxlarge")

    with c1:
        header_dashboard()
    with c2:
        st.header(f""" Welcome {teacher_data['name']}""") 
        if st.button("Logout", type = "primary",key = "loginbackbtn", shortcut="control+backspace"):
            st.session_state["is_logged_in"] = False
            del st.session_state.teacher_data
            st.rerun()


    st.space()
    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = "take_attendance"

    tab1 , tab2, tab3 = st.columns(3)

    with tab1:
        type1 = "secondary" if   st.session_state.current_teacher_tab =='take_attendance' else "tertiary"
        if st.button('Take Attendance',type =type1, width ="stretch", icon =':material/ar_on_you:'):
            st.session_state.current_teacher_tab ='take_attendance'
            st.rerun()

    with tab2:
            type2 = "secondary" if   st.session_state.current_teacher_tab =='manage_subject' else "tertiary"
            if st.button('Manage Subjects',type = type2, width ="stretch", icon =':material/book_ribbon:'):
                st.session_state.current_teacher_tab ='manage_subject'
                st.rerun()

    with tab3:
            type3 = "secondary" if   st.session_state.current_teacher_tab =='attendance_records' else "tertiary"
            if st.button('Attendance Records',type = type3, width ="stretch", icon =':material/cards_stack:'):
                st.session_state.current_teacher_tab ='attendance_records'
                st.rerun()

    st.markdown("""
    <div style="
        width: 100%;
        height: 3px;
        background-color: #8A8FA3;
        margin: 25px 0;
        border-radius: 10px;
    "></div>
    """, unsafe_allow_html=True)

    if st.session_state.current_teacher_tab =='take_attendance':
        teacher_tab_take_attendance()
    if st.session_state.current_teacher_tab =='manage_subject':
            teacher_tab_manage_subject()
    if st.session_state.current_teacher_tab =='attendance_records':
            teacher_tab_attendance_records()


    footer_login_dashboard()

def teacher_tab_take_attendance():
    st.header("Take AI Attendence")

def teacher_tab_manage_subject():

    teacher_id = st.session_state.teacher_data["teacher_id"]

    col1 , col2 = st.columns(2)

    with col1:

        st.header("Manage Subjects")

    with col2:

        if st.button("Create New Subject", width="stretch",type ="primary"):

            create_subject_dialog(teacher_id)

    #LIST ALL SUBJECTS 

    subjects= get_teacher_subject(teacher_id)

    if subjects:

        for sub in subjects:

            stats = [

                ("👥","Students",sub["total_students"]),

                ("🏫","Classes",sub["total_classes"])

            ]

            def share_btn():

                if st.button(

                        f'Share Code : {sub["name"]}',

                        key=f'share_{sub["subject_code"]}',

                        icon=":material/share:"

                    ):

                    share_subject_dialog(sub["name"], sub["subject_code"])

                st.space()

            subject_card(

                name = sub['name'],

                code = sub["subject_code"],

                section = sub["section"],

                stats = stats,

                footer_callback = share_btn

            )

    else :

        st.info("NO SUBJECT FOUND.CREATE ONE ABOVE")


def teacher_tab_attendance_records():

    st.header("Attendance Record")
   

def login_teacher(username , password):

    if not username or not password:
        return False
    
    teacher =  teacher_login(username, password)

    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data= teacher
        st.session_state.is_logged_in = True
        return True
    return False


def teacher_screen_login():

    c1 , c2 = st.columns(2,vertical_alignment="center",gap = "xxlarge")

    with c1:

        header_dashboard()

    with c2:

        if st.button("Go back to Home", type = "secondary",key ="loginbackbtn", shortcut="control+backspace"):

            st.session_state["teacher_login_type"] = "login"

            st.session_state["login_type"] = None

            st.rerun()


    st.header("Login Using Password",text_alignment="center")

    st.space()

    # text can visible in black color

    st.markdown("""

            <style>

             label {

                color: black !important ;

                }

            </style>

        """, unsafe_allow_html=True)


    teacher_username = st.text_input("Enter here Username",placeholder="Enter Username")


    # icon button to view password color

    teacher_password = st.text_input("Enter here Password", type = "password",placeholder="Enter password")


    st.markdown("""

        <style>

        button[data-testid="stTextInputPasswordVisibilityButton"] svg {

            stroke: #5B75F3 !important;

        }

        </style>

        """, unsafe_allow_html=True)


    # creating buttons login and register

    col1 , col2 =st.columns(2)

    with col1:

        if st.button("Login", type="primary",icon=":material/passkey:",icon_position="left",width="stretch"):

            if login_teacher(teacher_username,teacher_password):

                st.toast("Welcome back!",icon="👋")

                import time

                time.sleep(1)

                st.rerun()

            else:

                st.error("Invalid Username and password combo")


    with col2:

        if st.button("Register Instead", type="secondary", icon=":material/passkey:",icon_position="left",width="stretch"):

            st.session_state.teacher_login_type = "register"

            st.rerun()


    # footer

    footer_login_dashboard()


def register_teacher(teacher_username , teacher_name, teacher_password, teacher_password_confirm):

    if not teacher_username or not teacher_name or not teacher_password or not teacher_password_confirm:

        return False, "All fields are required"


    if check_techer_exists(teacher_username):

        return False ,"Username already exists"


    if teacher_password != teacher_password_confirm:

        return False , "Password doesn't match"


    try:

        create_teacher(teacher_username,teacher_password,teacher_name)

        return True,"Successfully Created Profile! Login Now"

    except Exception as e:

        return False, f"Unexpected Error: {e}"


def teacher_screen_register():

    style_background_dashboard()

    style_base_layout()


    c1 , c2 = st.columns(2,vertical_alignment="center",gap = "xxlarge")

    with c1:

        header_dashboard()

    with c2:

        if st.button("Go back to Home", type = "primary",key ="registerbackbtn", shortcut="control+backspace"):

            st.session_state["teacher_login_type"] = "login"

            st.session_state["login_type"] = None

            st.rerun()


    st.space()

    st.header("Register your teacher profile", text_alignment="center")


    # text can visible in black color

    st.markdown("""

            <style>

                label {

                color: black !important ;

                }

            </style>

        """, unsafe_allow_html=True)


    teacher_username = st.text_input("Enter here Username",placeholder="Enter Username")


    teacher_name = st.text_input("Enter Here Name",placeholder="Enter Name")


    teacher_password = st.text_input("Enter here Password", type = "password",placeholder="Enter password")


    teacher_password_confirm = st.text_input("Confirm Your Password", type = "password",placeholder="Re-enter the password")


    st.markdown("""

        <style>

        button[data-testid="stTextInputPasswordVisibilityButton"] svg {

            stroke: #5B75F3 !important;

        }

        </style>

        """, unsafe_allow_html=True)


    # creating buttons login and register

    col1 , col2 =st.columns(2)


    with col1:

        if st.button("Register", type="primary",icon=":material/passkey:",icon_position="left",width="stretch"):

            success , message = register_teacher(

                teacher_username,

                teacher_name,

                teacher_password,

                teacher_password_confirm

            )


            if success:

                st.success(message)

                import time

                time.sleep(2)

                st.session_state.teacher_login_type ="login"

                st.rerun()

            else:

                st.error(message)


    with col2:

        if st.button("Login Instead", type="secondary", icon=":material/passkey:",icon_position="left",width="stretch"):

            st.session_state.teacher_login_type="login"

            st.rerun()


    # footer

    footer_login_dashboard()