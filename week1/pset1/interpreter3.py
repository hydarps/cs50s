exp = input("Expression: ")

if (" ") in exp == ("")

x,y,z = exp.split(" ")

x = float(x)
z = float(z)
y = y

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
