import math
import csv

T0 = 300
d = 0.135
A = math.pi * (d/2)**2
sigma = 5.67037 * 10**-8

def error_percentage(actual, experimental):
    return abs(actual - experimental) / actual * 100

data = []
with open("original_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        Potential = float(row['V(Volt)'])
        Current = float(row['Current(Ampere)'])   
        TC = float(row['T(C)'])
        TK = float(row['T(K)'])
        row["Power_Input"] = Potential * Current
        temp_diff = TK**4 - T0**4
        row["Temp_Diff"] = temp_diff
        Denominator = temp_diff * A
        row["Denominator"] = Denominator
        data.append(row)
        
    with open("experimental_readings.csv", "w", newline='') as file:
        fieldnames = reader.fieldnames + ["Power_Input", "Temp_Diff", "Denominator"]
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


slope = calculate_slope_from_csv("Temp_Diff", "Power_Input")
print(f"Slope = {slope}")
print(f"Error Percentage = {error_percentage(sigma, slope)}")