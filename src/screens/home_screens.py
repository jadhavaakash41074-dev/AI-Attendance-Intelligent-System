import streamlit as st
from src.components.header import header_home
from src.ui.style_base_layout import style_base_layout,style_background_home,style_background_dashboard
from src.components.footer import footer_home
def home_screen():

    header_home()
    style_base_layout()
    style_background_dashboard()
    style_background_home()

    # Center buttons
    st.markdown("""
    <style>
        h2 {
            text-align: center !important;
        }

        .stButton {
            display: flex;
            justify-content: center;
        }
    </style>
    """, unsafe_allow_html=True)

    
    st.markdown("""
        <style>
            div[data-testid="stHorizontalBlock"] {
                margin-top: -80px !important;
            }
    </style>
    """, unsafe_allow_html=True)
    

    # Add home screen functionality here
    col1, col2 = st.columns(2,gap="large")

    with col1:

        st.header("I'm Teacher")

        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://img.magnific.com/premium-vector/education-material-icon-vector-illustration_1287271-7931.jpg?semt=ais_hybrid&w=740&q=80"
                     style="width:200px; height:150px; object-fit:contain;">
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("""
                <style>
                    .stButton {
                        margin-top: 20px;
                    }
                </style>
            """, unsafe_allow_html=True)

        if st.button("Teacher Portal", type="primary",icon=":material/login:",icon_position="right"):
            st.session_state["login_type"] = "teacher"
            st.rerun()


    with col2:

        st.header("I'm Student")

        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://i.pinimg.com/originals/42/ac/13/42ac13d6fda6321088eb091cf351f8f1.jpg?nii=t"
                     style="width:200px; height:150px; object-fit:contain;">
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("""
                <style>
                    .stButton {
                        margin-top: 20px;
                    }
                </style>
            """, unsafe_allow_html=True)
        if st.button("Student Portal", type="primary",icon=":material/login:",icon_position="right"):
            st.session_state["login_type"] = "student"
            st.rerun()

    footer_home()