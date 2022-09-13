#爬蟲"台灣證劵交易網站"
#指定"月份" "股票代碼"


import requests
import time
import pandas as pd
from fake_useragent import UserAgent

s = 1
d = 1
dates = []
stockNo = 0

for d in range(s):
    dates.append(input("請輸入yyyy年mm月dd日:").strip())
    stockNo = input("請輸入股票代碼:").strip()

#dates = [20220801]
#stockNo = 2330

url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}"

# 偽裝 User-Agent
ua = UserAgent()


for date in dates :
    url2 = url.format(date, stockNo)
    #print(url2)
    file = ("{}_{}.csv".format(date,stockNo))
    
    data = pd.read_html(requests.get(url2).text)[0]
    data.columns = data.columns.droplevel(0)
    data.to_csv(file, index=False, encoding="utf_8_sig") #存成csv檔

    time.sleep(5)
