import streamlit as st
import requests
import pandas as pd
import datetime

st.title('Add Income')






add_income_form = st.form(key='add_income_form',clear_on_submit=True)
income_date = add_income_form.date_input("Transaction Date")
income_category = add_income_form.text_input("Category")
income_vendor = add_income_form.text_input(label='Vendor')
income_amount= add_income_form.number_input('Transaction Amount')
income_description = add_income_form.text_input(label='Description')
submit_button = add_income_form.form_submit_button(label='Submit')




if income_date and income_vendor and income_amount and income_description != "":


    post_url = 'http://127.0.0.1:5000/income'

    income_data = {'amount': income_amount,
    'date': str(income_date),
    'description': income_description,
    'vendor': income_vendor,
    'category':income_category}



    requests.post(post_url, json=income_data)

    st.success('This is a success message!', icon="✅")
    

else:
    st.error('Please Fill in Information above', icon="🚨")



r = requests.get('http://127.0.0.1:5000/income')
data = r.json()
df1 = pd.json_normalize(data)

if len(df1) == 0:
    pass

else: 
    df1['date'] = df1['date'].astype('datetime64[ns]')
    df1 = df1[["id","date",'category',"amount","description","vendor"]]
    df1 = df1.rename(columns={'id':'ID','date': 'Date', 'category':'Category','amount': 'Amount','description': 'Description','vendor': 'Vendor'})
    #df1 = df1[df1['date'].dt.month == 1]
    #df1 = df1[df1['date'].dt.year == 2023]
    st.dataframe(df1) 
    #st.table(df1)

 











