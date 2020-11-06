#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print ("Welcome to the tip calculator.")
total = float(input ("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
numberOfPeople = int(input("How many people to split the bill? "))

perPerson = total * (1 + percentage/100) / numberOfPeople

roundedAmount = round(perPerson, 2)

print (f"Each person should pay: ${roundedAmount}")
