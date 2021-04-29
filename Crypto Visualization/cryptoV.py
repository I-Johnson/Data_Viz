import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt

crypto = "BTC"
currency = "USD"

start = dt.datetime(2020, 5, 1)
end = dt.datetime.now()

btc = web.DataReader(f"BTC-{currency}", "yahoo", start, end)
Eth = web.DataReader(f"ETH-{currency}", "yahoo", start, end)
doge = web.DataReader(f"DOGE-{currency}", "yahoo", start, end)

plt.yscale("log")

plt.plot(btc['Close'], label="BTC")
plt.plot(Eth['Close'], label="ETH")
plt.plot(doge['Close'], label="DOGE")
plt.legend(loc="upper left")
plt.show()
# mpf.plot(data, type='candle', volume=True, style='yahoo')
