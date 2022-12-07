from pathlib import Path


data = Path("input1.txt").read_text()
size = len(data)
dest = 0
for i in range(size):
    x = data[i:i+4]
    nd = []
    if len([nd.append(q) for q in x if q not in nd]) == 4:
        dest = i
        print(f"bytes: {i+3}, {data[i+3]}")

        break
    print(x)

print(data[i:i+4])