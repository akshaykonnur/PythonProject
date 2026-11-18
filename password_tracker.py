correct_password = "Python123"
password = input("Please enter your password: ")
count = 3
while password != correct_password:
    print("incorrect password")
    count = count - 1
    print(f"you have {count} attempts left")

    if count == 0:
        print("you have reached the limit")
        break

    password = input("Please enter your password: ")

    if password == correct_password:
        print("access_granted")

