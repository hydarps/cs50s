question = input("What is the answer to the great question in life, the univerese, everything? ").lower() #ask for the question and convert the answer to lowercase

if question == "42" or question == "forty two" or question == "forty_two": #handling the possible answers
    print("yes")
else:
    print("no")
