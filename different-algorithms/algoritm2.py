n=int(input())
a=n//100
b=n//10%10
c=n%10
new_number=c*100+b*10+a
if new_number==n:
    print("Yes")
else:
    print("No")