'''
camel_case = input("Enter word: ")
result = ""

for letter in camel_case:
    result += "_" + letter.lower() if letter.isupper() else letter

print(result)
'''


'''
#================================================
#Tenery operator

x = 10
y = 20

max_value = x if x > y else y

print(max_value)
'''
