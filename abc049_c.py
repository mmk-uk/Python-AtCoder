import re
s = input()
m = re.fullmatch(r"(dreamer|dream|erase|eraser)+", s)

if m:
    print("YES")
else:
    print("NO")
