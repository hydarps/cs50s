meal = input("How much is the meal?: ") #ask for the meals dollar value
meal_float = float(meal.replace("$", "")) #convert str to float and remove the dollar sign

tip = input("What percentage would you like to tip?: ") #ask for the tip percentage
tip_float = float(tip.replace("%", "")) #convert str to float

percentage = (tip_float / 100) * meal_float #calculate percentage

print ("Leave: " + str(percentage))
