name = "hoveven"

for i in range(0, len(name)):
    if name[i] == "v":
        name = name[0:i] + "p" + name[i+1:len(name)]

print(name)
