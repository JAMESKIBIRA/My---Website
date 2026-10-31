import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="M-PESA Spending Analyzer", page_icon="💸")

st.title("💸 M-PESA Spending Analyzer")
st.write("Upload your M-PESA statement (CSV) below to instantly see where your money goes!")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        
        st.success("File uploaded successfully!")
        st.write("Here is a preview of your data:")
        st.dataframe(df.head())

        # Check for the correct column names
        if 'Details' in df.columns and 'Withdrawn' in df.columns:
            
            def categorize(details):
                details = str(details).lower()
                if 'bundle' in details or 'airtime' in details: return 'Airtime & Data'
                if 'fuliza' in details or 'overdraft' in details: return 'Loans'
                if 'pay bill' in details or 'merchant' in details: return 'Bills & Shopping'
                if 'send money' in details or 'transfer' in details: return 'Send Money'
                return 'Other'

            df['Category'] = df['Details'].apply(categorize)
            
            # Use 'Withdrawn' for the amount spent
            df_out = df[df['Withdrawn'] > 0]
            category_sum = df_out.groupby('Category')['Withdrawn'].sum()

            st.subheader("Your Spending by Category")
            fig, ax = plt.subplots()
            category_sum.plot(kind='barh', color='darkred', ax=ax)
            ax.set_xlabel("Amount (KES)")
            st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")
