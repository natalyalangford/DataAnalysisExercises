import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    """
    Creates a scatter plot using "epa-sea-level.csv"

    Returns:
        Axes: Returns the scatter plot that was created
    """
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    lin1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = pd.Series([int(i) for i in range(1880, 2051)])
    y1 = lin1.slope * x1 + lin1.intercept
    plt.plot(x1, y1)

    # Create second line of best fit
    df_2000 = df.loc[df["Year"] >= 2000]
    lin2 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    x2 = pd.Series([int(i) for i in range(2000, 2051)])
    y2 = lin2.slope * x2 + lin2.intercept
    plt.plot(x2, y2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()