import streamlit as st
# Function to convert temperatures
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
        else:
            return value
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value

# Streamlit UI setup
st.title('Temperature Converter')

# Input field for temperature
temp_value = st.number_input('Enter temperature value:', value=0)

# Dropdowns for selecting units
from_unit = st.selectbox('Convert from', ['Celsius', 'Fahrenheit', 'Kelvin'])
to_unit = st.selectbox('Convert to', ['Celsius', 'Fahrenheit', 'Kelvin'])

# Button to calculate the result
if st.button('Convert'):
    result = convert_temperature(temp_value, from_unit, to_unit)
    st.write(f"{temp_value} {from_unit} is equal to {result:.2f} {to_unit}")

