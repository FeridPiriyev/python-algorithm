'''
ededin polindrom olub-olmamasini yoxla
'''
# n=int(input())
# n_copy=n
# polindrome_number=0
# while n>0:
#     son_reqem=n%10
#     polindrome_number=polindrome_number*10+son_reqem
#     n=n//10
# if polindrome_number==n_copy:
#     print("yes")
# else:
#     print("no")

eded=input()
eded_copy=eded
polindrome_number=" "
for i in eded:
    polindrome_number=i+polindrome_number
if int(polindrome_number)==int(eded_copy):
    print("yes")
else:
    print("no")