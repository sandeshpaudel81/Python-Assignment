import os
import csv

season_temperature = {
    'Summer': [],
    'Autumn': [],
    'Winter': [],
    'Spring': []
}

def aggregate_seasonal_temp():
    for filename in os.listdir('./temperature_data'):
        with open(os.path.join('./temperature_data', filename), 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                try:
                    # Monthly temperature starts from index 4 (January) and ends to index 15 (December)
                    # Summer season months are Dec, Jan and Feb (4,5,15)
                    season_temperature['Summer'].append(float(row[4]))
                    season_temperature['Summer'].append(float(row[5]))
                    season_temperature['Summer'].append(float(row[15]))
                    # Summer season months are Mar, Apr and May (6,7,8)
                    season_temperature['Autumn'].append(float(row[6]))
                    season_temperature['Autumn'].append(float(row[7]))
                    season_temperature['Autumn'].append(float(row[8]))
                    # Summer season months are Jun, Jul and Aug (9,10,11)
                    season_temperature['Winter'].append(float(row[9]))
                    season_temperature['Winter'].append(float(row[10]))
                    season_temperature['Winter'].append(float(row[11]))
                    # Summer season months are Sep, Oct and Nov (12,13,14)
                    season_temperature['Spring'].append(float(row[12]))
                    season_temperature['Spring'].append(float(row[13]))
                    season_temperature['Spring'].append(float(row[14]))
                except ValueError:
                    continue

# part A - writing average of each season
def write_season_average_temp():
    with open('average_temp.txt', 'w') as f:
        for season, temps in season_temperature.items():
            avg = sum(temps) / len(temps)
            f.write(f"{season}: {avg:.2f} C\n")

def main():
    aggregate_seasonal_temp()
    write_season_average_temp()


if __name__=="__main__":
    main()