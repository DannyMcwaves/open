from open import Csv
from open import CSV_DATA

print(CSV_DATA)

csv = Csv(CSV_DATA)
print(csv)
print(len(csv))
print(csv[0])
csv()

for i in csv:
    print(i)

print(csv.read())
