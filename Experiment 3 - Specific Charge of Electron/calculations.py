import math
import csv

R = 0.2
N = 154
mu0 = 4*(math.pi)*10**-7

specific_charge_constant = (125*R*R)/(32*mu0*N*N*mu0)

def calculate_specific_charge(potential:float, current:float, radius:float) -> float:
    specific_charge = specific_charge_constant * potential * 1/(current * radius)**2
    return specific_charge

data = []
with open("original_readings.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        potential = float(row['U(V)'])
        I2 = float(row['I_2'])   
        I3 = float(row['I_3'])
        I4 = float(row['I_4'])
        I5 = float(row['I_5'])
        i2 = I2**2
        i3 = I3**2
        i4 = I4**2
        i5 = I5**2
        charge1 = calculate_specific_charge(potential=potential, current=I2, radius=0.02)
        charge2 = calculate_specific_charge(potential=potential, current=I3, radius=0.03)
        charge3 = calculate_specific_charge(potential=potential, current=I4, radius=0.04)
        charge4 = calculate_specific_charge(potential=potential, current=I5, radius=0.05)
        row['I_2**2'] = i2
        row['I_3**2'] = i3
        row['I_4**2'] = i4
        row['I_5**2'] = i5
        row['Specific_Charge(I_2)'] = charge1
        row['Specific_Charge(I_3)'] = charge2
        row['Specific_Charge(I_4)'] = charge3
        row['Specific_Charge(I_5)'] = charge4
        data.append(row)
        
    with open("experimental_readings.csv", "w", newline='') as file:
        fieldnames = reader.fieldnames + ['I_2**2', 'I_3**2', 'I_4**2', 'I_5**2', 'Specific_Charge(I_2)', 'Specific_Charge(I_3)', 'Specific_Charge(I_4)', 'Specific_Charge(I_5)']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        

def calculate_slope_from_csv(X, Y)-> float:
    with open("experimental_readings.csv", "r") as file:
        reader = csv.DictReader(file)
        x_values = []
        y_values = []
        for row in reader:
            x_values.append(float(row[X]))
            y_values.append(float(row[Y]))

    if len(x_values) < 2 or len(y_values) < 2:
        raise ValueError("Not enough data points to calculate slope")

                # Calculate the slope using the formula (y2 - y1) / (x2 - x1)
    
    n = len(x_values)
    x_sum = sum(x_values)
    x_squared_sum = sum([x**2 for x in x_values])
    y_sum = sum(y_values)
    xy_sum = sum([x * y for x, y in zip(x_values, y_values)])
    slope = (n*xy_sum-(x_sum)*(y_sum))/(n*x_squared_sum-(x_sum)**2)

    return slope