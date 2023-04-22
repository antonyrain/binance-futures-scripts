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
num = input(colored("Number of 15min bars to show: ", "yellow"))
if num == "":
    num = 16 

print("=" * 40)
print(colored(f"Last, {num} bars", "yellow")) 
sticks_array = []
 
res = client.klines(symbol=coinPair, interval="15m", limit=num)

volGreen = 0.0
volRed = 0.0

for x in res:
    openKline = float(x[1])
    closeKline = float(x[4])
    vol = float(x[5])
    if openKline < closeKline:
        volGreen = volGreen + vol
        # print(colored(volGreen, "green"))
    if openKline > closeKline:
        volRed = volRed + vol
        # print(colored(volRed, "red"))
print(colored(f"{coin} sum volumes: ", "magenta"))
print(colored(volGreen, "green"))
print(colored(volRed, "red"))
if volGreen < volRed:
    print(colored("Green", "green") + " < " + colored("Red", "red"))
    print(colored(f"Growth coefficient: {volGreen / volRed}", "magenta"))
elif volGreen > volRed:
    print(colored("Green", "green") + " > " + colored("Red", "red"))
    print(colored(f"Growth coefficient: {volGreen / volRed}", "magenta"))
else:
    print(colored("Equal", "magenta"))
