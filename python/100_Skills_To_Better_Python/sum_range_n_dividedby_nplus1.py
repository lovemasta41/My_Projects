x = int(input("Enter last no."))
sum = 0.0
for i in range(1,x+1):
    print(i)
    sum += float(i/(i+1))

print(sum)
