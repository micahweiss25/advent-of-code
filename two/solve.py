from pathlib import Path
dict = {"A": "r", "B": "p", "C": "s", "X": "r", "Y": "p", "Z": "s"}
data = Path("text1.txt").read_text()
data = [(dict[i[0]], dict[i[2]]) for i in data.split("\n")]
print(len(data))
sum = 0
for i in data:
    if i[0] == "r" and i[1] == "p" or i[0] == "p" and i[1] == "s" or i[0] == "s" and i[1] == "r":
        sum += 3
    elif i[0] == i[1]:
        sum += 1 
    else:
        sum += 0
    if i[1] == "r":
        sum += 1
    elif i[1] == "p":
        sum += 2
    else:
        sum += 3
print(sum)
