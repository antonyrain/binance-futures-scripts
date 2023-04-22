#!/usr/bin/env python3
from binance.um_futures import UMFutures
from credentials import api_key, api_secret
from settings import coin, stbCoin, amount


client = UMFutures(key=api_key, secret=api_secret)
# coin = input("Coin: ").upper()
coinPair = f"{coin}{stbCoin}"
# amount = float(input("Qty: "))

close_short_order = {
    "symbol": coinPair,
    "side": "BUY",
    "type": "MARKET",
    "positionSide": "SHORT",
    "quantity": amount,
}

client.new_order(**close_short_order)
