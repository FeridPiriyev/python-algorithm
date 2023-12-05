'''
İki natural a və b ədədləri verilmişdir. a-nın b-yə bölünməsindən alınan tam hissəni və qalığı çap edin.
a-nın b-yə bölünməsindən alınan tam hissəni və qalığı çap edin.

e-olymp mesele 8522
'''

a,b=map(int,input().split())
if a%b==0:
    print("Divisible")
else:
    print(a//b,a%b)