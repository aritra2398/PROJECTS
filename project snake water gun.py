# making the snake water gun game
import random
def game(comp,you):
    if comp == you:
        print("its a draw")
    elif comp =="S":
        if you== "g":
            print("you won")
        elif you == "w":
            print("you lose")
    elif comp =="g":
        if you== "w":
            print("you won")
        elif you == "s":
            print("you lose")
    elif comp =="w":
        if you== "s":
            print("you won")
        elif you == "g":
            print("you lose")
    
    
        


    
print("the computer selects snake(s),water(w),gun(g)")
random_no = random.randint(1,3)
if random_no == 1:
    comp ="s"
elif random_no ==2:
    comp = "w"
else:
    comp = "g"
   
you = input("the player selects snake(s),water(w),gun(g)")  


print("the computer shows" ,comp)
game(comp,you)