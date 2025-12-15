from pathlib import Path

def main() -> str: 
    count = 0
    rotation = 50

    test_input = Path(__file__).parent / "day1.txt"
    with open(test_input, "r") as file: 
        for line in file:
            direction = line[0]
            num = int(line[1:])

            if direction == 'L': 
                rotation -= num
            elif direction == 'R': 
                rotation += num

            rotation = rotation % 100
            if rotation == 0:
                count += 1
    
    return count

if __name__ == "__main__": 
    print(main())