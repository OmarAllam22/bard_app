import streamlit as st
from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "cgg3MEvV_ukgzyDk-uKvPGm-lbYvnR8-BAgZM5FrveeNvETUuPqdAEPkgAkHcSLHOEOciw.",
    "__Secure-1PSIDTS": "sidts-CjIBNiGH7ohPgPcfmAfy8hetTvRPsFG7I2RSn-bDRp4z9qNCl51-RomHbzaqlR5CtbmtGxAA",
    "__Secure-1PSIDCC": "ACA-OxNpjujSxhYuBsvNuxge4A3i0ACUUGC4NC19YaS5SGXwNI4tSeDjIcjWv27hvYyLDNiSu3z9"
}


bard = BardCookies(cookie_dict=cookie_dict)

# Define the Streamlit app
st.title("Propositional Logic Question Answering")

# Get the user's question
question = st.text_input("Enter a propositional logic question:", "")

# Get the answer from Bard
answer = bard.get_answer(question)['content']

# Display the answer to the user
st.write("Answer:", answer)
