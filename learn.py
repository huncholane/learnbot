import pandas as pd
import os
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

df = pd.read_csv('export.csv')

myarr = df.close.to_numpy()[:10000]


arr = myarr
peaks = find_peaks(arr, threshold=.1)

dot_y = []
for i, point in enumerate(arr):
    if i in peaks[0]:
       dot_y.append(point)

len(peaks[0]), len(dot_y)

plt.plot(arr)
plt.plot(peaks[0], dot_y, 'r.', markersize=3)
plt.show()

