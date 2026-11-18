import time

#time.sleep(1)
my_time = int(input("Enter the time to countdown in seconds: "))
average = my_time

for x in range(my_time, 0, -1):
    second = x % 60
    minute = int(x / 60) % 60
    hour = int(x / 3600)
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

print("TIME'S UP!")