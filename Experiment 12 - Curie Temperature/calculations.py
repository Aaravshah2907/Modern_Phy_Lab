import csv

d = 0.00108
r = 0.012
C0 = r**2/(36*d)
C_SC = 10.38
data = []
with open("og_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        VSC = float(row['VSC'])
        VDC = float(row['VDC'])
        CDC = C_SC * VSC/VDC
        Er = CDC/C0 
        row['CDC'] = CDC
        row['Er'] = Er
        data.append(row)
        
with open("experimental_readings.csv", "w", newline='') as file:
    fieldnames = reader.fieldnames + ['CDC', 'Er']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
        
