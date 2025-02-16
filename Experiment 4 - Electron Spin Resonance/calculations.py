from math import sqrt,pi
import csv

r = 0.077
N = 500
mu0 = 4*(pi)*10**-7
zeta = 2*sqrt(1.6)*(0.8)*mu0*N/r
h = 6.62607015*10**-34
e = 1.60217662*10**-19
m_e = 9.10938356*10**-31
muB = e*h/(4*pi*m_e)

def calculate_B(P, Q, current):
    return (zeta/P)*(current*Q)


def calculate_g(nu,B0):
    return (h*nu*10**6)/(muB*B0)


data = []

with open("Original_readings.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        current = float(row['I(mA)']) * 10**-3
        P1 = float(row['P1'])   
        Q1 = float(row['2Q1'])/2
        P2 = float(row['P2'])   
        Q2 = float(row['2Q2'])/2
        P3 = float(row['P3'])   
        Q3 = float(row['2Q3'])/2
        P4 = float(row['P4'])   
        Q4 = float(row['2Q4'])/2
        B1 = calculate_B(P1, Q1, current)
        B2 = calculate_B(P2, Q2, current)
        B3 = calculate_B(P3, Q3, current)
        B4 = calculate_B(P4, Q4, current)
        g1 = calculate_g(12, B1)
        g2 = calculate_g(13, B2)
        g3 = calculate_g(14, B3)
        g4 = calculate_g(15, B4)
        row['(Current)_inv (1/A)'] = 1/current
        row['B1'] = B1
        row['B2'] = B2
        row['B3'] = B3
        row['B4'] = B4
        row['g1'] = g1
        row['g2'] = g2
        row['g3'] = g3
        row['g4'] = g4
        data.append(row)
        
    with open("experimental_readings.csv", "w", newline='') as file:
        fieldnames = reader.fieldnames + ['(Current)_inv (1/A)', 'B1', 'B2', 'B3', 'B4', 'g1', 'g2', 'g3', 'g4']
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


def average_from_csv(column_name):
    with open("experimental_readings.csv", "r") as file:
        reader = csv.DictReader(file)
        values = []
        for row in reader:
            values.append(float(row[column_name]))
    return sum(values)/len(values)


print("nu = 12 MHz,\nslope = ", calculate_slope_from_csv('2Q1', '(Current)_inv (1/A)'))
print("nu = 13 MHz,\nslope = ", calculate_slope_from_csv('2Q2', '(Current)_inv (1/A)'))
print("nu = 14 MHz,\nslope = ", calculate_slope_from_csv('2Q3', '(Current)_inv (1/A)'))
print("nu = 15 MHz,\nslope = ", calculate_slope_from_csv('2Q4', '(Current)_inv (1/A)'))
print("Average g value = ", average_from_csv('g1'), average_from_csv('g2'), average_from_csv('g3'), average_from_csv('g4'))