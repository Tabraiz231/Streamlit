import streamlit as st
# Title of the app
st.title("Simple Calculator")
# Input fields
st.header("Enter Your Numbers")
num1 = st.number_input("Enter the first number:", step=1.0)
num2 = st.number_input("Enter the second number:", step=1.0)
# Dropdown menu for operation selection
operation = st.selectbox("Select an Operation:", ["Addition",
"Subtraction", "Multiplication", "Division"])
# Perform the operation based on user input
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of division is: {result}")
        else:
            st.error("Division by zero is not allowed!")
