list =["apple", "strawberry", "manggo", "kiwi", "lemon"]

fruit = input("type fruit: ")

text1 = "found"
text2 = "not found"

cap_text1 = str.title(text1)
cap_text2 = str.title(text2)
cap_fruit = str.title(fruit)


if fruit in list:
    #print(cap_text1 + " " + cap_fruit)
else:
    print(cap_text2 + " " + cap_fruit)
