# Display rollno and marks in sorted order of rollno

markslist = {}

while True:
    rollno = int(input("Enter rollno [0 to stop] :"))
    if rollno == 0:
        break

    marks =input("Enter marks  :")
    if rollno in markslist:
        markslist[rollno].append(marks)  # Add to existing list
    else:
        markslist[rollno] = [ marks ]  # Create new list with marks

for r, m in sorted(markslist.items()):
    print(f"{r:3} {','.join(m)}")
