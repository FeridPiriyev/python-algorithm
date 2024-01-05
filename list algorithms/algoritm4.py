'''
Daxil edilmis natural ededin reqemlerinin ededi ortasini tapin
'''

eded=input()
cem=0
say=0
for i in eded:
    cem=cem+int(i)
    say=say+1
print(cem//say)