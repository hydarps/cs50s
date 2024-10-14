amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    coin = int(input("Insert coin: "))
    if coin in [5, 10, 25, 50]:
        amount_due -= coin
    else:
        print("Amount Due: ")

change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")
