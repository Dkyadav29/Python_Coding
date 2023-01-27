print("WELCOME TO PIZZA DELIVHERY!")
size = input("enter the size of pizza ?S, M, L ")
add_peporponi = input("do you want add_peporponi ? Y , N ")
add_chess = input("are you want add extra chess ?Y,N ")
bill = 0

if size =="S":
    bill += 15
elif size =="M":
    bill += 20
elif size =="M":
    bill += 30
    
else:
    print("plese select the pizza size")

if add_peporponi == "Y":
    if size == "S":
        bill += 20
    else:
        bill += 15
            
if add_chess == "Y":
    bill += 1
    
if bill >= 0:
    print("PLEASE CHOOSE THE PIZZA SIZE")
else :
    print("select pizza")

   
