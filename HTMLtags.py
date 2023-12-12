import re
N = int(input())
box = []
for i in range(N):
    s = input()
    regex_pattern = re.findall(r"<\s*[A-Za-z0-9]+\s*>?", s)
    for i in regex_pattern:
        x = i.replace("<","").replace(">","").strip()
        box.append(x)

print(";".join(sorted(list(set(box)))))