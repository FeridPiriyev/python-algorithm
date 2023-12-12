n=int(input())
n_copy=n
polindrome_number=0
while n>0:
    son_reqem=n%10
    polindrome_number=polindrome_number*10+son_reqem
    n=n//10
if polindrome_number==n_copy:
    print("polindrome number")
else:
    print("polindrome deyil")