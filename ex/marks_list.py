# Display rollno and marks in sorted order of rollno

markslist = {}

while True:
    rollno = int(input("Enter rollno [0 to stop] :"))
    if rollno == 0:
        break

    marks = int(input("Enter marks  :"))
    markslist[rollno] = marks  # rollno is key, marks is value

for r, m in sorted(markslist.items()):
    print(f"{r:3} {m}")
