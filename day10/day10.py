with open("input.txt") as f:
    signals = f.read().splitlines()

X = 1
signal_strength = [0]
signal_strength_sum=0

for signal in signals:
    if signal == "noop":
        signal_strength.append(X)
    elif signal.split()[0] == "addx": # Can do with a simple else also
        signal_strength.append(X)
        signal_strength.append(X)
        X += int(signal.split()[1])


for cycle, X in list(enumerate(signal_strength))[20::40]:
    signal_strength_sum+=cycle*X

print(f"Part1: {signal_strength_sum}")
print(f"Part1: {sum(cycle*X for cycle, X in list(enumerate(signal_strength))[20::40])}")


for i in range(1, len(signal_strength), 40):
    for j in range(40):
        print("#" if abs(signal_strength[i + j] - j) <= 1 else " ", end="")
    print()
