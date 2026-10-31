import requests

st.write("---")
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
