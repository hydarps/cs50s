exp = input("Expression: ")

x,y,z = exp.split(" ")

x = float(x)
z = float(z)

if y == "+":
    y = x + z
elif y == "-":
    y = x - z
elif y == "*":
    y = x * z
elif y == "/":
    y = x/z
else:
    print("Invalid operator, try again.")

print(y)
