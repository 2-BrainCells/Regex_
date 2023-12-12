import re
N = int(input())
S = "\n".join([input() for _ in range(N)])
q = int(input())
for _ in range(q):
    i = input()
    count = len(re.findall(f"\B{i}\B",S))
    print(count)