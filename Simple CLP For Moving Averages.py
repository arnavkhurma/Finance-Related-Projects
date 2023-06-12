# Simple Command Line Program
# for calculating Moving 
# Averages, and Comparing to
# Adjusted Close values.
# 
# Author: Arnav Khurma
# Version: 2023-01-09

# Importing necessary libraries:
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import pandas_datareader as pdr
yf.pdr_override()

# Getting stock user input
stock = input("Enter a stock ticker: ")
print("You have selected", stock + ".")

startyear = 2021
startmonth = 1
startday = 1

# Dates:
startdate = dt.datetime(startyear, startmonth, startday)
# print(startdate)

enddate = dt.datetime.now()
# print(enddate)

dataframe = yf.download(stock, start=startdate, end=enddate)
# print(dataframe)

# Moving Average
days = int(input("Days for Calculating Moving Average: "))
sma_string = "Sma_" + str(days)
# print(sma_string)

dataframe[sma_string] = dataframe["Adj Close"].rolling(window = days).mean()
dataframe = dataframe.iloc[days:]
# print(dataframe)

counter_higher = 0
counter_lower = 0
# Now we check if the Moving Average is above the close.
for value in dataframe.index:
    current_adjusted_close = dataframe["Adj Close"][value]
    current_moving_average = dataframe[sma_string][value]
    # print(current_adjusted_close, current_moving_average)
    if (current_adjusted_close > current_moving_average):
        # print("The close is higher on", value)
        counter_higher += 1
    else:
        # print("The close is lower on", value)
        counter_lower += 1
print("The close was higher on", str(counter_higher), "occasion(s), and the close was lower on", str(counter_lower), "occasion(s)")