
import streamlit as st 
import yfinance as fn 

st.write("""# Welcome to a new project""")
st.title("Stock Market App with Streamlit")
st.header("Simple Data Science web App")
st.sidebar.header("Code with me")

def get_ticker(name):
    company = fn.Ticker(name)
    return company

c1 = get_ticker("AAPL")
c2 = get_ticker("MSFT")
c3 = get_ticker("TSLA")

apple =fn.download("AAPL",start="2024-1-1",end="2024-1-3")
microsoft =fn.download("MSFT",start="2024-1-1",end="2024-1-3")
tsla =fn.download("TSLA",start="2024-1-1",end="2024-1-3")

#Fetching historical data
data1 = c1.history(period="3mo")
data2 = c2.history(period="3mo")
data3 = c3.history(period="3mo")

#Markdown 
st.write("""### Apple""")
st.write(c1.info['longBusinessSummary'])
st.write(apple)
st.line_chart(data1.values)

st.write("""### MSFT""")
st.write(c2.info['longBusinessSummary'])
st.write(microsoft)
st.line_chart(data2.values)

st.write("""### TSLA""")
st.write(c3.info['longBusinessSummary'])
st.write(tsla)
st.line_chart(data3.values)