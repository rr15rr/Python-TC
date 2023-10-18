#Tip Calculator Program

country = input("Choose a country: (Mexico, United States, Canada)\n ")

if country == "Mexico" or country == "mexico":
    print("\nIn Mexico, the normal tip percentage is 10%\n")
    bill    = int(input("Indicate the total cost of the bill: "))
    tip = bill * 10/100
    print("\nThe total tip you must pay is of: " + str(tip) + "$ Mexican pesos\n" )



if country == "USA" or country == "United States" or country == "US" or country == "us" or country == "usa":
    print("\nIn the United States, the normal tip percentage is 20%\n")
    billUS = int(input("Indicate the total cost of the bill: "))
    tipUS = billUS * 20/100
    print("\nThe total tip you must pay is of: " + str(tipUS) + "$ United States Dollars\n")

if country == "Canada" or country == "canada":
    print("\nIn Canada, the normal tip percentage is 15%\n")
    billC = int(input("Indicate the total cost of the bill: "))
    tipC = billC * 15/100
    print("\nThe tital tip you must pay is of: " + str(tipC) + "$ Canadian Dollars\n")