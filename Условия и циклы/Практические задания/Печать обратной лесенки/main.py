count_stairs = 4
# TODO распечатать лесенку
stair = []
star = "*"
for i in range(4):
    stair.append(star)
    star += "*"

for s in stair[::-1]:
    print(s)