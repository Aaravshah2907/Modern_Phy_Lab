import math
import csv

R = 0.2
N = 154
mu0 = 4*(math.pi)*10**-7
Theta_ref = 277.5 + 4/30 #degrees
d = 1.67 * 10**-6 #metres
Rydebergs_actual = 1.0973731568539 * 10**7 #m^-1

def percentage_error(experimental:float)->float:
    return (abs(experimental - Rydebergs_actual)/Rydebergs_actual)*100


def average_theta(theta1:float, theta2:float) -> float:
    return (theta1 - theta2 )/2


def calculate_wavelength(m:int, theta:float) -> float:
    return (d*math.sin(math.radians(theta)))/m

data = []
with open("Original_readings.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        n = float(row['n'])
        m = float(row['m'])
        Theta_R = float(row['Theta_R'])
        Theta_L = float(row['Theta_L'])
        Theta_average = average_theta(Theta_L, Theta_R)
        diff = (0.25 - 1/(n**2))
        wavelength = calculate_wavelength(m, Theta_average)
        inv_wavelength = 1/wavelength
        Rydebergs = inv_wavelength/diff
        percentage_error_value = percentage_error(Rydebergs)
        row['Theta_average'] = Theta_average
        row['Wavelength'] = wavelength
        row['Wavelength_inv'] = inv_wavelength
        row['diff'] = diff
        row['Rydebergs'] = Rydebergs
        row['percentage_error'] = percentage_error_value
        data.append(row)
        
    with open("experimental_readings.csv", "w", newline='') as file:
        fieldnames = reader.fieldnames + ['Theta_average', 'Wavelength', 'Wavelength_inv', 'diff', 'Rydebergs', 'percentage_error']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        

def calculate_slope_from_csv(X, Y, m)-> float:
    with open("experimental_readings.csv", "r") as file:
        reader = csv.DictReader(file)
        x_values = []
        y_values = []
        m_values = []
        for row in reader:
            x_values.append(float(row[X]))
            y_values.append(float(row[Y]))
            m_values.append(float(row['m']))

    if len(x_values) < 2 or len(y_values) < 2:
        raise ValueError("Not enough data points to calculate slope")

                # Calculate the slope using the formula (y2 - y1) / (x2 - x1)
    
    n = len(x_values)
    x_sum = 0
    x_squared_sum = 0
    y_sum = 0
    xy_sum = 0
    for index in range(len(m_values)):
        if m == m_values[index]:
            x_sum += x_values[index]
            x_squared_sum += x_values[index]**2
            y_sum += y_values[index]
            xy_sum += (x_values[index]*y_values[index])
    slope = (n*xy_sum-(x_sum)*(y_sum))/(n*x_squared_sum-(x_sum)**2)

    return slope


slope1 = calculate_slope_from_csv("diff", "Wavelength_inv", 1)
slope2 = calculate_slope_from_csv("diff", "Wavelength_inv", 2)
print(f'Slope for m = 1 is {slope1}, Error % = {percentage_error(slope1)}%')
print(f'Slope for m = 2 is {slope2}, Error % = {percentage_error(slope2)}%')