# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:56:41 2016

@author: hp
"""

import Quandl
import matplotlib.pyplot as plt

data= Quandl.get(['YAHOO/ASX_FAR_AX','FRED/DCOILBRENTEU'],
trim_start='2014-10', authtoken='kAvz8yJfRpGdCoH2qRTx')

#%%

data2 =data.drop(data.columns[[0,1,2,4,5]], axis=1)
data2.columns = ['FAR Price', 'Brent Crude Price']
data2.plot()

#%%
plt.style.use('bmh')

data2.plot(secondary_y=['Brent Crude Price'])