import csv

a = -5
nums = []
while a<5:
    nums.append(a)
    a = a+0.001
    
with open("numbers.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["a"])
    for num in nums:
        writer.writerow([num])