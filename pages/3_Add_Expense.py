import streamlit as st
import requests
import pandas as pd
import datetime



st.title('Add Expenses')


add_expense_form = st.form(key='add_expense_form',clear_on_submit=True)
expense_date = add_expense_form.date_input("Transaction Date")
expense_category = add_expense_form.text_input("Category")
expense_vendor = add_expense_form.text_input(label='Vendor')
expense_amount= add_expense_form.number_input('Transaction Amount')
expense_description = add_expense_form.text_input(label='Description')
submit_button = add_expense_form.form_submit_button(label='Submit')

if expense_date and expense_vendor and expense_amount and expense_description != "":


    post_url = 'http://127.0.0.1:5000/expense'

    expense_data = {'amount': expense_amount,
    'date': str(expense_date),
    'description': expense_description,
    'vendor': expense_vendor,
    'category':expense_category}



    requests.post(post_url, json=expense_data)

    st.success('This is a success message!', icon="✅")

else:
    st.error('Please Fill in Information above', icon="🚨")




r = requests.get('http://127.0.0.1:5000/expense')
data = r.json()
df1 = pd.json_normalize(data)

if len(df1) == 0:
    pass

else:

    df1['date'] = df1['date'].astype('datetime64[ns]')
    df1 = df1[["id","date","category","amount","description","vendor"]]
    df1 = df1.rename(columns={'id':'ID','date': 'Date','category':"Category" ,'amount': 'Amount','description': 'Description','vendor': 'Vendor'})
    st.dataframe(df1)



