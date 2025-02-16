signal = True
while signal:
    s1={'stone','paper','scissor'}
    l1=list(s1)
    res=l1[0]
    inp = input("enter stone, paper or scissor: ")
    
    print("Your opponent is :",res);

    if(res==inp):
        print("It's a Tie")
    elif((res=="stone" and inp=="paper") or
         (res=="paper" and inp=="scissor") or
         (res=="scissor" and inp=="stone")):
        print("You won the Game")
    else:
        print("Your Opponent won the game");
        

    inp2=input("Do You want to play again? yes/no: ")

    if(inp2=="yes" or inp2=="Yes" or inp2=="YES"):
        signal= True;
    else:
        signal= False;
                                           
'''
import random
i=random.randint(1,3)
print(i)
'''
