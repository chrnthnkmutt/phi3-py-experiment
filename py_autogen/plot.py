# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 11:10:28 2024

@author: boatc
"""

import matplotlib.pyplot as plt

# Use the Yahoo Finance API to retrieve the YTD stock prices for both NVDA and TESLA
nvda_ytd = get_stock_price('NVDA', start='01/01/2023')
tesla_ytd = get_stock_price('TESLA', start='01/01/2023')

# Create a chart to display the YTD stock price changes for both NVDA and TESLA
fig, axs = plt.subplots(2, 1, figsize=(15,6))
axs[0].plot(nvda_ytd['Date'], nvda_ytd['Close'])
axs[0].set_title('NVDA YTD Stock Price')
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Price')

axs[1].plot(tesla_ytd['Date'], tesla_ytd['Close'])
axs[1].set_title('TESLA YTD Stock Price')
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Price')

plt.show()