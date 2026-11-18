# python compound Intrest calculator

principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the Principal amount: "))
    if principal < 0:
        print("Principal cannot be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the Intrest Rate: "))
    if rate < 0:
        print("Intrest Rate cannot be less than zero")
    else:
        break

while True:
    time = int(input("Enter the Time in Years: "))
    if time < 0:
        print("Time Frame cannot be less than zero")
    else:
        break

total = round(principal * pow((1 + rate/100),time),2)
#total = round(total,2)

print(f"Balance after {time} years: ${total}")