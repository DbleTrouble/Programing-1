eggs = int(input("Enter the total number of eggs:"))
dozens = eggs // 12
remainder = eggs % 12
price = 0.0
cost = 0.0

if dozens >= 0 and dozens < 4:
    price = 0.50
elif dozens >= 4 and dozens < 6:
    price = 0.45
elif dozens >= 6 and dozens < 11:
    price = 0.40
elif dozens >= 11:
    price = 0.35



cost = dozens * price + (remainder * 1.0/12 * price)
print("Price per eggs is $" + str(price))
print("Total cost is $" + str(round(cost,2)))
input()
