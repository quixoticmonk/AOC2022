original_list = []
offset_value_set = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
count = 0

for line in open("input.txt"):
    x, y, z = line.split(",")
    original_list.append((int(x), int(y), int(z)))


for x, y, z in original_list:
    for dx, dy, dz in offset_value_set:
        if (x + dx, y + dy, z + dz) not in original_list:
            count += 1

print(count)
