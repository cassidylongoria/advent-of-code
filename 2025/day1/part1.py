from pathlib import Path

# path to this script's folder
here = Path(__file__).parent
input_file = here / "input.txt"

position = 50
zero_count = 0

with open(input_file) as file:
    for line in file:
        line = line.strip()

        direction = line[0]
        distance = int(line[1:])

        step = 1 if direction == "R" else -1

        for _ in range(distance):
            position = (position + step) % 100
            if position == 0:
                zero_count += 1

print(zero_count)