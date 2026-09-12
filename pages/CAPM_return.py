# importing libraries
import capm_functions
import datetime

import streamlit as st
import pandas as pd
import yfinance as yf 
import pandas_datareader.data as web 


st.set_page_config(page_title="CAPM", 
    page_icon="chart_with_upwards_trend",
    layout="wide")

st.title("Capital Asset Pricing Model")

# getting inputs from user

col1, col2= st.columns([1,1])
with col1:
    stocks_list=st.multiselect("Choose 4 stocks", ("TSLA","AAPL","NFLX","MSFT","MGM","AMZN","NVDA","GOOGL"),["TSLA","AAPL","AMZN","GOOGL"])

with col2:
    year=st.number_input("Number of years",1,10)

# downloading data for SP 500
end=datetime.date.today()
start = datetime.date(
    datetime.date.today().year - year,
    datetime.date.today().month,
    datetime.date.today().day
)

SP500=web.DataReader(["SP500"],"fred",start,end)
print(SP500.head())

stocks_df=pd.DataFrame()


for stock in stocks_list:
    data=yf.download(stock, period=f'{year}y')
    print(data.head())
    stocks_df[f'{stock}']=data['Close']


# Reset and clean stocks_df
stocks_df.reset_index(inplace=True)
stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])

# Reset and clean SP500
SP500 = SP500.reset_index()
SP500.rename(columns={'DATE':'Date'}, inplace=True)
SP500['Date'] = pd.to_datetime(SP500['Date'])

# Merge
stocks_df = pd.merge(stocks_df, SP500[['Date','SP500']], on="Date", how="inner")

print(stocks_df.head())

col1,col2=st.columns([1,1])

with col1:
    st.markdown("### Dataframe head")
    st.dataframe(stocks_df.head(),use_container_width=True)

with col2:
    st.markdown("### Dataframe tail")
    st.dataframe(stocks_df.tail(),use_container_width=True)

col1,col2=st.columns([1,1])
with col1:
    st.markdown("Price of all the stocks")
    st.plotly_chart(capm_functions.interactive_plot(stocks_df), use_container_width=True)

with col2:
    st.markdown("Price of all the stocks (After normalizing)")
    st.plotly_chart(capm_functions.interactive_plot(capm_functions.normalize(stocks_df)), use_container_width=True)

stocks_daily_return=capm_functions.daily_return(stocks_df)
print(stocks_daily_return.head())

beta={}
alpha={}

for i in stocks_daily_return.columns:
    if i != 'Date' and i != 'SP500':
        b, a = capm_functions.calculate_beta(stocks_daily_return, i)
        beta[i] = b
        alpha[i] = a
        print(beta, alpha)

beta_df = pd.DataFrame(columns=['Stock', 'Beta Value'])
beta_df['Stock'] = beta.keys()
beta_df['Beta Value'] = [str(round(i, 2)) for i in beta.values()]

with col1:
    st.markdown("### Calculated Beta Value")
    st.dataframe(beta_df, use_container_width=True)

rf = 0
rm = stocks_daily_return['SP500'].mean() * 252

return_df = pd.DataFrame()
return_value = []
for stock, value in beta.items():
  return_value.append(str(round(rf + (value * (rm - rf)), 2)))

return_df['Stock'] = stocks_list
return_df['Return Value'] = return_value

with col2:
    st.markdown('### Calculated return using CAPM')

    st.dataframe(return_df,use_container_width=2)
    
















