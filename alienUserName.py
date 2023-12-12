import re

users = [input() for _ in range(int(input()))]
r = re.compile(r"^[_.]\d+[a-zA-Z]*_?$")
print(*['VALID' if r.search(user) else 'INVALID' for user in users], sep='\n')