from pathlib import Path; print(sum(sorted([sum(map(lambda x: int(x), n.split("\n"))) for n in Path("text.txt").read_text().split("\n\n")], reverse=True)[:3]))
