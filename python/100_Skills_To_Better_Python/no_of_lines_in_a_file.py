def no_oflines():
    lines = open("test.txt",'r')
    i=0
    for line in lines:
        i = i + 1
    print("No of lines in the file are:",i)

no_oflines()

