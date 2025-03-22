import csv
import random
from datetime import datetime, timedelta

# Define app names and generate random usage data
apps = ['Instagram', 'WhatsApp', 'YouTube', 'Twitter', 'LinkedIn']
rows = []

# Generate data for the last 7 days
for i in range(7):
    date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
    for app in apps:
        usage_time = random.randint(30, 180)  # Random usage between 30 to 180 mins
        launch_count = random.randint(1, 15)
        rows.append([app, usage_time, launch_count, date])

# Save data to CSV
csv_file = 'data/app_usage.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['app_name', 'usage_time', 'launch_count', 'timestamp'])
    writer.writerows(rows)

print(f"✅ Data collected and saved in {csv_file}")
