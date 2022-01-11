import yfinance as yf
from colorama import init, Fore, Back, Style
from termcolor import colored
import threading
import os

clear = lambda: os.system('cls')

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    clear()
    return t

def call():
    arr = ["00893.tw","00895.tw","2330.tw","00881.tw"]
    for x in arr:
        stock = yf.Ticker(x) # 00893  00895
        # info = stock.info
        stockList = stock.history(period="2d")
        closeF = float(round(stockList['Close'][0],2))  # 前日價格
        closeL = float(round(stockList['Close'][1],2))  # 目前價格
        High = float(round(stockList['High'][1],2))
        Low = float(round(stockList['Low'][1],2))
        Spread = round(round(closeL,2) - round(closeF,2),2)          # 價差
        fluctuationLimit = float(round((Spread / closeF) * 100,2))  # 漲跌幅
        if fluctuationLimit > 0:
            fluctuationLimit = "+" + str(fluctuationLimit)
        elif fluctuationLimit < 0:
            fluctuationLimit = "-" + str(abs(fluctuationLimit))
        fluctuationLimit = str(fluctuationLimit) + " %"
        # print(info['shortName'])
        print("ID：" + x + " 當前價：" + str(closeL) + " 開盤價：" + str(closeF) +" 最高價：" + str(High) + " 最低價：" + str(Low) + " 價差：" + str(Spread) + " 漲跌幅：" + str(fluctuationLimit))
        
set_interval(call, 10)        