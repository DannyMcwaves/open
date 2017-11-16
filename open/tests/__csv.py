from open.main.csv import Csv
from open.main.variables import CSV_DATA

csv = Csv(CSV_DATA)
print(csv)
print(len(csv))
print(csv[0])
# csv()
for i in csv:
    print(i)
