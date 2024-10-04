greet = input("Greetings: ").lower().strip() #ask for the greetings, convert to lowercase and remove whitespace

if greet.startswith("hello"): #if greetings starts with hello
    print("$0")               #give $0
elif greet.startswith("h"):   #if greetings starts with h
    print("$20")              #give $20

else:                         #else
    print("$100")             #give $100
