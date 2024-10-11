amount_due = 50
calc = 0

while calc < amount_due:
    print(f"Still due: {amount_due - calc}")
    coin = int(input("insert coin: "))
    if coin < amount_due:
        calc += coin
    elif coin > amount_due:
        calc -= coin


    else:
        calc += coin

print(f"Balance paid, your change: {calc-amount_due}")
