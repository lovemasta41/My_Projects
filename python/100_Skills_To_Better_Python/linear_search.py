def sequentialsearch(li,item):
    pos=0
    found=False
    while pos<len(li) and not found:
        if li[pos] ==item:
            found = True
        else:
            pos=pos+1
    return found,pos

print(sequentialsearch([2,4,6,8,9,5,2],2))   