print("***Markete xosh geldin***")
print("Ne qeder pulun var?")
n=int(input())
if n<=100:
    print("sen nausnik ala bilərsən(80manat)")
elif 1000>=n>=600:
    print("Sen telefon ala bilersen. Pulun var!")
    print("1-nausnik(80 manat)","2-telefon(520 manat)",sep="\n")
    ortaqiymet=int(input("Hansini isteyirsen?"))
    if ortaqiymet==1:
        print("Congrutalations nausnik aldin.", n-80, "manatin qaldi")
    elif ortaqiymet==2:
        print("Telefon aldin",n-520, "manatin qaldi")
    else:
        print("Yanlish əməliyyat")
elif n>=1000:
    print("Sen komputer ala bilersen")
    print("1-nausnik(80manat)","2-telefon(520 manat)","komputer(940manat)",sep="\n")
    aliqarx=int(input())
    if aliqarx==1:
        print("Congrutalations nausnik aldin.", n-80, "manatin qaldi")
    elif aliqarx==2:
        print("Telefon aldin.",n-520, "manatin qaldi")
    elif aliqarx==3:
        print("Komputer aldin.", n-920, "manatin qaldi")
    else:
        print("Yanlish əməliyyat")