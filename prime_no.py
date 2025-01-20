#prime number

a=7
i=2
flag=1
while i<a:
    if a%i==0:
        flag=0
        break
    i=i+1
if flag==1:
    print('prime number')
else:
    print('not prime')
        

