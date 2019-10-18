import os


def print_file(filename):
    print("\n" + filename)
    print("=" * len(filename))
    with open(filename, "rt") as f:
        lineno = 1
        for line in f:
            print(f"{lineno:03}:{line}", end='')
            lineno += 1


startdir = r"e:\classroom\python\sep27"

for dirname, dirs, files in os.walk(startdir):
    for f in files:
        if f.endswith(".py"):
            print_file(dirname + "\\" + f)
