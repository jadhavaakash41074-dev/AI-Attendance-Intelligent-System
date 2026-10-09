import streamlit as st
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.screens.home_screens import home_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog


def main():
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    join_code = st.query_params.get('join-code')

    if join_code and st.session_state["login_type"] != "student":
        st.session_state["login_type"] = "student"
        st.rerun()

    match st.session_state["login_type"]:
        case "teacher":
            teacher_screen()
        case "student":
            student_screen()
        case None:
            home_screen()

    if (
        join_code
        and st.session_state.get('is_logged_in')
        and st.session_state.get('user_role') == 'student'
        and st.session_state.get('join_code_handled') != join_code
    ):
        st.session_state['join_code_handled'] = join_code
        auto_enroll_dialog(join_code)


main()