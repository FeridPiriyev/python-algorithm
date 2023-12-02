#tenlik verilir. y=x**4-(5*x/sqrt(x**2-4))+abs(PI-x). y tap
import math
x=int(input())
if -2<=x<=2:
    print("False")
else:
    y=pow(x,4)-((5*x)/math.sqrt(pow(x,2)-4))+abs(math.pi-x)
    print(y)