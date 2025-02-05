from math import sqrt, sin, asin
import csv

wavelength_constant = 3.878299416e-11

def calculate_wavelength(potential :float) -> float:
    return wavelength_constant / sqrt(potential)


def calculate_wavelength_from_csv():
    with open("experimental_readings.csv","+r") as file:
        # Read the existing data
        data = []
        with open("experimental_readings.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                potential = float(row['U(kV)'])
                wavelength = calculate_wavelength(potential)
                row['Wavelength(pm)'] = wavelength*1e12
                data.append(row)

        # Write the updated data back to the CSV file
        with open("experimental_readings.csv", "w", newline='') as file:
            fieldnames = reader.fieldnames + ['Wavelength(pm)']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
            

def calculate_distance(wavelength: float, r: float) -> float:
    numerator = wavelength/2
    denominator = sin(0.25 * asin(r/65))
    return numerator / denominator


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

def calculate_d_theoretical(X,Y,Z)->None:
    with open("experimental_readings.csv","+r") as file:
        # Read the existing data
        data = []
        with open("experimental_readings.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                wavelength = float(row[Y])
                r = float(row[X])
                distance = calculate_distance(wavelength, r)
                row[Z] = distance
                data.append(row)

        # Write the updated data back to the CSV file
        with open("experimental_readings.csv", "w", newline='') as file:
            fieldnames = reader.fieldnames + [Z]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    
    
def average_value(Z)->float:
    with open("experimental_readings.csv","+r") as file:
        # Read the existing data
        data = []
        with open("experimental_readings.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(float(row[Z]))
    return sum(data)/len(data)


calculate_wavelength_from_csv()
print(calculate_slope_from_csv(Y='R1(mm)', X='Wavelength(pm)'))
print(calculate_slope_from_csv(Y='R2(mm)', X='Wavelength(pm)'))
calculate_d_theoretical(X='R1(mm)', Y='Wavelength(pm)',Z='d1_wo_app(pm)')
calculate_d_theoretical(X='R2(mm)', Y='Wavelength(pm)',Z='d2_wo_app(pm)')

print(average_value('d1_wo_app(pm)'))
print(average_value('d2_wo_app(pm)'))