
# Given a dataset of monthly temperature records for a city, calculate the
# monthly average temperature, identify the hottest and coldest months,
# and determine the overall annual temperature trend using NumPy.
# monthly_temperatures = np.array([
# [32.1, 34.5, 40.2, 48.7, 56.3, 63.8, 70.2, 70.1, 63.1, 53.5, 43.9, 35.0], # January
# [32.9, 35.8, 41.5, 49.7, 57.5, 64.8, 71.2, 71.1, 63.8, 54.2, 44.5, 35.7], # February
# [34.2, 37.4, 44.1, 52.2, 60.3, 67.2, 74.0, 74.1, 66.1, 56.2, 46.2, 37.4], # March
# [39.2, 42.5, 49.9, 58.2, 66.4, 73.2, 79.4, 79.0, 70.4, 60.1, 49.8, 41.1], # April
# [46.1, 49.9, 57.3, 65.4, 73.3, 79.9, 85.5, 85.3, 76.4, 66.0, 55.2, 47.0], # May
# [53.2, 57.5, 65.4, 73.2, 80.6, 86.7, 91.7, 91.3, 82.4, 72.5, 61.6, 54.1], # June
# [59.2, 63.4, 71.3, 79.1, 86.9, 92.5, 96.9, 96.4, 88.4, 78.5, 67.6, 60.0], # July
# [59.0, 63.0, 70.9, 78.6, 86.0, 91.8, 96.4, 96.2, 88.0, 78.3, 67.6, 59.6], # August
# [52.3, 56.6, 64.5, 72.4, 80.1, 86.4, 91.3, 91.2, 83.3, 73.5, 62.6, 54.8], # September
# [45.4, 49.4, 56.9, 64.8, 72.7, 78.8, 83.2, 82.8, 75.0, 65.2, 54.9, 47.1], # October
# [37.8, 41.4, 48.5, 56.2, 63.5, 69.9, 74.7, 74.5, 67.2, 57.3, 47.9, 39.5], # November
# [32.6, 35.8, 42.7, 50.0, 57.1, 63.1, 67.8, 67.6, 60.2, 50.9, 41.4, 34.1] # December
# ])

import numpy as np

# Sample dataset of monthly temperatures (replace with your data)
monthly_temperatures = np.array([
[32.1, 34.5, 40.2, 48.7, 56.3, 63.8, 70.2, 70.1, 63.1, 53.5, 43.9, 35.0], # January
[32.9, 35.8, 41.5, 49.7, 57.5, 64.8, 71.2, 71.1, 63.8, 54.2, 44.5, 35.7], # February
[34.2, 37.4, 44.1, 52.2, 60.3, 67.2, 74.0, 74.1, 66.1, 56.2, 46.2, 37.4], # March
[39.2, 42.5, 49.9, 58.2, 66.4, 73.2, 79.4, 79.0, 70.4, 60.1, 49.8, 41.1], # April
[46.1, 49.9, 57.3, 65.4, 73.3, 79.9, 85.5, 85.3, 76.4, 66.0, 55.2, 47.0], # May
[53.2, 57.5, 65.4, 73.2, 80.6, 86.7, 91.7, 91.3, 82.4, 72.5, 61.6, 54.1], # June
[59.2, 63.4, 71.3, 79.1, 86.9, 92.5, 96.9, 96.4, 88.4, 78.5, 67.6, 60.0], # July
[59.0, 63.0, 70.9, 78.6, 86.0, 91.8, 96.4, 96.2, 88.0, 78.3, 67.6, 59.6], # August
[52.3, 56.6, 64.5, 72.4, 80.1, 86.4, 91.3, 91.2, 83.3, 73.5, 62.6, 54.8], # September
[45.4, 49.4, 56.9, 64.8, 72.7, 78.8, 83.2, 82.8, 75.0, 65.2, 54.9, 47.1], # October
[37.8, 41.4, 48.5, 56.2, 63.5, 69.9, 74.7, 74.5, 67.2, 57.3, 47.9, 39.5], # November
[32.6, 35.8, 42.7, 50.0, 57.1, 63.1, 67.8, 67.6, 60.2, 50.9, 41.4, 34.1] # December
])

# Step 2: Calculate Monthly Averages
monthly_averages = np.mean(monthly_temperatures, axis=0)

# Step 3: Identify Hottest and Coldest Months
hottest_month = np.argmax(monthly_averages) + 1 # Adding 1 to convert 0-based index to month number
coldest_month = np.argmin(monthly_averages) + 1

# Step 4: Determine Annual Temperature Trend
annual_average = np.mean(monthly_averages)

# Print results
print("Monthly Averages:", monthly_averages)
print("Hottest Month:", hottest_month)
print("Coldest Month:", coldest_month)
print("Annual Average Temperature:", annual_average)
