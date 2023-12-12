# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
regex_pattern = r"^[a-z]{1,3}[0-9]{2,8}[A-Z]{3,}$"

for _ in range(int(input())):
    s = input()
    if re.findall(regex_pattern, s):
        print("VALID")
    else:
        print("INVALID")