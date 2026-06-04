import streamlit as st
import pandas as pd
from analysis import *

st.set_page_config(
    page_title="Cricket Analytics Dashboard",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 Cricket Analytics Dashboard")

uploaded_file = st.file_uploader(
    "Upload Cricket CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    tab1, tab2, tab3, tab4 = st.tabs([
        "Overview",
        "Charts",
        "Correlation",
        "Top Records"
    ])

    with tab1:
        dataset_overview(df)

    with tab2:
        charts(df)

    with tab3:
        correlation_analysis(df)

    with tab4:
        top_records(df)
