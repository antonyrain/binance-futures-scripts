#!/usr/bin/env python3
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
mark_price = res['markPrice']
print("*" * 40)
print(colored(f"{coinPair} market price: ", "yellow"), mark_price)
