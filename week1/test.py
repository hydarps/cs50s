'''
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

'''
# --------------------------------------------------------------------------------------------------->
# PSET 0
# --------------------------------------------------------------------------------------------------->

# indoorvoice----------------------------->
'''
text = input("enter text: ")
new_text = text.lower()
print(new_text)
'''

# playbackspeed----------------------------->
'''
text = input("Enter Text: ")

new_text = text.replace(" ", "...")

print(new_text)
'''

# making faces----------------------------->
'''
text = input("enter text: ")
if ":)" in text:
    print(text.replace(":)", "🙂"))
elif ":(" in text:
    print(text.replace(":(", "🙁"))
else:
    print("yehey!")
'''

# einstein----------------------------->
'''
mass = int(input("enter mass:")) #ask for a number input then convert to int to perform a matematical operation
emc = (3 * 10**8)**2 #E=mc2
calc = (mass*emc) #calculate mass and e=mc2

print(calc)
'''

# tip calculator----------------------------->

'''
meal = input("How much is the meal?: ") #ask for the meals dollar value
meal_float = float(meal.replace("$", "")) #convert str to float and remove the dollar sign

tip = input("What percentage would you like to tip?: ") #ask for the tip percentage
tip_float = float(tip.replace("%", "")) #convert str to float

percentage = (tip_float / 100) * meal_float #calculate percentage

print ("Leave: " + str(percentage))
'''


# --------------------------------------------------------------------------------------------------->
# PSET 1
# --------------------------------------------------------------------------------------------------->

# deep----------------------------->
'''
question = input("What is the answer to the great question in life, the univerese, everything? ").lower() #ask for the question and convert the answer to lowercase

if question == "42" or question == "forty two" or question == "forty_two": #handling the possible answers
    print("yes")
else:
    print("no")

'''

# deep 2nd solution----------------------------->
'''

question = input("What is the answer to the great question in life, the univerese, everything? ").lower()

if question != "42" and question != "forty two" and question != "forty_two":
    print("No")
else:
    print("yes")
'''

# bank----------------------------->
'''
greet = input("Greetings: ").lower().strip() #ask for the greetings, convert to lowercase and remove whitespace

if greet.startswith("hello"): #if greetings starts with hello
    print("$0")               #give $0
elif greet.startswith("h"):   #if greetings starts with h
    print("$20")              #give $20

else:                         #else
    print("$100")             #give $100
'''

# extenssions----------------------------->
'''
filetype = input("Enter filetype: ").lower().strip()

if "." not in filetype:
    print("octet-stream")
    name = filetype
    ext = "octet-stream"  # Define ext here, since it doesn't have one
else:
    name, ext = filetype.split(".")

    if ext == "jpg":
        ext = "jpeg"

# Now it prints correctly, no matter what
print(name + "/" + ext)

'''

# extenssions v2----------------------------->

'''

filetype = input("Enter filetype: ").lower().strip()

if "." in filetype:
    name, ext = filetype.split(".")

if ext == "jpg":
    ext = "jpeg"

else:
    name = filetype
    ext = "octet-stream"



print(f"{name}/{ext}")

'''

# interpreter ---------------------------->

'''

x = float(input("Num: "))

y = input("operator: ")
z = float(input("Num2: "))

if y == "+":
    y = x + z
elif y == "-":
    y = x - z
elif y == "*":
    y = x * z
elif y == "/":
    y = x/z
else:
    print("try again")

print(y)

'''
# interpreter v2----------------------------->

'''

exp = input("Expression: ")

x,y,z = exp.split(" ")

x = float(x)
z = float(z)

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
'''

# interpreter v3----------------------------->
'''

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

'''
# TEST 1 ----------------------------->

'''

def main():


def test(num1, num2):
    result = num1 + num2
    return(result)

tes= test(1,2)
print(tes)

if __name__ = "__main__":
    main()

'''

# TEST 1.v1 ----------------------------->

'''

userinput = input("time: ")

def timesplit(usertime):
    if "am" not in userinput and "pm" not in userinput:
        x,y = userinput.split(":")
        x = int(x)
        if x >= 12:
            x -= 12
        else:
            return(x)
    else:
        timeparts = userinput.split(":")
        x = timeparts[0]
        y = timeparts[1][:2]
        z = timeparts[1][2:]

print(z)
'''

'''

# TEST 1.v2 ----------------------------->

def main():

    time = input("time: ")
    if 7 <= convert(time) <=8: #time between 7 and 8 will be printed as breakfast
        print("breakfast")
    elif 12 <= convert(time) <= 13:
        print("lunch")
    elif 18 <= convert(time) <= 19:
        print("dinner")
    else:
        print("stop thinking of food")



def convert(time):
    if "am" in time or "pm" in time:
        timesplit = time.split(":")
        hour = int(timesplit[0])
        minute = int(timesplit[1][:2])
        period = timesplit[1][2:]
        if "pm" in period and hour != 12:
            hour = hour + 12
        elif "am" in period and hour == 12:
            hour = 0

        return hour + (minute / 60)
    else:
        x,y = time.split(":")
        hour = float(x)
        mins = float(y) * 1 / 60
        return (hour+mins)



if __name__ == "__main__":
    main()


#7-8 breakfast 12-13 lunch 18-19 dinner

'''
