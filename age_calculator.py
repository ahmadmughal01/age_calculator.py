import streamlit as st
from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    st.title("Age Calculator")
    st.write("Enter your date of birth to calculate your age:")

    # Date input widget for user to enter their date of birth
    birth_date = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())

    if st.button("Calculate Age"):
        if birth_date:
            age = calculate_age(birth_date)
            st.success(f"Your age is {age} years.")
        else:
            st.warning("Please select a valid date of birth.")

if __name__ == "__main__":
    main()
