EXAMPLE = "./Day6- Wait For It/example.txt"

INPUT = "./Day6- Wait For It/input.txt"


def read_file(filename : str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.split(": ")[1].strip() for line in file.readlines()]

def get_possible_beat_number(distance:int, time:int) -> int:
    return sum((time - i) * i > distance for i in range(time))

def multiply_possibilities_part_one(filename:str) -> int:
    lines = read_file(filename)
    times, distances = lines[0].split(),lines[1].split()
    total = 1
    for i in range(len(times)):
        total *= get_possible_beat_number(int(distances[i]),int(times[i]))
    return total

def multiply_possibilities_part_two(filename:str) -> int:
    lines = read_file(filename)
    time = lines[0].replace(" ","")
    distance = lines[1].replace(" ","")
    return get_possible_beat_number(int(distance), int(time))

def main() -> None:
    test_one = False
    test_two = False

    example_part_one = multiply_possibilities_part_one(EXAMPLE)
    if example_part_one == 288:
        print(f"PASSED TEST: EXAMPLE 1 ({example_part_one})")
        test_one = True

    example_part_two = multiply_possibilities_part_two(EXAMPLE)
    if example_part_two == 71503:
        print(f"PASSED TEST: EXAMPLE 2 ({example_part_two})")
        test_two = True
    
    if test_one:
        input_part_one = multiply_possibilities_part_one(INPUT)
        print(f"Result of multiplications for part one: {input_part_one}")

    if test_two:
        input_part_two = multiply_possibilities_part_two(INPUT)
        print(f"Result of multiplications for part one: {input_part_two}")

if __name__ == "__main__":
    main()