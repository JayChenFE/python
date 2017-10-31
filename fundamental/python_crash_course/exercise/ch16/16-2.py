# 16-2
# 比较锡特卡和死亡谷的气温 ：
# 在有关锡特卡和死亡谷的图表中，气温刻度反映了数据范围的不同。
# 为准确地比较锡特卡和死亡谷的气温范围，需要在y 轴上使用相同的刻度。
# 为此，请修改图16-5和图16-6所示图表的y 轴设置，对锡特卡和死亡谷的气温范围进行直接比较（你也可以对任何两个地方的气温范围进行比较）。
# 你还可以尝试在一个图表中呈现这两个数据集。

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Get dates, high, and low temperatures from file.
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,death_valley_highs,death_valley_lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            death_valley_highs.append(high)
            death_valley_lows.append(low)

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    row2 = next(reader)

    dates1,sitka_weather_highs,sitka_weather_lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            sitka_weather_high = int(row[1])
            sitka_weather_low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates1.append(current_date)
            sitka_weather_highs.append(sitka_weather_high)
            sitka_weather_lows.append(sitka_weather_low)

# Plot data.
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,death_valley_highs,c='red',alpha=0.5)
plt.plot(dates,death_valley_lows,c='blue',alpha=0.5)

plt.plot(dates1,sitka_weather_highs,c='yellow',alpha=0.5)
plt.plot(dates1,sitka_weather_lows,c='pink',alpha=0.5)

# plt.fill_between(dates, death_valley_lows, death_valley_highs, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley&Sitka"
plt.title(title,fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
