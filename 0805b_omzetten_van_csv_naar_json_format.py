# script_0805b_omzetting van csv naar json
# File.csv omzetten naar JSON-formaat
import csv
import json

f = open ( 'file.csv', 'rU')


reader = csv.DictReader(f, fieldnames = ( "V00_Index", "V00_tijd", "V01_gas", "V02_gas", "V03_gas", "V04_gas", "V05_gas", "V06_gas", "V07_gas", "V08_gas", "V11_temp", "V12_vochtigheid"))

out = json.dumps( [ row for row in reader] )
print("Parsen van JSON-formaat  gereed!")
f = open( 'parsed.json', 'w')
f.write(out)
print("Dataset is omgezet naar JSON!")
f.close()