import re

regex_pattern = r'(<\w+)\s(\w+)|<\w'
n = input()
string = list()
for _ in range(int(n)):
    s = input()
    string.append(s)

str = ""
str = "\n".join(string)
print(str)