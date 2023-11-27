f = open("movies.dat", "r")

lines = f.read().splitlines()

for line in lines:
    if lines[len(lines) - 1] == "":
        lines.pop()

last_line = lines[len(lines)-1].split(", ")
last_id = last_line[0]
