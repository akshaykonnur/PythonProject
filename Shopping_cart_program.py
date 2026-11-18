# Shopping Cart Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food item to buy. Press 'q' tp Quit: ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter price of food item: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR SHOPPING CART -----")

for food,price in zip(foods,prices):
    print(f"{food} : ${price}")

total = sum(prices)
print(f"the total price is ${total}")