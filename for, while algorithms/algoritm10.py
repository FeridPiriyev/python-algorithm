'''
n sayda daxil edilen ededin uchreqemli olanlarinin sayini tap
'''
n=int(input())
say=0
for i in range(n):
    a=int(input())
    if a>99 and a<1000:
        say=say+1
print(say)
