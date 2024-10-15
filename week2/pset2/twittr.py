word = input("Input: ")
vowel = "aeiouAEIOU"
new_word =""

for letter in word:
    if letter not in vowel:
        new_word += letter

print("Output: ",new_word)
