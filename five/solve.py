from pathlib import Path
import re

steps = Path("input1.txt").read_text().split("\n") # steps
crates = Path("input2.txt").read_text().split("\n") # stack config

# create stacks
# first in first out
lol = [[] for x in range(0, 9)]
for line in crates[:-1]:
    index = 1
    while index < len(line):
        if line[index] != " ":
            lol[(index - 1) // 4].append(line[index]) 
        index += 4
    

for line in steps:
    z = re.match(r"[a-z ]+([0-9]+)[a-z ]+([0-9]+)[a-z ]+([0-9]+)", line)
    print(f"move {z.group(1)} from {z.group(2)} to {z.group(3)}")
    count = 0
    # NUMBER OF CRATES TO MOVE
    for x in range(0, int(z.group(1))):
        count += 1
        swap = lol[int(z.group(2))-1].pop(0)
        lol[int(z.group(3))-1].insert(0, swap)
    print(count)
for l in lol:
    print(l[0])