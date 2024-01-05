'''
butun reqemlerinin eyni olub-olmadigini yokhlayan algoritm
'''
eded=input()
a=int(eded)%10
lamp=0
for i in eded:
    if a==int(i):
        lamp=0
        a=int(i)
    else:
        lamp=1
        break
if lamp==0:
    print("eynidir")
else:
    print("eyni deyil")