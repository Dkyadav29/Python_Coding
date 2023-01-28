print("WELCOME TO ROLER COSTER ")
height = int(input("Enter the your height "))
total_charge = 0

if height >= 120:
    print("You can ride ")
    age = int(input("Enter the your age "))

    if age < 12:
        total_charge += 5
    if age > 18:
        total_charge += 5
    elif age >= 45 and age <= 55:
            total_charge = 0
   
    do_want_pic = ("do you want click pic ? Y or N")
    if do_want_pic == "Y":
        total_charge +3
else:
  print("Sorry, you have to grow taller before you can ride.")


