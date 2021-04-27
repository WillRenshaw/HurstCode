import numpy as np
import matplotlib.pyplot as plt
import csv

#Read Data in
with open('test.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)[0]
newData = []
for i in range(1, len(data)):
    newData.append(float(data[i]))

########################################################################################################################
###################################### CHANGE ME #######################################################################
########################################################################################################################
rangeStart = 0 #This is the range start value
rangeEnd = len(newData) #This is the range end value, can be set to any integer number, at the moment it is set for all
xLabel = "This is the x label"
yLabel = "This is the y label"
graphTitle = "This is the graph title"
########################################################################################################################
########################################################################################################################
########################################################################################################################



newData = newData[rangeStart:rangeEnd]
ts = newData
ts = ts[int(len(ts)/2):]

lags = range(2, 20)
tau = [np.sqrt(np.std(np.subtract(ts[lag:], ts[:-lag]))) for lag in lags]
# plot on log-log scale


# calculate Hurst as slope of log-log plot
m = np.polyfit(np.log(lags), np.log(tau), 1)
hurst = m[0]*2.0
print('hurst = ', hurst)
plt.plot(np.log(lags), np.log(tau))
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title(graphTitle)
plt.show()
