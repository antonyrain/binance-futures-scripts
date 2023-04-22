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
num = input(colored("The number of 15min bars to show: ", "yellow"))
if num == "":
    num = 16 

print("=" * 40)
print(colored(f"Last, {num} bars", "yellow"))

sticks_array = []

res = client.klines(symbol=coinPair, interval="15m", limit=num)

for x in res:
    openKline = float(x[1])
    closeKline = float(x[4])
    vol = float(x[5])
    if openKline < closeKline:
        stars = round(vol / 10)
        if stars > 70:
            stars = 59
            print(colored("#" * stars + "more", "green"))
        else:
            print(colored("#" * stars, "green"))
    if openKline > closeKline:
        stars = round(vol / 10)
        if stars > 70:
            stars = 59
            print(colored("#" * stars + "more", "green"))
        else:  
            print(colored("#" * stars, "red"))
print(colored("Actual", "yellow"))
print("=" * 40)
