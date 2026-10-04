import streamlit as st

def header_home():
    logo_url = "https://snapclass-landing-page-theta.vercel.app/static/img/logo.png"

    st.markdown(f"""
            <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:15px; margin-top:15px">
                <img src="{logo_url}" style="height:100px;"/>
                <h1 style="text-align:center; color:#E0E3FF;">SNAP<br/>CLASS</h1>
            </div>
        """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://snapclass-landing-page-theta.vercel.app/static/img/logo.png"

    st.markdown(f"""
        <style>
            .dashboard-title {{
                color: #5865F2 !important;
            }}
        </style>

        <div style="display:flex; align-items:center; justify-content:center; gap:10px; margin-top:15px">
            <img src="{logo_url}" style="height:85px;"/>
            <h2 class="dashboard-title" style="text-align:left;">
                SNAP<br/>CLASS
            </h2>
        </div>
    """, unsafe_allow_html=True)