import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="Live Excel Viewer",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Auto-refresh every 5 minutes (300000 ms)
st_autorefresh(interval=300000, key="datarefresh")

excel_path = "D:/RPA/Zerodha/BSE/DataAlignment.xlsm"
st.title("📊 BSE Data Alignment - Live View")

try:
    df = pd.read_excel(excel_path, engine='openpyxl')
    st.dataframe(df.astype(str), height=1000, use_container_width=True)
except Exception as e:
    st.error(f"Error loading Excel file: {e}")
