string = input()
G_count = 0
F_count = 0

for i in string:
    if i == "G":
        G_count += 1
    elif i == "F":
        F_count += 1


if G_count > F_count:
    print(F_count)
else:
    print(G_count)