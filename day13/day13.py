import functools
with open("input.txt", "r") as f:
    lines = f.read().split("\n\n")


def compare_inputs(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        inc = 0
        while inc < len(left) and inc < len(right):
            cop = compare_inputs(left[inc], right[inc])
            if cop !=0:
                return cop
            inc += 1
        if inc == len(left) and inc < len(right):
            return -1
        elif inc < len(left) and inc == len(right):
            return 1
        else:
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return compare_inputs([left], right)
    else:
        return compare_inputs(left, [right])

packets=[]
index = 1
count_index = 0
for line in lines:
    left=eval(line.split("\n")[0])
    right=eval(line.split("\n")[1])
    packets.append(left)
    packets.append(right)
    if compare_inputs(left ,right) == -1:
        # print(f"index is {index}")
        count_index += index
    index += 1
print(f"count_index is {count_index}")

#divider packets
packets.append([[2]])
packets.append([[6]])

#uses the callable above to sort the packets
packets = sorted(packets, key=functools.cmp_to_key(lambda p1,p2: compare_inputs(p1,p2)))

print(f"Decoder key is {(packets.index([[2]])+1) * (packets.index([[6]])+1)}")