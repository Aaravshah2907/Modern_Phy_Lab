import csv

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


red_slope = calculate_slope_from_csv("B(Tesla)","Theta_R(Rad)")
green_slope = calculate_slope_from_csv("B(Tesla)","Theta_G(Rad)")
print(f'For Red Line, slope = {red_slope}')
print(f'For Green Line, slope = {green_slope}')

print(f'Verdet Constant for Red Line = {red_slope/0.1}')
print(f'Verdet Constant for Green Line = {green_slope/0.1}')

print(f'Constant = {(red_slope/0.1)*650*650*10**-18}')
print(f'Constant = {(green_slope/0.1)*532*532*10**-18}')
