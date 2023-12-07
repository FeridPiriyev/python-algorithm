'''
daxil edilmis reqemleri muxtelif 3 reqemli natural ededin en boyuk reqemi ile en kicik reqeminin yerini
deyisdirerek yeni eded yaradan proqram #718--781  123--321 
'''

n=int(input())
a=n//100
b=n//10%10
c=n%10
if a>b and a>c:
    if b>c:
        print(c*100+b*10+a)
    else:
        print(b*100+a*10+c)
elif b>a and b>c:
    if a>c:
        print(a*100+c*10+b)
    else:
        print(b*100+a*10+c)
else:
    if a>b:
        print(a*100+c*10+b)
    else:
        print(c*100+b*10+a)