import random
def ran():
    print(random.randint(1,6))
b=1
while b<=5:
    a=input('do you want the play GAME=')
    if a=='yes' or a=='Yes' or a=='YES' or a=='y' or a=='Y':
        ran()
    if a=='NO' or a=='No' or a=='n' or a=='N' or a=='no':
        print('well played  thankyou....')
    b+=1;

    
    
