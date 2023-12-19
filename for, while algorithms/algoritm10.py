# n=int(input())
# i=1
# say=0
# while i<=n:
#     a=int(input())
#     if a>99 and a<1000:
#         say=say+1
#     i=i+1
# print(say)
n=int(input())
say=0
for i in range(n):
    a=int(input())
    if a>99 and a<1000:
        say=say+1
print(say)
