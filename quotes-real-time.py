from googlefinance import getQuotes
from datetime import datetime as dt

quotes = ['AAPL', 'GOOG', 'MSFT', 'TSLA'] ## Here are the quotes desired.
prices = [0,0,0,0] ## Intializes the prices list.
prevtime = [dt.utcnow().minute, dt.utcnow().second, dt.utcnow().microsecond]  ## Our comparitor
for i in range(20):
    time = [dt.utcnow().minute, dt.utcnow().second, dt.utcnow().microsecond]  ## 'Present' time
    if time[2] > prevtime[2] or time[1] > prevtime[1]: ## Compares our time
    	q = getQuotes(quotes)
    	for j in range(len(q)):
    		prices[j] = q[j]['LastTradePrice']
    	print(prices)
    	prevtime = time