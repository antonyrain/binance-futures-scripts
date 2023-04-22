#!/usr/bin/env python3
from credentials import api_key, api_secret
from settings import coin, stbCoin, amount
from binance.um_futures import UMFutures
from colorama import init
from termcolor import colored

init()
client = UMFutures(key=api_key, secret=api_secret)

coinPair = f"{coin}{stbCoin}"

lev = input(colored(f"{coinPair} leverage: ", "yellow"))

try:
    response = client.change_leverage(
        symbol=coinPair,
        leverage=lev,
        recvWindow=6000
    )
except Exception as e:
    print(e)

print(colored(f"{coinPair} leverage changed to:", "magenta"), colored(lev, "yellow"))
