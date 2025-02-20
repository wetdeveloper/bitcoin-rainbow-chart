import datetime
import time

import ccxt
import numpy as np
import pandas as pd
from dateutil.parser import parse
from scipy.optimize import curve_fit
import math


def validcsvmaker(
csvfile="data/ADAUSD.csv",keep_col=['Date','Value']):


    oldcsvfile=pd.read_csv(csvfile)
    oldcsvfile= oldcsvfile[keep_col]
    #removing time for Date column
    oldcsvfile['Date'] = pd.to_datetime(oldcsvfile['Date']).dt.date
     
    #sort csv data
    oldcsvfile=oldcsvfile.sort_values(by=["Date"], ascending=True)
    oldcsvfile.to_csv('data/newadadata.csv',index=False) #index=False =>you won't have indices per row like 0,1,2,3 in new

# validcsvmaker()
