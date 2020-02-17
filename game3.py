s='1-go to college'
i='2-go on vacation'
n='3-take rest'
d='4-play games'
h='q-quit'
print('1-go to college')
print('2-go on vacation')
print('3-take rest')
print('4-play games')
print('q-quit')
m=1
while m>1:
    a=input('enter ur choice=')
    if a=='1':
        print(s)
    if a=='2':
        print(i)
    if a=='3':
        print(n)
    if a=='4':
        print(d)
    if a=='q' or 'Q':
        print('ended!!!!')
        break
    m+=1
