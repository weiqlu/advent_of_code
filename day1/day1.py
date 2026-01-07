from pathlib import Path

def main() -> int: 
    count = 0
    position = 50

    test_input = Path(__file__).parent / "day1.txt"
    with open(test_input, "r") as file: 
        for line in file:
            direction = line[0]
            distance = int(line[1:])

            prev_distance = position

            if direction == 'L': 
                position -= distance
                count += (prev_distance - 1) // 100 - (position - 1) // 100
            elif direction == 'R': 
                position += distance
                count += (position) // 100 - prev_distance // 100

            position %= 100
    return count

if __name__ == "__main__": 
    print(main())