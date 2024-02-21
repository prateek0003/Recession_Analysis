# -*- coding: utf-8 -*-
"""India_GDP_Forecast

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JtDqQGyX2BSKf3yxXvLsP5wFZpl5eT2k
"""

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

# Read data from excel file
data = pd.read_excel("/content/sample_data/India.xlsx")

# Selecting the data for ARIMA model
india_gdp = data[['Year', 'GDP']]
india_gdp.set_index('Year', inplace=True)

# Fit the ARIMA model
model = ARIMA(india_gdp, order=(5,1,0))
model_fit = model.fit()

# Forecasting for the next 5 years
forecast = model_fit.forecast(steps=5)

# Plotting the forecast
plt.figure(figsize=(10, 6))
plt.plot(india_gdp.index, india_gdp['GDP'], label='Historical GDP')
plt.plot(range(2023, 2028), forecast, color='red', linestyle='--', label='Forecasted GDP')
plt.title('India GDP Forecast 2023-2027')
plt.xlabel('Year')
plt.ylabel('GDP in Billion USD')
plt.legend()
plt.show()

# Output the forecast values
print('Forecasted GDP values for 2023 to 2027 in Billion USD :\n',forecast)