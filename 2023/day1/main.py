import re

file = open('data.txt', 'r')
data = file.readlines()

sum = 0
pat = '(\\d).*?(\\d)?(?!.*\\d)'
for d in data:
    m = re.search(pat, d.strip('\n'))
    if m is None:
        continue
    f, l = m.groups()
    if l is None:
        l = f
    sum += int(f + l)

print(sum)
