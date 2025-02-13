import datetime
import time
from scipy.special import logsumexp,log1p,xlogy
import ccxt
import numpy as np
import pandas as pd
from dateutil.parser import parse
from scipy.optimize import curve_fit
import math


def log_func(x, a, b, c):
    """Logarithmic function for curve fitting."""
    
    r=a * np.log(b + x) + c
    # r=a * logsumexp(b + x) + c
    # r=xlogy(a,b+x)+c
    # print(type(r))
    return r


def get_data(file_path,update_permission=False):
    "update permission=False => don't update data anyways"
    """
    Load and preprocess data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Processed data.
        np.ndarray: Fitted Y data.
    """
    raw_data = pd.read_csv(file_path)
   
  
    raw_data["Date"] = pd.to_datetime(raw_data["Date"])
    # print(raw_data["Date"])
    # # Calculate the difference in days between the last date and today
    # diff_days = (pd.Timestamp.today() - raw_data["Date"].max()).days


    raw_data = raw_data[raw_data["Value"] > 0]
    # print(raw_data)
    # # Prepare data for curve fitting
    xdata = np.array([x + 1 for x in range(len(raw_data))])
    
    ydata =np.log(raw_data["Value"])
    # ydata =log1p(raw_data["Value"])
    # ydata =logsumexp(raw_data["Value"])
    # ydata =raw_data["Value"]

    # print(f'xdata={xdata}')
    # print(f'ydata={ydata}')
  
    #  Fit the logarithmic curve
    popt, _ = curve_fit(log_func, xdata, ydata,maxfev=100000)
    return raw_data, popt
# # get_data("data/bitcoin_data.csv")
# print("--------------------------------------------------------------------")
# get_data("data/newbtcdata.csv")

