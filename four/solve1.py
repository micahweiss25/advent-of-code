from pathlib import Path
import re

data = Path("input.txt").read_text().split()
count = 0
for i in data:
    z = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", i)
    x = set([x for x in range(int(z.group(1)), int(z.group(2))+1)])
    y =  set([x for x in range(int(z.group(3)), int(z.group(4))+1)])
    if x.issubset(y) or y.issubset(x):
        count += 1
print(count)