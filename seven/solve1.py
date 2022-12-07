from pathlib import Path
import re

data = Path("input.txt").read_text().split("\n")

class Dir:
    def __init__(self, name, parent):
        # dir name
        self.name = name
        self.parent = parent
        # dir stores Dir's
        self.dir = {}
        # file stores file name and size
        self.files = {}
        self.size = 0

    def print_dir(self, lvl):
        lvl = lvl
        string = "\t" * lvl + "dir: " + self.name 
        print(string)
        for key in self.files:
            string = "\t" * (lvl + 1) + f"file: {key}, size: {self.files[key]}"
            print(string)
        for key in self.dir:
            self.dir[key].print_dir(lvl+1)
        
    def count(self):
        num = 0
        for key in self.dir:
            num += self.dir[key].count()
        num += self.size
        return num

    def add_dir_size(self):
        for key in self.dir:
            self.size += self.dir[key].size

    def go_to_parent(self):
        x = self
        while x.name != "/":
            x = x.parent
        return x

def parse(data):
    pwd = Dir("top", "parent")
    pwd.dir["/"] = Dir("/", pwd)
    # index of data
    idx = 0
    data_len = len(data)
    while idx < data_len:
        line = data[idx]
        if "$ cd" in line:
            cmd = re.search('[$] cd ([a-zA-Z/..]+)', line)
            if ".." in line:
                '''change working directory to current dir's parent '''
                pwd = pwd.parent
            else:
                '''change pwd to current dir object from parent's dirs'''
                pwd = pwd.dir[cmd.group(1)]
        elif "$ ls" in line:        
            pass
        else:
            if "dir" in line:
                '''create a dir '''
                cmd = re.search("dir ([a-zA-Z]+)", line)
                new_dir = Dir(cmd.group(1), pwd)
                pwd.dir[cmd.group(1)] = new_dir
            else:
                cmd = re.search("([0-9]+) ([a-zA-Z]+)", line)
                pwd.files[cmd.group(2)] = cmd.group(1)
                pwd.size += int(cmd.group(1))
        idx += 1
    return pwd

def count_lt(curr, pwd):
    for key in pwd.dir:
        count = pwd.dir[key].count()
        if count <= 100000:
            curr = count_lt(curr+count, pwd.dir[key])
        else:
            curr = count_lt(curr, pwd.dir[key])
    return curr

def closest(pwd,list):
    list.append((pwd.count(),pwd.name))
    for key in pwd.dir:
        closest(pwd.dir[key],list)
    return list


directories = parse(data)
pwd = directories.go_to_parent()
list = []
print("\n")
list = closest(pwd,list)
smallest = (100000000000000000,"tmp")
for num in list:
    if num[0] < smallest[0] and num[0] > 2080344:
        smallest = num
print(smallest)
print()

