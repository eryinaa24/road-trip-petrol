distance=float(input("Enter a distance in km: "))
while distance<0 or distance>2000:
    print("Invalid distance. Please enter a distance between 0 to 2000km.")
    distance=float(input("Enter a distance in km: "))

car_petrol=float(input("Enter a car's petrol use in litre per 100km: "))
while car_petrol<1 or car_petrol>20:
    print("Invalid car's petrol use. Please enter a car's petrol use between 1 to 20litre per 100km.")
    car_petrol=float(input("Enter a car's petrol use in litre per 100km: "))

price=float(input("Enter a price in RM: "))
while price<1 or price>10:
    print("Invalid price. Please enter a price between 1 to 10.")
    price=float(input("Enter a price per litre in RM: "))

people=int(input("Enter a number of people: "))
while people<1 or people>10:
    print("Invalid number of people. Please enter between 1 to 10.")
    people=int(input("Enter a number of people: "))

total_petrol=(distance*car_petrol)/100
total_price=total_petrol*price
per_person=total_price/people
print(f"{total_price:.2f}")
print(f"{per_person:.2f}")
