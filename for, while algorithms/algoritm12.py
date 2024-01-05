'''
Daxil edilmish ededin reqemlerinin hamisinin ferqli olub-olmadiginin yokhla
'''
n=int(input())
lamp=1
while n>0:
    r=n%10
    n=n//10
    temp=n
    while temp>0:
        d=temp%10
        if r==d:
            lamp=0
            break
        temp=temp//10
if lamp==1:
    print("ferqlidir")
else:
    print("ferqli deyil")