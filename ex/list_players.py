from datetime import datetime

f = open("players.txt", "rt")
players = {}

today = datetime.now()
for line in f:
    parts = line.strip("\n").split(",")
    if len(parts) < 2:
        continue
    try:
        dob = datetime.strptime(parts[1], "%d-%m-%Y")
        years = (today - dob).days // 365  # calculate age in years
        players[parts[0]] = years  # add name and age in years to dict
    except:
        pass

for name, age in sorted(players.items(), key=lambda t: t[1]):
    print(f"{name:10}  {age}")
