import os
import csv

# Path to the folder containing CSV files
data_folder = "temperature"

# Initialize a dictionary to store monthly temperature sums and counts
monthly_data = {month: {'sum': 0, 'count': 0} for month in range(1, 13)}

# Initialize dictionaries to track station-specific data
station_temperature_ranges = {}
station_average_temperatures = {}

# Iterate over all CSV files in the data folder
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        filepath = os.path.join(data_folder, filename)

        with open(filepath, "r") as file:
            reader = csv.reader(file)
            
            # Skip the first row (headers)
            next(reader)

            for row in reader:
                try:
                    # Extract station name and temperatures from columns E to P (index 4 to 15)
                    station_name = row[0]
                    temperatures = [float(temp) for temp in row[4:16]]

                    # Update monthly data
                    for month, temperature in enumerate(temperatures, start=1):
                        monthly_data[month]['sum'] += temperature
                        monthly_data[month]['count'] += 1

                    # Calculate station-specific range and average
                    temp_range = max(temperatures) - min(temperatures)
                    avg_temp = sum(temperatures) / len(temperatures)

                    if station_name not in station_temperature_ranges:
                        station_temperature_ranges[station_name] = temp_range
                        station_average_temperatures[station_name] = avg_temp
                    else:
                        station_temperature_ranges[station_name] = max(station_temperature_ranges[station_name], temp_range)
                        station_average_temperatures[station_name] = (station_average_temperatures[station_name] + avg_temp) / 2

                except (ValueError, IndexError):
                    # Skip rows with invalid data
                    continue

# Calculate the average temperature for each month
average_temperatures = {
    month: monthly_data[month]['sum'] / monthly_data[month]['count'] if monthly_data[month]['count'] > 0 else None
    for month in range(1, 13)
}

# Find stations with the largest temperature range
largest_range = max(station_temperature_ranges.values())
largest_range_stations = [station for station, temp_range in station_temperature_ranges.items() if temp_range == largest_range]

# Write the results to "largest_temp_range_station.txt"
with open("largest_temp_range_station.txt", "w") as f:
    f.write("Stations with the largest temperature range:\n")
    for station in largest_range_stations:
        f.write(f"{station}: {largest_range:.2f}\n")

# Find the warmest and coolest stations
warmest_temp = max(station_average_temperatures.values())
coolest_temp = min(station_average_temperatures.values())
warmest_stations = [station for station, avg_temp in station_average_temperatures.items() if avg_temp == warmest_temp]
coolest_stations = [station for station, avg_temp in station_average_temperatures.items() if avg_temp == coolest_temp]

# Write the results to "warmest_and_coolest_station.txt"
with open("warmest_and_coolest_station.txt", "w") as f:
    f.write("Warmest stations:\n")
    for station in warmest_stations:
        f.write(f"{station}: {warmest_temp:.2f}\n")
    f.write("\nCoolest stations:\n")
    for station in coolest_stations:
        f.write(f"{station}: {coolest_temp:.2f}\n")

# Write the average temperatures to "average_temp.txt"
with open("average_temp.txt", "w") as f:
    for month, avg_temp in average_temperatures.items():
        if avg_temp is not None:
            f.write(f"Month {month}: {avg_temp:.2f}\n")
        else:
            f.write(f"Month {month}: No data available\n")