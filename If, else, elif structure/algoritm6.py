'''
Şagirdin dərs nailiyyətlərinin səviyyəsini (ilkin, orta, kafi, yüksək) verilmiş qiymətlərə (1-dən 12-dək) uyğun olaraq müəyyənləşdirin.
İlkin səviyyə üçün Initial (1-dən 3-ə qədər), orta üçün Average (4-dən 6-ya qədər), kafi üçün Sufficient (7-dən 9-a qədər) və yüksək səviyyə üçün High (10-dan 12-yə qədər) sözlərini çıxışa verin.
e-olymp algorithm 902
'''

n=int(input())
if 1<=n<=3:
    print("Initial")
elif 4<=n<=6:
    print("Average")
elif 7<=n<=9:
    print("Sufficient")
elif 10<=n<=12:
    print("High")