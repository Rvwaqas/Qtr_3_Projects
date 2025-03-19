import streamlit as st
import re

st.title("🔐 Password Strength Meter")

st.write("Enter your password below the check its strength:")

def check_password(password):
    score=0
    feedback=[]
    if len(password)>=0:
        score+=1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score+=1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d",password):
        score+=1
    else:
         feedback.append("❌ Add at least one number (0-9).")

    
    if re.search(r"[!@#$%^&*]",password):
        score+=1
    else:
       feedback.append("❌ Add at least one special character (!@#$%^&*).")
    
    if score==4:
        st.success("✅ Strong Password!")
    elif score==3:
        st.subheader("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.subheader("❌ Weak Password - Improve it using the suggestions above.")
    if feedback:
        st.subheader("Suggestions to improve your password:")
        for message in feedback:
            st.write(message)





password_strength=st.text_input("Enter your password")
if st.button("Check your password strength"):
    check_password(password_strength)


