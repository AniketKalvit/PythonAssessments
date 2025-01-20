a=no=121
result=0
while a!=0:
    rem=a%10
    result=result*10+rem
    a=a//10
    
if result==no:
    print('palindrome ')
else:
    print('not palindrome ')

