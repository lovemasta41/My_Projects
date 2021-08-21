import re
text = "Clearly, he felt she was inexcusably wrong!"
for m in re.finditer(r"\w+ly", text):
    #print(m)
    print(m.start(), m.end(), m.group(0))

