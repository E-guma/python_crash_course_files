from os import path
from datetime import datetime
import csv
from matplotlib import pyplot as plt

# Get high temperatures from file
file_path = path.join(path.dirname(__file__) , 'sitka_weather_2014.csv')
with open(file_path) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        # Get data.
        date = datetime.strptime(row[0], '%Y-%m-%d')
        high = int(row[1])
        low = int(row[3])
        # Append data.
        dates.append(date)
        highs.append(high)
        lows.append(low)

# Plot Data
# plt.style.use('seaborn-v0_8')
fig = plt.figure(dpi=128, figsize=(7,4))
plt.plot(dates, highs, 'r')
plt.plot( lows, 'b')
# Format Plot
plt.title("Daily high and low temperatures - 2014", fontsize=20)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12,)

plt.savefig('highs_lows.png')