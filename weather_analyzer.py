import numpy as np
import csv
from datetime import datetime

# Step 1: Load the CSV file (skipping the header)
filename = "DailyDelhiClimateTest.csv"

dates = []
temps = []
humidity = []
wind_speed = []

with open(filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        try:
            dates.append(datetime.strptime(row[0], "%Y-%m-%d"))
            temps.append(float(row[1]))
            humidity.append(float(row[2]))
            wind_speed.append(float(row[3]))
        except:
            continue  # Skip rows with missing or invalid data

# Step 2: Convert lists to NumPy arrays
temps = np.array(temps)
humidity = np.array(humidity)
wind_speed = np.array(wind_speed)
dates = np.array(dates)

# Step 3: Perform calculations
avg_temp = np.mean(temps)
max_temp = np.max(temps)
min_temp = np.min(temps)
max_temp_day = dates[np.argmax(temps)]
min_temp_day = dates[np.argmin(temps)]

avg_humidity = np.mean(humidity)
high_humidity_days = np.sum(humidity > 80)

avg_wind_speed = np.mean(wind_speed)
windy_days = np.sum(wind_speed > 10)

# Step 4: Display results
print("--------- Delhi Weather Stats ---------")
print(f"Average Temperature      : {avg_temp:.2f} °C")
print(f"Hottest Day              : {max_temp_day.date()} ({max_temp} °C)")
print(f"Coldest Day              : {min_temp_day.date()} ({min_temp} °C)")
print(f"Average Humidity         : {avg_humidity:.2f} %")
print(f"High Humidity Days (>80%): {high_humidity_days} days")
print(f"Average Wind Speed       : {avg_wind_speed:.2f} km/h")
print(f"Windy Days (>10 km/h)    : {windy_days} days")
print("----------------------------------------")
