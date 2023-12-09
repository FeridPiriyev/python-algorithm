'''
daxil edilmis 3 reqemli natural ededin tersine ozune beraber olub-olmadigini yoxlayan proqram tertib edin
171(171) --yes 781(187) -- no
'''
n=int(input())
a=n//100
b=n//10%10
c=n%10
new_number=c*100+b*10+a
if new_number==n:
    print("Yes")
else:
    print("No")