'''
Növbəti şərtə uyğun olaraq y-in qiymətini hesablayın:
y={ 
1.x**3+5x,x>=10
2.x**2-2x+4,x<10
}

e-olymp mesele 8521
'''

x=int(input())
if x>=10:
    y=pow(x,3)+5*x
    print(y)
else:
    y=pow(x,2)-2*x+4
    print(y)