import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Hello streamlit")
st.write("Welcome to the new dashboard")
st.write("Beginning the dashboard")

df1 = pd.read_csv("1a_median_price_transposed.csv")
df2 = pd.read_csv("1c_ratio_transposed.csv")

st.bar_chart(df1)
st.line_chart(df2)

#st.dataframe(df1.head(10))
#st.table(df2.head(10))