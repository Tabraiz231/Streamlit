
import streamlit as st


from datetime import datetime

# Function to calculate age
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Streamlit app
def main():
    st.title("Age Calculator App")

    # Get user's birthdate input
    birthdate = st.date_input("Select your birthdate")
    
    # Ensure the user has selected a birthdate
    if birthdate:
        age = calculate_age(birthdate)
        st.write(f"Your age is {age} years old.")

if __name__ == "__main__":
    main()




   
