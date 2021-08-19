l = []
x = input("Enter list of Nos.")
for i in x.split(","):
    if int(i)%2 != 0:
        l.append(str(int(i)**2))
    #if i%2 != 0:
     #   l.append(i**2)

#print(','.join(l))
print(','.join(l))

