f = open("marks.txt", "rt")
marks_list = {}
for line in f.readlines():
    # ignore lines without ,
    line = line.strip("\n")
    if ',' not in line:
        continue

    rollno, marks = line.split(',')
    if len(rollno) == 0 or len(marks) == 0:
        continue

    try:
        marks = int(marks)
        if rollno in marks_list:
            marks_list[rollno] += marks  # add marks to existing total
        else:
            marks_list[rollno] = marks  # add a new entry with marks
    except:
        pass

f.close()

for rollno, total in marks_list.items():
    print(rollno, total)
