'''
Növbəti şərtə uyğun olaraq y-in qiymətini hesablayın:
y={ 
1.x**2−3x+4,x<5
2.x+7,x≥5
}

e-olymp mesele 8520
'''

x=int(input())
if x<5:
    y=x**2-3*x+4
    print(y)
else:
    print(x+7)