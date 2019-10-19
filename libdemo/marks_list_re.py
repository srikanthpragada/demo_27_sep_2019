import re

f = open("marks2.txt", "rt")
marks_list = {}
for line in f.readlines():
    # ignore lines without rollno and marks
    m = re.fullmatch(r"(\d+)\D+(\d+)\D+", line)
    if m is None:
        continue

    try:
        rollno = m.group(1)
        marks = int(m.group(2))
        if rollno in marks_list:
            marks_list[rollno] += marks  # add marks to existing total
        else:
            marks_list[rollno] = marks  # add a new entry with marks
    except:
        pass

f.close()

for rollno, total in marks_list.items():
    print(rollno, total)
