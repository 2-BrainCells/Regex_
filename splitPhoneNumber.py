import re

regex_pattern = r"(^\d{1,2})(?:\s|\S)(\d{1,3})(?:\s|\S)(\d{4,10})$"

for _ in range(int(input())):
    s = input()
    a = re.findall(regex_pattern, s)
    print(f"CountryCode={a[0][0]},LocalAreaCode={a[0][1]},Number={a[0][2]}")
