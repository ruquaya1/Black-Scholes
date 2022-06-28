# Black Scholes Merton Model
This mathematical equation estimates the theoretical value of derivatives based on other investment instruments, taking into account the impact of time and other risk factors. 
##### The Black-Scholes model requires five input variables: 
- strike price of an option 
- current stock price 
- time to expiration 
- risk-free rate
- volatility.

##### The standard BSM model is only used to price European options, as it does not take into account that American options could be exercised before the expiration date.

### Implementing the Black-Scholes Formula

##### Import Libraries
```
import numpy as np
from scipy.stats import norm
```

##### Define variables
```
r = 0.01     #risk-free rate
S = 30       #current stock price
K = 40       #strike price
T = 240/365  #time to expiration
sigma = 0.30 #volatility
```

```
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
```

##### The Black-Scholes model makes certain assumptions:

- No dividends are paid out during the life of the option.
- Markets are random (i.e., market movements cannot be predicted).
- There are no transaction costs in buying the option.
- The risk-free rate and volatility of the underlying asset are known and constant.
- The returns on the underlying asset are log-normally distributed.
- The option is European and can only be exercised at expiration.

##### Drawbacks of the Black-Scholes Model

- The Black-Scholes model is only used to price European options and does not take into account that American options could be exercised before the expiration date.
- The model assumes dividends and risk-free rates are constant, but this may not be true in reality.
- The model also assumes volatility remains constant over the option's life, which is not the case because volatility fluctuates with the level of supply and demand.
- Other assumptions—that there are no transaction costs or taxes; that the risk-free interest rate is constant for all maturities; that short selling of securities with use of proceeds is permitted; and that there are no risk-less arbitrage opportunities—can lead to prices that deviate from the real world's.
