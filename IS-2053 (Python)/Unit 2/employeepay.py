# Put your code here
# inputs
wage = float(input("Enter the wage: "))
regularHours = int(input("Enter the regular hours: "))
overtimeHours = int(input("Enter the overtime hours: "))
# calculations
overtimePay = overtimeHours * 1.5 * wage
totalWage = wage * regularHours + overtimePay
# output
print(f'The total weekly pay is ${totalWage}')
