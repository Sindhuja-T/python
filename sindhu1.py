l=[int(k) for k in input('enter the elements=').split(',')]
#l=[map(int,input().split(','))](use either first line or second line to get input)
print(l)
m=l[0]
for i in range(len(l)):
    if(l[i]>m):
        m=l[i];
print('max=%s'%m)
for i in range(len(l)):
    if(l[i]<m):
        m=l[i];
print('min=%s'%m)


