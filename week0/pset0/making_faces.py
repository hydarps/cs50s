text = input("enter text: ")
if ":)" in text:
    print(text.replace(":)", "🙂"))
elif ":(" in text:
    print(text.replace(":(", "🙁"))
else:
    print("yehey!")
