#!/usr/bin/env python3
import time
from credentials import api_key, api_secret
from settings import coin, stbCoin
from binance.um_futures import UMFutures
from colorama import init
from termcolor import colored

init()
client = UMFutures(key=api_key, secret=api_secret)
# coin = input("Coin: ").upper()
coinPair = f"{coin}{stbCoin}"
res = client.mark_price(coinPair)
temp = round(float(res['markPrice']), 1)

print("*" * 40)
print(colored(f"{coinPair} market price changes 1 min", "magenta"))
for i in range(60):
    res = client.mark_price(coinPair)
    mark_price = round(float(res['markPrice']), 1)
    if mark_price > temp:
        print(colored("   " + f"{mark_price}", "green"))
    elif mark_price < temp:
        print(colored("   " + f"{mark_price}", "red"))
    else:
        print("   " + str(mark_price))
    temp = mark_price
    time.sleep(1)
