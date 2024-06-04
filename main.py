import tkinter as tk
from tkinter import simpledialog
import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch and plot the data
def fetch_and_plot_data(start_year):
    # Define the indicators for industrialization, inflation, and exchange rate
    indicators = {
        'NV.IND.MANF.ZS': 'Manufacturing, value added (% of GDP)',
        'FP.CPI.TOTL.ZG': 'Inflation, consumer prices (annual %)',
        'PA.NUS.FCRF': 'Official exchange rate (LCU per US$, period average)'
    }

    # Retrieve data for Nepal
    data = wb.data.DataFrame(indicators, economy='NPL', time=range(start_year, 2024))  # from start_year to most recent year

    # Transpose the data for better readability
    data = data.transpose()

    # Rename the columns for easier understanding
    data.columns = ['Inflation', 'Manufacturing', 'Exchange Rate']

    # Convert the index to datetime format, stripping the "YR" prefix
    data.index = pd.to_datetime(data.index.str.replace('YR', ''), format='%Y')

    # Create subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 18), sharex=True)

    # Plot Manufacturing
    color = 'tab:blue'
    ax1.set_ylabel('Manufacturing (% of GDP)', color=color)
    ax1.plot(data.index, data['Manufacturing'], color=color, marker='o', label='Manufacturing')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='upper left')
    ax1.set_title('Manufacturing, Inflation Rates, and Exchange Rate of Nepal')

    # Plot Inflation
    color = 'tab:red'
    ax2.set_ylabel('Inflation rate (%)', color=color)
    ax2.plot(data.index, data['Inflation'], color=color, marker='x', label='Inflation')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend(loc='upper left')

    # Plot Exchange Rate
    color = 'tab:green'
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Exchange Rate (NPR per USD)', color=color)
    ax3.plot(data.index, data['Exchange Rate'], color=color, marker='s', label='Exchange Rate (NPR/USD)')
    ax3.tick_params(axis='y', labelcolor=color)
    ax3.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

# Function to prompt user for input and call fetch_and_plot_data
def get_start_year():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    start_year = simpledialog.askinteger("Input", "Enter the starting year:", minvalue=1960, maxvalue=2024)
    if start_year:
        fetch_and_plot_data(start_year)
    root.destroy()

# Run the Tkinter interface to get the starting year
get_start_year()
