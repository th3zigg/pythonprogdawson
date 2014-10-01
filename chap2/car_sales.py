# Car Salesman program
# A user enters the base price of a car and program outputs

base_price = int(input("Please enter base price: "))

vat = 0.2*base_price

admin_fee = 80

road_tax = 150

insurance = 200

total = base_price + vat + road_tax + insurance

print("Total including admin_fee of " + str(admin_fee) + ", road tax at "+str(road_tax)+", insurance at "+str(insurance)+" and VAT at 20%:", total)
