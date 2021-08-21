x=int(input("enter a number:"))
a = list()
def evengen(n):
    for i in range(0,n):
        if i%2 == 0:
            a.append(str(i))
    print(a)
    z=",".join(a)
    print(z)

print(evengen(x))