import streamlit as st
import requests
import pandas as pd
import datetime






st.title('Delete Expense Entry')
del_expense_form = st.form(key='del_expense_form',clear_on_submit=True)
expense_id = del_expense_form.text_input(label='ID You Want to Delete')
del_submit_button = del_expense_form.form_submit_button(label='Submit')


if expense_id != "":
    
    del_url = 'http://127.0.0.1:5000/expense/{}'.format(expense_id)
    requests.delete(del_url)
    st.success('Item Succsesfuly Deleted!', icon="✅")

else:
    st.error('Please Check ID Number', icon="🚨")