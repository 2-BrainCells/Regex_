# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

regex_pattern = r"^(?:h|H)(?:i|I)\s[^Dd].*$"

for _ in range(int(input())):
    s = input()
    if re.findall(regex_pattern, s):
        print(s)