import re
items = ["techotd(.com)","theverge(.com)","edx(.org)"]
for item in items:
    print(re.sub(r" ?\([^)]","", item))
