#!/usr/bin/env python3
from credentials import api_key, api_secret
from binance.um_futures import UMFutures
from colorama import init
from termcolor import colored

init()
client = UMFutures(key=api_key, secret=api_secret)

def get_balance():
    print("*" * 40)
    usdt_balance = client.balance()[6]["balance"]
    print(colored("USDT Balance: ", "yellow" ), colored(usdt_balance, "green"))
    busd_balance = client.balance()[8]["balance"]
    print(colored("BUSD Balance: ", "yellow" ), colored(busd_balance, "green")) 
    bnb_balance = client.balance()[3]["balance"]
    print(colored("BNB Balance: ", "yellow" ), colored(bnb_balance, "green"))


get_balance()
