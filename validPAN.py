# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

regex_pattern = (r"^[A-Z]{5}[0-9]{4}[A-Z]$")
for _ in range(int(input())):
    s = input()
    if re.findall(regex_pattern, s):
        print("YES")
    else:
        print("NO")
    