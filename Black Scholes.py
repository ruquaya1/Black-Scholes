#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Implementing the Black-Scholes formula


# In[9]:


import numpy as np
from scipy.stats import norm


# In[10]:


#define variables
r = 0.01 #Interest Rate
S = 30 #underlying price
K = 40 #strike price
T = 240/365 #time
sigma = 0.30


# In[15]:


def blackscholes(r, S, K, T, sigma, type="C"):
    "Calculate BS option price for a call/put"
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    try:
        if type == "C":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "P":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Please confirm all option parameters above!!!")
        
print("Option Price is:", round(blackscholes(r, S, K, T, sigma, type="C"), 2))        
        
            


# In[ ]:




