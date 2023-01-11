import streamlit as st 
import pandas as pd
import datetime
import requests
import calendar
import plotly.express as px



#st.title('My Expanses')


#form = st.form(key='my-form')
#name = form.text_input('Enter your name')
#submit = form.form_submit_button('Submit')

page_title = 'Income & Expense Tracker'
layout = 'wide'

st.set_page_config(page_title=page_title,layout=layout)
st.title(page_title)





r = requests.get('http://127.0.0.1:5000/income')

data = r.json()
df1 = pd.json_normalize(data)
df1['date'] = df1['date'].astype('datetime64[ns]')
df1['month'] = df1['date'].dt.month
df2 = df1.groupby(['category','month'])['amount'].sum()
df2 = pd.DataFrame(df2).reset_index()
df2 = df2.pivot(index='category', columns='month', values='amount')
df2 = df2.rename(columns={1:'January',2: 'February', 3:'March',4: 'April',5:'May',6:"June",7:'July',8:"August",9:"September",10:"October",11:'November',12:'December'})

income_total = df1.groupby(['month'])['amount'].sum()
income_total = pd.DataFrame(income_total)
income_total= income_total.reset_index()
income_total['Month Name'] = income_total['month'].apply(lambda x: calendar.month_abbr[x])
fig = px.line(income_total, x="Month Name", y="amount", title='Income')



st.title('Income')
st.plotly_chart(fig)
st.dataframe(df2)




s = requests.get('http://127.0.0.1:5000/expense')

exp_data = s.json()
df1_exp = pd.json_normalize(exp_data)
df1_exp['date'] = df1_exp['date'].astype('datetime64[ns]')
df1_exp['month'] = df1_exp['date'].dt.month
df2_exp = df1_exp.groupby(['category','month'])['amount'].sum()
df2_exp = pd.DataFrame(df2_exp).reset_index()
df2_exp = df2_exp.pivot(index='category', columns='month', values='amount')
df2_exp = df2_exp.rename(columns={1:'January',2: 'February', 3:'March',4: 'April',5:'May',6:"June",7:'July',8:"August",9:"September",10:"October",11:'November',12:'December'})


exp_total = df1_exp.groupby(['month'])['amount'].sum()
exp_total = pd.DataFrame(exp_total)
exp_total= exp_total.reset_index()
exp_total['Month Name'] = exp_total['month'].apply(lambda x: calendar.month_abbr[x])
exp_fig = px.line(exp_total, x="Month Name", y="amount", title='Expense')


inc_pie = df1.groupby(['category'])['amount'].sum()
inc_pie = pd.DataFrame(inc_pie)
inc_pie = inc_pie.reset_index()
exp_fig_pie = px.pie(inc_pie, values='amount', names='category')



st.title('Expense')
col1, col2 = st.columns(2)
col1.plotly_chart(exp_fig,use_container_width = True)
col2.plotly_chart(exp_fig_pie,use_container_width = True)

st.dataframe(df2_exp)