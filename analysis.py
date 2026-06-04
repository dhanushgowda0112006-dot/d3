import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def dataset_overview(df):

    st.subheader("Column Details")

    info = pd.DataFrame({
        "Column": df.columns,
        "Datatype": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum()
    })

    st.dataframe(info)

    st.subheader("Statistics")
    st.dataframe(df.describe(include="all"))


def charts(df):

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found")
        return

    selected = st.selectbox(
        "Select Numeric Column",
        numeric_cols
    )

    fig, ax = plt.subplots()

    ax.hist(
        df[selected].dropna(),
        bins=20
    )

    ax.set_title(selected)

    st.pyplot(fig)


def correlation_analysis(df):

    numeric_df = df.select_dtypes(include="number")

    if len(numeric_df.columns) < 2:
        st.warning("Need at least 2 numeric columns")
        return

    corr = numeric_df.corr()

    st.dataframe(corr)

    fig, ax = plt.subplots(figsize=(8,6))

    image = ax.imshow(corr)

    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=90)

    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)

    plt.colorbar(image)

    st.pyplot(fig)


def top_records(df):

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found")
        return

    metric = st.selectbox(
        "Select Metric",
        numeric_cols
    )

    st.subheader(f"Top 10 by {metric}")

    st.dataframe(
        df.sort_values(
            by=metric,
            ascending=False
        ).head(10)
    )
