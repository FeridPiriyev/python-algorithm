n=int(input())
n_copy=n
maks=0
maks_say=0
while n>0:
    a=n%10
    if a>maks:
        maks=a
        n=n//10
    else:
        n=n//10
while n_copy>0:
    c=n_copy%10
    if c==maks:
        maks_say+=1
    n_copy=n_copy//10
print(maks_say)
