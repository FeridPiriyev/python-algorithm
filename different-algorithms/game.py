a,b=map(int,input().split())
if a==b:
    print(0)
elif abs(a-b)==1:
    print(2)
else:
    eded=abs(a-b)
    count=eded//3
    qaliq=eded%3
    second_count= qaliq // 2
    if qaliq == 1:
        print(count+second_count+1)
    else:
        print(count+second_count)