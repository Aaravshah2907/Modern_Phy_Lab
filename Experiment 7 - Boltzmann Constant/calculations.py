import math
import csv

planck_actual = 1.28 * 10**-23 
q = 1.6 * 10**-19

def percentage_error(experimental:float)->float:
    return (abs(experimental - planck_actual)/planck_actual)*100
        

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
    x_sum = 0
    x_squared_sum = 0
    y_sum = 0
    xy_sum = 0
    for index in range(len(x_values)):
        x_sum += x_values[index]
        x_squared_sum += x_values[index]**2
        y_sum += y_values[index]
        xy_sum += (x_values[index]*y_values[index])
    slope = (n*xy_sum-(x_sum)*(y_sum))/(n*x_squared_sum-(x_sum)**2)
    return slope

slope1 = calculate_slope_from_csv("V(Volts)", "ln(I)")
k_calc = q/(293*slope1)
print(f'Slope is {slope1} \nk_calculated is {k_calc}, Error % = {percentage_error(k_calc)}%')