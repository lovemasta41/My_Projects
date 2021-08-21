x = ["12","24","35","24","27"]
y = []
for i in x:
    if i in y:
        continue
    else:
        y.append(i)

print(y)
