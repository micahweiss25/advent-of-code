from pathlib import Path

# Read the text from the file and split by new line
data = Path("input.txt").read_text().split()

# create groups of each three line
length = len(data) - 1
data = [data[i:i+3] for i in range(0, length, 3)]

# find common value within group
l = []
for i in data:
    for guess in i[0]:
        if guess in i[1] and guess in i[2]:
            l.append(guess)
            break

# sum the priorities of each groups common letter
print(sum([ord(x) - 96 if x.islower() else ord(x) - 38 for x in l]))