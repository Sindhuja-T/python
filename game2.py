import random
x=random.randint(1,9)
def ran():
    i=1
    while i<=5:
        a=int(input('enter any number='))
        print('your random value=',x)
        if a==x:
            print('u won the game!!!!!')
            
        else:
            print('sorry try again....')
        if i==5:
            print('game ended...')
        i+=1
ran();

    
