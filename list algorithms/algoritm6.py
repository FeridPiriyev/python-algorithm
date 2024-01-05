'''
men boyuk cut reqem ile en kicik tek ededin cemi
'''
eded=input()
lamp=0
min_tek=1
for i in eded:
    if int(i)%2==1 and lamp==0:
        min_tek=int(i)
        lamp=1
for i in eded:
    if int(i)%2==0:
        max_cut=int(i)
    if int(i)<min_tek and int(i)%2==1:
        min_tek=int(i)
print(max_cut+min_tek)