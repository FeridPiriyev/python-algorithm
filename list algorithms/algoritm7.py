eded=input()
a=len(eded)
cem=0
for i in eded:
    cem=cem+int(i)**a
if cem==int(eded):
    print("armstrongdur")
else:
    print("armstrong deyil")