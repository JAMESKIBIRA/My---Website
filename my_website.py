import streamlit as st
import requests

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

with st.container(border=True):
    st.subheader("I turn messy data into actionable insights using Python, R, and SQL.")
    st.write("I am a second-year BSc Statistics student at Kirinyaga University. I specialize in data cleaning, exploratory data analysis, and statistical modeling.")
    st.markdown("**Currently open to:** Data Analysis Internships & Junior Roles")

st.write("---")

# 4. Tech Stack
st.header("🛠️ My Tech Stack")
col_tech1, col_tech2, col_tech3, col_tech4 = st.columns(4)
with col_tech1:
    st.info("**Languages:**\nPython\nR\nSQL\nC")
with col_tech2:
    st.info("**Data Analysis:**\nPandas\nNumPy\nTidyverse\nMatplotlib")
with col_tech3:
    st.info("**Databases:**\nSQLite\nPostgreSQL")
with col_tech4:
    st.info("**Tools:**\nGit & GitHub\nStreamlit\nRStudio")

st.write("---")

# 5. Projects Section
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

st.write("---")

# Project 3: Interactive App
st.subheader("3. Interactive M-PESA Spending Analyzer")
col5, col6 = st.columns(2)
with col5:
    st.write("A live, interactive web app where users can upload their own M-PESA CSV files to instantly visualize their spending.")
    st.markdown("[Launch the App](https://james-mpesa-analyzer.streamlit.app)")
with col6:
    st.info("💡 Click the link to try the live data app!")

st.write("---")

# 6. Contact Form
st.header("📬 Send Me a Message")
st.write("Have a project in mind? Let's connect!")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send Message")

    if submit:
        formspree_url = "https://formspree.io/f/xvkkbepd" 
        
        response = requests.post(formspree_url, data={
            "name": name,
            "email": email,
            "message": message
        })
        
        if response.status_code == 200:
            st.success("Thank you! Your message has been sent.")
        else:
            st.error("Oops! Something went wrong. Please try again.")

st.write("---")
st.markdown(
    """
    <div style='text-align: center; color: grey; padding: 20px;'>
        <p>Built with ❤️ using Python & Streamlit by James Kiruma © 2026</p>
    </div>
    """, 
    unsafe_allow_html=True
)
