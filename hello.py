aantal = input('hoeveel? ') # 3
prijs = 6

print("Totaal 1: " + prijs * aantal) #333333
print("Totaal 1:", prijs * aantal) #333333

print("Totaal 2: {}".format(prijs * int(aantal))) #18
print("{} x {} = {}".format(aantal, prijs, prijs * int(aantal))) #3 x 6 = 18

totaal = prijs * int(aantal)
print("Totaal 3: " + str(totaal)) #18

print("Totaal 4: " + prijs * int(aantal)) #can only concatenate str (not "int") to str