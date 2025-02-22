import streamlit as st
import random

# Function to simulate exchange rate for testing
def get_exchange_rate(from_currency, to_currency):
    # Mock exchange rates between USD, EUR, GBP, and PKR for demonstration
    mock_rates = {
        ('USD', 'EUR'): 0.85,
        ('USD', 'GBP'): 0.75,
        ('USD', 'PKR'): 286.5,  # Example exchange rate
        ('EUR', 'USD'): 1.18,
        ('EUR', 'GBP'): 0.88,
        ('EUR', 'PKR'): 338.2,  # Example exchange rate
        ('GBP', 'USD'): 1.33,
        ('GBP', 'EUR'): 1.14,
        ('GBP', 'PKR'): 379.4,  # Example exchange rate
        ('PKR', 'USD'): 1 / 286.5,
        ('PKR', 'EUR'): 1 / 338.2,
        ('PKR', 'GBP'): 1 / 379.4
    }

    # Return a mock rate or random rate if not in the mock dictionary
    return mock_rates.get((from_currency, to_currency), random.uniform(0.5, 1.5))

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    if exchange_rate:
        return amount * exchange_rate
    return None

# Streamlit UI setup
st.title('Currency Converter')

# Dropdown for selecting from currency
from_currency = st.selectbox('From currency', ['USD', 'EUR', 'GBP', 'PKR', 'INR', 'JPY', 'AUD', 'CAD', 'CHF'])

# Dropdown for selecting to currency
to_currency = st.selectbox('To currency', ['USD', 'EUR', 'GBP', 'PKR', 'INR', 'JPY', 'AUD', 'CAD', 'CHF'])

# Input field for amount
amount = st.number_input('Amount to convert', min_value=0.0, step=0.01)

# Button to perform conversion with a unique key
if st.button('Convert', key="convert_button"):
    if from_currency != to_currency:
        result = convert_currency(amount, from_currency, to_currency)
        if result:
            st.write(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
        else:
            st.write("Sorry, we couldn't get the exchange rate. Please try again later.")
    else:
        st.write("Please select different currencies to convert.")


