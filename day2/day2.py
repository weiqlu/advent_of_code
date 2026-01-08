from pathlib import Path

def main() -> int: 
    invalid_sum = 0
    
    test_input = Path(__file__).parent / "day2.txt"
    with open(test_input, "r") as file: 
        content = file.read()
        sections = content.split(",")

    for section in sections: 
        id_range = section.split("-")
        for i in range(int(id_range[0]), int(id_range[1])+1):
            id_str = str(i)
            if len(id_str) % 2 == 1: 
                continue
            
            middle = len(id_str) // 2
            if id[0:middle] == id[middle:]:
                invalid_sum += i
    return invalid_sum

if __name__ == "__main__":
    print(main())