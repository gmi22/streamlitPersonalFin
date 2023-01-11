import streamlit as st
import requests
import pandas as pd
import datetime



st.title('Delete Income Entry')
del_income_form = st.form(key='del_income_form',clear_on_submit=True)
income_id = del_income_form.text_input(label='ID You Want to Delete')
del_submit_button = del_income_form.form_submit_button(label='Submit')

if income_id != "":
    
    del_url = 'http://127.0.0.1:5000/income/{}'.format(income_id)
    requests.delete(del_url)
    income_id = 0
    st.success('Item Succsesfuly Deleted!', icon="✅")

else:
    st.error('Please Check ID Number', icon="🚨")