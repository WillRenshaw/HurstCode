import numpy as np
from pylab import plot, show
import csv

#Read Data in
with open('test.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)[0]
print(data)
newData = []
for i in range (1, len(data)):
    newData.append(float(data[i]))
print(newData)

ts = newData
lags = range(2, 20)
tau = [np.sqrt(np.std(np.subtract(ts[lag:], ts[:-lag]))) for lag in lags]
# plot on log-log scale


# calculate Hurst as slope of log-log plot
m = np.polyfit(np.log(lags), np.log(tau), 1)
hurst = m[0]*2.0
print ('hurst = ',hurst)
plot(np.log(lags), np.log(tau)); show()