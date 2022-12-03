from pathlib import Path

# split the text by lines
data = Path("input.txt").read_text().split()

# iterator throught the lines, split each in half, and return halfs as tuples
data = [(x[:len(x)//2], x[len(x)//2:]) for x in data]

# find the common value between the two halves
#a = [i for x in data for i in x[0]  if i in x[1]]
a = []
for x in data:
    for i in x[0]:
        if i in x[1]:
            a.append(i)
            break

# convert value to "priority" and sum list to find the total priority 
#print(sum(a.map(lambda x: x - 96 if x.islower() else x - 64)))
print(sum([ord(x) - 96 if x.islower() else ord(x) - 38 for x in a ]))
