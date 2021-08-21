def longesteword():
    with open("test.txt", 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longesteword())