'''
daxil edilmis 3 reqemli natural ededin armstrog olub-olmadigini yoxlayan algoritm
armstrong ededler ededin mertebelerinin kublari cemi 153=1**3+5**3+3**3 eded armstrongdur
'''

n=int(input())
a=n//100
b=n//10%10
c=n%10
if a**3+b**3+c**3==n:
    print("Armstrongdur")
else:  
    print("Armstrong deyil")
