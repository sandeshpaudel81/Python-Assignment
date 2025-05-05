import os
import csv

season_temperature = {
    'Summer': [],
    'Autumn': [],
    'Winter': [],
    'Spring': []
}

for filename in os.listdir('./temperature_data'):
    with open(os.path.join('./temperature_data', filename), 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            season_temperature['Summer'].append(float(row[4]))
            season_temperature['Summer'].append(float(row[5]))
            season_temperature['Summer'].append(float(row[15]))