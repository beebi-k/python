# sum od alter numder 2544

num=541
total=0
sign=1
for i in str(num):
    total+=sign*int(i)
    sign*=-1
print(total)


n=[13,24,56,78]
ans=[]
for i in n:
    for dig in str(i):
        ans.append(int(dig))
print(ans)
