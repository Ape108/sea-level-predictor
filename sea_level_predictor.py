import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5)
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years = np.arange(1880, 2051)

    line = slope * years + intercept

    plt.plot(years, line, 'r', label=f'Line of best fit (slope: {slope:.2f})')

    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    recent_slope, recent_intercept, r_value, p_value, std_err = linregress(
        recent_data['Year'], recent_data['CSIRO Adjusted Sea Level']
    )
    recent_years = np.arange(2000, 2051)
    recent_line = recent_slope * recent_years + recent_intercept
    plt.plot(recent_years, recent_line, 'g', label=f'Line of best fit from 2000 (slope: {recent_slope:.2f})')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()