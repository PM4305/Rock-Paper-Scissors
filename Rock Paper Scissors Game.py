import random
def result(inp,comp):
    if inp==comp:
        print("\nIt's a Tie")
        return 0
    elif inp=="Rock" and comp=="Scissors":
        print("\nCongratulations!! You Win")
        return 1
    elif inp=="Rock" and comp=="Paper":
        print("\nYou Lose")
        return -1
    elif inp=="Paper" and comp=="Rock":
        print("\nYou Win")
        return 1
    elif inp=="Paper" and comp=="Scissors":
        print("\nYou Lose")
        return -1
    elif inp=="Scissors" and comp=="Paper":
        print("\nYou Win")
        return 1
    elif inp=="Scissors" and comp=="Rock":
        print("\nYou Lose")
        return -1
    else:
        return 0
    
print("              Rock Paper Scissors Game")
score=0
ch='y'
while ch=='y':
    print("\nPress 'R' for Rock\nPress 'P' for Paper\nPress 'S' for Scissors\n")
    inp=input("Enter your Choice: ")
    comp=random.choice(["Rock","Paper","Scissors"])
    if inp=='R':
        print("\nYour Selection: Rock")
        print("Computer Selection: ",comp)
        score+=result("Rock",comp)
    elif inp=='P':
        print("\nYour Selection: Paper")
        print("Computer Selection: ",comp)
        score+=result("Paper",comp)
    elif inp=='S':
        print("\nYour Selection: Scissors")
        print("Computer Selection: ",comp)
        score+=result("Scissors",comp)
    else:
        print("\n!!Wrong Input!!")
    if score<0:
        score=0
    print("\nYour Current Score: ",score)
    ch=input("\nDo you want to play again (y/n): ")


















    
        
        
        
