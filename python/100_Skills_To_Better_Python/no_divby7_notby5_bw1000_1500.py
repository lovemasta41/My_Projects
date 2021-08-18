l=[]
for i in range(1000, 1500):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print(l)
t = ','.join(l)
print(t)