#!/usr/bin/env python3
from credentials import api_key, api_secret
from settings import coin, stbCoin, amount
from binance.um_futures import UMFutures
from colorama import init
from termcolor import colored

init()
client = UMFutures(key=api_key, secret=api_secret)

coinPair = f"{coin}{stbCoin}"

mar = input(colored(
    f"{coinPair} margin type 1 - crossed, 2 - isolated:", "yellow"
))

if mar == "1":
    marginT = "CROSSED"
elif mar == "2":
    marginT = "ISOLATED"
else:
    print(colored("Wrong number, try again!", "red"))

try:
    response = client.change_margin_type(
        symbol=coinPair, marginType=marginT, recvWindow=6000
    )
except Exception as e:
    print(e)

print(colored(f"{coinPair} margin type changed to:", "magenta"), colored(
    marginT, "yellow"))
