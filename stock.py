import yfinance as yf
from colorama import init, Fore, Back, Style

def my_function(stockId):
    init(autoreset=True)    #  初始化，并且设置颜色设置自动恢复
    stock = yf.Ticker(stockId)
    stockList = stock.history(period="2d")
    closeF = float(round(stockList['Close'][0],2))  # 前日價格
    closeL = float(round(stockList['Close'][1],2))  # 目前價格
    Spread = float(round(closeL - closeF))          # 價差
    fluctuationLimit = float(round((Spread / closeF) * 100,2))  # 漲跌幅
    print(Fore.RED  + str(fluctuationLimit) + " %")
    print(str(fluctuationLimit) + " %")

while True:
    print("離開：!exit")
    try:
        stockId = input("請輸入代號：")
        if stockId == "!exit":
            break
        my_function(stockId)
    except:
        print("")