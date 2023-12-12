# Enter your code here. Read input from STDIN. Print output to STDO
import re
pattern = list()
regex_pattern = (r'(?:h|H)\w{5}(?:r|R)\w{3}')
for _ in range(int(input())):
    string = input()
    if re.findall(regex_pattern, string):
        pattern.append(string)

print(pattern)
print(len(pattern))
    