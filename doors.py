door = ["closed"] * 100

for a in range(100):
    for b in range(a, 100, a+1):
        if door[b] == "closed":
            door[b] = "open"
        elif door[b] == "open":
            door[b] = "closed"
print("Opened doors:")
for a in range(len(door)):
    if door[a] == "open":
        print(str(a+1), end=", ")