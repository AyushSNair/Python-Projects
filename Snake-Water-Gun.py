import random
print("1.Snake 2.Water 3.Gun")
user_choice = int(input("Enter Your Choice  "))
computer_choice = (random.randrange(1,3))
if(user_choice == 1):
    if(computer_choice == 1):
        print("You Chose Snake Computer Chose Snake . Draw")
    elif(computer_choice == 2):
        print("You Chose Snake Computer Chose Water . You Win")
    elif(computer_choice == 3):
        print("You Chose Snake Computer Chose Gun . You Loose")
elif(user_choice == 2):
    if(computer_choice == 1):
        print("You Chose Water Computer Chose Snake . You Loose")
    elif(computer_choice == 2):
        print("You Chose Water Computer Chose Water . Draw")
    elif(computer_choice == 3):
        print("You Chose Water Computer Chose Gun . You Win")
elif(user_choice == 3):
    if(computer_choice == 1):
        print("You Chose Gun Computer Chose Snake . You Win")
    elif(computer_choice == 2):
        print("You Chose Gun Computer Chose Water . You Loose")
    elif(computer_choice == 3):
        print("You Chose Gun Computer Chose Gun . Draw")





