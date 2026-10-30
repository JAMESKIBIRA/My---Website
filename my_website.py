import streamlit as st

st.set_page_config(page_title="James Kiruma | Data Analyst", page_icon="📊")

st.title("James Kiruma")
st.subheader("Data Analyst & Statistician | Python, R, SQL")

st.write("""
Welcome to my portfolio! I am a second-year BSc Statistics student at Kirinyaga University.
I specialize in data cleaning, exploratory data analysis, and statistical modeling.
""")

st.header("My Projects")

st.subheader("1. M-PESA Spending Tracker")
st.write("A Python and SQL data pipeline that extracts, cleans, and analyzes M-PESA transaction data.")
st.markdown("[View the GitHub Repository](https://github.com/JAMESKIBIRA/M-PESA-Spending-Tracker)")

st.subheader("2. Kenya DHS 2022 Malnutrition Analysis")
st.write("A statistical analysis using R to identify the socioeconomic determinants of child malnutrition across 19,530 records.")
st.markdown("[View the GitHub Repository](https://github.com/JAMESKIBIRA/Kenya---malnutrition---dhs)")

st.header("Contact Me")
st.write("Email: kibirajames33@gmail.com")
st.write("LinkedIn: https://www.linkedin.com/in/james-kibira-7892a1444/")
