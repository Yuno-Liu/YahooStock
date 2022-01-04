import yfinance as yf
from colorama import init, Fore, Back, Style
from termcolor import colored

def getStock(stockId):
    init(autoreset=True)    #  初始化，並且設置顏色設置自動恢復
    stock = yf.Ticker(stockId)
    stockList = stock.history(period="2d")
    closeF = float(round(stockList['Close'][0],2))  # 前日價格
    closeL = float(round(stockList['Close'][1],2))  # 目前價格
    Spread = float(round(closeL - closeF))          # 價差
    fluctuationLimit = float(round((Spread / closeF) * 100,2))  # 漲跌幅
    # _str =  + str(fluctuationLimit) + " %"
    if fluctuationLimit == 0 :
        print(Back.WHITE + Fore.BLACK + "0.00 %")
    elif fluctuationLimit > 0 :
        print(Back.RED + Fore.BLACK + str(fluctuationLimit) + " %")
    else:
        print(Back.GREEN + Fore.BLACK + str(fluctuationLimit) + " %")    

while True:
    print("離開：!exit")
    try:
        stockId = input("請輸入代號：")
        if stockId == "!exit":
            break
        getStock(stockId)
    except:
        print("")