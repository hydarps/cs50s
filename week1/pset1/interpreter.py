x = float(input("Num: "))

y = input("operator: ")
z = float(input("Num2: "))

if y == "+":
    y = x + z
elif y == "-":
    y = x - z
elif y == "*":
    y = x * z
elif y == "/":
    y = x/z
else:
    print("try again")

print(y)
