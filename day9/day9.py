with open("input.txt") as f:
    steps = f.read().splitlines()


def positioning(n):
    return -1 if n < 0 else (1 if n > 0 else 0)


def update_position(H, T):
    x, y = H[0] - T[0], H[1] - T[1]
    if abs(x) <= 1 and abs(y) <= 1:  # No need to change Tail's position in this case
        pass
    elif (
        abs(x) >= 2 and abs(y) >= 2
    ):  # move x,y co-ordinates according to the head's position (diagonal)
        T = (H[0] + positioning(T[0] - H[0]),
            H[1] + positioning(T[1] - H[1]))
    elif abs(x) >= 2:
        T = (H[0] + positioning(T[0] - H[0]), H[1])
    elif abs(y) >= 2:
        T = (H[0], H[1] + positioning(T[1] - H[1]))

    return T


H = (0, 0)
T = [(0, 0) for _ in range(9)]
D = {"R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)}

part_1, part_2 = set(), set()

for step in steps:
    dir, dist = step.split()
    for _ in range(int(dist)):
        part_1.add(T[0])
        part_2.add(T[8])
        H = (H[0] + D[dir][0], H[1] + D[dir][1])
        T[0] = update_position(H, T[0])
        for i in range(1, 9):
            T[i] = update_position(
                T[i - 1], T[i]
            )  # part2 has 8 tails which follow the previous one
        part_1.add(T[0])
        part_2.add(T[8])

print(len(part_1), len(part_2))
