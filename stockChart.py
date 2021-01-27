# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 08:52:22 2021

@author: carol
"""

import yfinance as yf
import  streamlit as st
import pandas as pd

st.write("""
# Simple stock Price App


Shown something

""")

tickerSimbol ='GOOGL'

tickerData = yf.Ticker(tickerSimbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-1-26')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)