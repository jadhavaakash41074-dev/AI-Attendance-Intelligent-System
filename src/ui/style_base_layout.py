
import streamlit as st

def style_background_home():

    st.markdown("""
        <style>

        .stApp {
            background: #5868F2 !important;
        }

        div[data-testid="stColumn"] > div {
            background-color: white !important;
            padding: 2rem !important;
            border-radius: 2rem !important;
            box-shadow: 0 3px 13px rgba(0,0,0,0.15) !important;
        }

        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>
              .stApp{
                  background : #E0E3FF !important;
              }
        </style>

    """, 
    unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>

             @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@100..900&display=swap');

              /* Hide Top bar of Streamlit */

              #MainMenu, footer, header{
                  visibility : hidden;
              }

              .block-container{
                   padding-top: 1.5rem !important;
              }

              h1 {
                    font-family : "Climate Crisis", sans-serif !important;
                    font-size : 3.5rem !important;
                    line-height : 1.1 !important;
                    margin-bottom : 0rem !important;
                    color : whitjust e !important;
                }

            h2 {
                font-family : "Climate Crisis", sans-serif !important;
                font-size : 1.5rem !important;
                line-height : 0.9 !important;
                margin-bottom : 0rem !important;
                color : black !important;
            }

            h3, p, h4{
                   font-family : "Outfit", sans-serif !important;
            }

            button{
                    border-radius : 1.5rem !important;
                    background : rgb(213, 94, 195) !important;
                    color : white !important;
                    padding : 10px 20px !important;
                    border : none !important;
                    transition : transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"]{
                    border-radius : 1.5rem !important;
                    background : #EB459E !important;
                    color : white !important;
                    padding : 10px 20px !important;
                    border : none !important;
                    transition : transform 0.25s ease-in-out !important;
            }

            button[kind="tertiary"] {
                    border-radius : 1.5rem !important;
                    background : black !important;
                    color : white !important;
                    padding : 10px 20px !important;
                    border : none !important;
                    transition : transform 0.25s ease-in-out !important;
            }

            button:hover{
                    transform : scale(1.05);
            }

        </style>

    """,  
    unsafe_allow_html=True)