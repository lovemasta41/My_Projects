senetence=input("Please provide a sentence:")
upperC = 0
lowerC = 0
dictt=dict()
dictt = {'upperC':0,'lowerC':0}
for char in senetence:
    if char.isupper():
        dictt['upperC'] = dictt['upperC'] + 1
    if char.islower():
        dictt['lowerC'] = dictt['lowerC'] + 1

print("No. Of upper Char:",dictt['upperC'])
print("No. Of lower Char:",dictt['lowerC'])
print(dictt)
