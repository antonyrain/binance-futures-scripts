#!/usr/bin/env python3
from credentials import api_key, api_secret
from binance.um_futures import UMFutures
from settings import coin, stbCoin
from colorama import init
from termcolor import colored

init()
client = UMFutures(key=api_key, secret=api_secret)
#coin = input("Coin: ").upper()
coinPair = f"{coin}{stbCoin}"

resp = client.get_position_risk(symbol=coinPair)
print("*" * 40)
print(colored("Long position entry price: ", "green"), colored(resp[0]['entryPrice'], "yellow"))
print(colored("Short position entry price: ", "red"), colored(resp[1]['entryPrice'], "yellow"))
res = client.mark_price(coinPair)
mark_price = res['markPrice']
print(colored(f"{coinPair} market price: ", "yellow"), mark_price)
