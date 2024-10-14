amount_due = 50
still_due = 0

while still_due <= amount_due:
    coin = int(input("Insert coin: "))
    if coin in [5, 10, 25, 50]:
        still_due += coin
        print(f"Insert more coin: {amount_due - still_due}")
        if still_due == amount_due:
            break
        else:
            (still_due + coin) >= amount_due
            change = (still_due + coin) - amount_due
    else:
        print("Insert 5, 10, 25 or 50 cents only")

print(f"Balance paid, your change {change - amount_due}")
