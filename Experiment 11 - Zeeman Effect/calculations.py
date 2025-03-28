import math
import csv

d = 0.0035
c = 3 * 10**8
B1 = 0.3294
B2 = 0.4388
e_m = 1.758820024 * 10**11

def error_percentage(actual, experimental):
    return abs(actual - experimental) / actual * 100

def calculate_ratio(dr,DR,B):
    return (4*math.pi*c*dr)/(2*DR*B*d)

data = []
with open("original_data-1.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        a = float(row['a'])
        c = float(row['c'])
        dr = c - a
        row['dr'] = dr
        data.append(row)
        
    with open("experimental_readings.csv", "w", newline='') as file:
        fieldnames = reader.fieldnames + ['dr']
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

def calculate_DR(X, Y, Z, A)-> float:
    with open("experimental_readings.csv", "r") as file:
        reader = csv.DictReader(file)
        x_values = []
        y_values = []
        z_values = []
        for row in reader:
            if row['Ring No'] == A:
                x_values.append(float(row[X]))
                y_values.append(float(row[Y]))
                z_values.append(float(row[Z]))

    if len(x_values) < 2 or len(y_values) < 2 or len(z_values) < 2:
        raise ValueError("Not enough data points to calculate slope")
    
    return (y_values[-1] - y_values[0] + x_values[-1] - x_values[0]+ z_values[-1] - z_values[0])/9



def average_val(X, A)-> float:
    with open("experimental_readings.csv", "r") as file:
        reader = csv.DictReader(file)
        x_values = []
        for row in reader:
            if row['Ring No'] == A:
                x_values.append(float(row[X]))
        return sum(x_values)/len(x_values)
    
    
DR1 = calculate_DR("a", "b", "c","a")
DR2 = calculate_DR("a", "b", "c","b")
print(f"DR1 = {DR1}")
print(f"DR2 = {DR2}")
dr1 = average_val("dr", "a")
dr2 = average_val("dr", "b")
print(f"dr1 = {dr1}")
print(f"dr2 = {dr2}")
em1 = calculate_ratio(dr1, DR1, B1)
em2 = calculate_ratio(dr2, DR2, B2)
print(f"e/m1 = {em1}")
print(f"e/m2 = {em2}")
print(f"Error Percentage 1 = {error_percentage(e_m, em1)}%")
print(f"Error Percentage 2 = {error_percentage(e_m, em2)}%")