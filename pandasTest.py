import pandas as pd
import datetime
import pandas_datareader.data as web
import os


print "this is a test"
print os.environ.get('PATH')
print os.environ.get('PYTHONPATH')

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2016, 12, 20)

df = web.DataReader("HQH", "yahoo", start, end)
print(df.head())
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
df['High'].plot()
plt.legend()
plt.show()

pd.read_

