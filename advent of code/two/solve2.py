dictl = {"r": "s", "p": "r", "s": "p"}
dictw = {"r": "p", "p": "s", "s": "r"}

with open("text2.txt", "r") as f:
    data = f.read().split("\n")
    sum = 0
    for i in data:
        ans = ""
        if i[2] == "w":
            sum += 6
            ans = dictw[i[0]]
        elif i[2] == "l":
            sum += 0
            ans = dictl[i[0]]
        else:
            sum += 3
            ans = i[0]
        
        if ans == "r":
            sum += 1
        elif ans == "p":
            sum += 2
        else:
            sum += 3
        
    print(sum)