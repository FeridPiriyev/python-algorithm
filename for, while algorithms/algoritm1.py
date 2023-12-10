'''
Bir eded daxil edilir, ededin butun mertebelerinin eyni oldugunu yoxlayan algortim
#111111--yes    #11111231--no
'''
n=int(input())
a=n%10
b=n//10
lamp=0
while b>0:
    c=b%10
    if a==c:
        b=b//10
    else:
        lamp=1
        b=b//10
if lamp==1:
    print("no")
else:
    print("yes")

