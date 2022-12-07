from pathlib import Path


data = Path("input1.txt").read_text()
size = len(data)
dest = 0
for i in range(size):
    x = data[i:i+14]
    nd = []
    if len([nd.append(q) for q in x if q not in nd]) == 14:
        dest = i
        print(f"bytes: {i+13}, {data[i+13]}")

        break
    print(x)

print(data[i:i+14])