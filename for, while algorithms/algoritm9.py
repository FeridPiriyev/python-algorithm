'''
[a;b] parçasında sadə ədədləri çap edə proqram
'''
# n=int(input())
# lamp=1
# kok=int(math.sqrt(n))
# for i in range(2,kok+1):
#     if n%i==0:
#         lamp=0
#         break
# if lamp==1 and n!=1:
#     print("sadedir")
# else:
#     print("sade deyil")
import math
a=int(input())
b=int(input())
lamp=1
for i in range(a,b+1):
    kok=int(math.sqrt(a))
    if a%i==0:
        lamp=0
        break
    if lamp==1 and a!=1:
        print(a)