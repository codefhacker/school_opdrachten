# script_0805a_omzetting van dat naar csv
# Dataset .dat omzetten naar .csv-formaat
import csv

with open ('/tmp/HT_Sensor_dataset/HT_Sensor_dataset.dat') as dat_file, open('file.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    for line in dat_file:
        row = [field.strip() for field in line.split(' ')]
        if len(row) == 13:
            csv_writer.writerow(row)
            
print("Omzetting naar file.csv is gereed")