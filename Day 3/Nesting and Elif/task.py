print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("What is your age? "))
    if age <= 12:
        bill=5
        print("Children tickets are $5")
    elif age <= 18:
        bill=7
        print("Teenager tickets are $7.")
    else:
        bill=10
        print("Adult tickets are $10.")
    photo=input("Do you want a photo? Type y for yes and n for no: ")
    if photo == "y":
        bill+=3
    print(f"You have to pay ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")
