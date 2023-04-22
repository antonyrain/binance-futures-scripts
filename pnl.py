#!/usr/bin/env python3
from credentials import api_key, api_secret
from settings import coin, stbCoin, amount
from decimal import Decimal
from binance.um_futures import UMFutures
from colorama import init
from termcolor import colored

init()
client = UMFutures(key=api_key, secret=api_secret)

coinPair_1 = "ETHBUSD"
coinPair_2 = "BTCBUSD"

info = client.exchange_info()
for sym in info["symbols"]:
    if sym["pair"] == coinPair_1:
        tickSize = sym["filters"][0]['tickSize']

def round_step_size(quantity, size):
    quantity = Decimal(quantity)
    return float(quantity - quantity % Decimal(size))


print("*" * 40)
res = client.get_position_risk(symbol=coinPair_1)
bp = res[0]['entryPrice']
entry_price = round_step_size(bp, tickSize)
print(colored(f"{coinPair_1} Long position Entry price: ", "magenta"), entry_price)

bp = res[1]['entryPrice']
entry_price = round_step_size(bp, tickSize)
print(colored(f"{coinPair_1} Short position Entry price: ", "magenta"), entry_price)

resp = client.mark_price(coinPair_1)
mk = float(resp['markPrice'])
mark_price = round_step_size(mk, tickSize)
print(colored(f"{coinPair_1} Mark price: ", "yellow"), mark_price)

try:
    res = client.get_position_risk(symbol=coinPair_1)
    pnl = res[0]['unRealizedProfit']
    long_side_pnl = round_step_size(pnl, tickSize)
    print(f"{coinPair_1} Long Side PNL: ", colored(long_side_pnl, "green"))
except:
    print("Zero")

try:
    res = client.get_position_risk(symbol=coinPair_1)
    pnl = res[1]['unRealizedProfit']
    short_side_pnl = round_step_size(pnl, tickSize)
    print(f"{coinPair_1} Short Side PNL: ", colored(short_side_pnl, "green"))
except:
    print("Zero")

print("*" * 40)
res = client.get_position_risk(symbol=coinPair_2)
bp = res[0]['entryPrice']
entry_price = round_step_size(bp, tickSize)
print(colored(f"{coinPair_2} Long position Entry price: ", "magenta"), entry_price)

bp = res[1]['entryPrice']
entry_price = round_step_size(bp, tickSize)
print(colored(f"{coinPair_2} Short position Entry price: ", "magenta"), entry_price)

resp = client.mark_price(coinPair_2)
mk = float(resp['markPrice'])
mark_price = round_step_size(mk, tickSize)
print(colored(f"{coinPair_2} Mark price: ", "yellow"), mark_price)

try:
    res = client.get_position_risk(symbol=coinPair_2)
    pnl = res[0]['unRealizedProfit']
    long_side_pnl = round_step_size(pnl, tickSize)
    print(f"{coinPair_2} Long Side PNL: ", colored(long_side_pnl, "green"))
except:
    print("Zero")

try:
    res = client.get_position_risk(symbol=coinPair_2)
    pnl = res[1]['unRealizedProfit']
    short_side_pnl = round_step_size(pnl, tickSize)
    print(f"{coinPair_2} Short Side PNL: ", colored(short_side_pnl, "green"))
except:
    print("Zero")
