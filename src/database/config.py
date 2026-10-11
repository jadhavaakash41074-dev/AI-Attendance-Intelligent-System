import streamlit as st

from supabase import create_client , Client

# creation the instance of database
supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)