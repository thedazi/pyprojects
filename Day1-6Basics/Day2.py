#print(Hello[3])
#will only print the second 'l' because couting starts at 0
#integer = whole numbers
#float = number with decimal
#string = letters marked by ""
#len() = length of strings
#type() = gives you the type of data
#type casts str(), int(), bool(), float()
#round(x, y) will round x and y will specific to what number it will round to
#f-string: f"your something something {variable} is sooo big" will print the variable into the statement without needing to convert the item

print("Welcome to the tip calculator!")
bill_amount = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like you give? 10, 12, or 15? "))
split_amount = int(input("How many people to split the bill? "))
calc = round((bill_amount * (1+tip/100)) / split_amount, 2)
calc = "{:.2f}".format(calc)

print(f"Each person should pay: ${calc}")