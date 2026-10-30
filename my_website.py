import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="James Kiruma | Data Analyst", page_icon="📊", layout="wide")

# 2. Sidebar
with st.sidebar:
    st.image("profile.png", width=200)
    st.title("James Kiruma")
    st.write("Data Analyst & Statistician")
    st.write("📍 Kutus, Kirinyaga, Kenya")
    st.write("📧 kibirajames33@gmail.com")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/james-kibira-7892a1444/) | [GitHub](https://github.com/JAMESKIBIRA)")
    st.write("---")
    st.write("Welcome to my portfolio!")

# 3. Main Page Header
st.title("Welcome to my Data Portfolio 🚀")
st.subheader("I turn messy data into actionable insights using Python, R, and SQL.")
st.write("I am a second-year BSc Statistics student at Kirinyaga University. I specialize in data cleaning, exploratory data analysis, and statistical modeling.")

st.write("---")

# 4. Projects Section
st.header("📊 My Data Projects")

# Project 1: M-PESA
st.subheader("1. M-PESA Spending Tracker")
col1, col2 = st.columns(2)
with col1:
    st.write("A Python and SQL data pipeline that extracts, cleans, and analyzes M-PESA transaction data.")
    st.markdown("[View the GitHub Repository](https://github.com/JAMESKIBIRA/M-PESA-Spending-Tracker)")
with col2:
    st.image("mpesa_chart.png", caption="M-PESA Spending by Category", use_container_width=True)

st.write("---")

# Project 2: DHS Malnutrition
st.subheader("2. Kenya DHS 2022 Malnutrition Analysis")
col3, col4 = st.columns(2)
with col3:
    st.write("A statistical analysis using R to identify the socioeconomic determinants of child malnutrition across 19,530 records.")
    st.markdown("[View the GitHub Repository](https://github.com/JAMESKIBIRA/Kenya---malnutrition---dhs)")
with col4:
    st.image("dhs_chart.png", caption="Top 10 Counties with Highest Stunting", use_container_width=True)
