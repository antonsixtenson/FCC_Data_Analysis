import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], s=5)
    years = list(range(1880, 2051))
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    line = [res.slope*i + res.intercept for i in years]

    # Create second line of best fit
    years_later = list(range(2000, 2051))
    df_later = df[df["Year"] >= 2000]
    res_later = linregress(df_later["Year"], df_later["CSIRO Adjusted Sea Level"])
    line_later = [res_later.slope*i + res_later.intercept for i in years_later]

    ax.plot(years, line, "g", label="1880-2050")
    ax.plot(years_later, line_later, "r", label="2000-2050")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    


    

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
