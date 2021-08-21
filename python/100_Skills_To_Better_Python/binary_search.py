import math
def binaryS(li,el):
    bottom = 0
    top = len(li) - 1
    index = -1
    while top>=bottom and index==-1:
        mid=int(math.floor((top+bottom)/2.0))
        if li[mid] == el:
            index = mid
        elif li[mid] > el:
            top = mid-1
        else:
            bottom = mid + 1

    return index

li = [2,4,6,8,9,12,15]
print(binaryS(li,2))
print(binaryS(li,11))



