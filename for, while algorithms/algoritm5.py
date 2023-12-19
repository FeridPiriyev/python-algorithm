'''
Iki eded daxil edilir. Ededin ebobu ve ekobu arasinda olan ededlerden 3 e boldukde qaliqda 3 olanlarinin
sayini tap
'''

num1=int(input())
num2=int(input())
num1_copy=num1
num2_copy=num2
num_say=0
while num1!=num2:
    if num1>num2:
        num1=num1-num2
    else:
        num2=num2-num1
ebob=num1
ekob=(num1_copy*num2_copy)//ebob
while ebob<ekob:
    ebob=ebob+1
    if ebob%3==1:
        num_say=num_say+1
print(num_say)