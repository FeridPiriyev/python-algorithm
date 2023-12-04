'''
n tam ədədi verilmişdir. Onun müsbət, mənfi və ya 0-a bərabər olmasını müəyyənləşdirin.
n-in qiymətindən asılı olaraq "Positive", "Negative" və ya "Zero" çap edin.
e-olymp mesele 8242
'''

n=int(input())
if n>0:
    print("Positive")
elif n==0:
    print("Zero")
else:
    print("Negative")