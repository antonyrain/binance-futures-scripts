#!/usr/bin/env python3                                                                                                                
from credentials import api_key, api_secret
from settings import coin, stbCoin, amount
from decimal import Decimal
from binance.um_futures import UMFutures
from colorama import init
from termcolor import colored


init()
client = UMFutures(key=api_key, secret=api_secret)
 
coinPair = f"{coin}{stbCoin}"
num = input(colored("The number of 15min candlesticks to calculate: ", "yellow"))
if num == "":
    num = 14
else:
    num = int(num)
num_ = num + 1


print("=" * 40)
print(colored(f"Last, {num} bars", "yellow")) 
 
res = client.mark_price_klines(symbol=coinPair, interval="15m", limit=num_)
prevClose = float(res[0][4])
gain = 0
loss = 0

# (2 / (Number of Periods + 1)
multi = (2 / num + 1)

i = 1
while i != num_:
    currentClose = float(res[i][4])
    change = currentClose - prevClose
    if change > 0:
        gain += change 
    elif change < 0:
        loss += abs(change)
    else:
        pass
    prevClose = currentClose
    i += 1

avgGain = gain / num
avgLoss = loss / num
rs = avgGain / avgLoss
rsi = 100 - (100 / (1 + rs))
print(colored("RSI: ", "yellow"), colored(rsi, "magenta"))
