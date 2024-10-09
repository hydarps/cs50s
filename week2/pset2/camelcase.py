# TEST 1.v2 ----------------------------->


camelcase = input("enter word: ")
result=""

for letter in camelcase:
    if letter.isupper():
         result += "_" + letter.lower()
    else:
        result += letter

print(result)



