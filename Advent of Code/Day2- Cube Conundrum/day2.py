EXAMPLE = "./Day2- Cube Conundrum/example.txt"

INPUT = "./Day2- Cube Conundrum/input.txt"

def read_file(filename : str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.rstrip().split(": ")[1] for line in file.readlines()]

def is_possible(game_sets : list[str]) -> bool:
    possibility = {"red":12, "green":13, "blue":14}
    for each_set in game_sets:
        each_set = each_set.strip().split(", ")
        for e in each_set:
            e = e.split(" ")
            color = e[1]
            num = int(e[0])
            if possibility[color] < num:
                return False
    return True
        
def get_minimum_requirement(game_sets : list[str]) -> int:
    colors = {"red":0, "green":0, "blue":0}
    for each_set in game_sets:
        each_set = each_set.strip().split(", ")
        for e in each_set:
            e = e.split(" ")
            color = e[1]
            amount = int(e[0])
            if colors[color] < amount:
                colors[color] = amount
    return colors["blue"] * colors["red"] * colors["green"]

def total_power_sets_part_two(filename : str) -> int:
    lines = read_file(filename)
    total = 0
    for line in lines:
        sets = line.split(";")
        total += get_minimum_requirement(sets)
    return total

def total_possible_games_part_one(filename : str) -> int:
    lines = read_file(filename)
    total = 0
    for i in range(0,len(lines)):
        sets_of_game = lines[i].split(";")
        if (is_possible(sets_of_game)):
            total += i+1
    return total

def main() -> None:
    test_one = False
    test_two = False

    example_total_possible_games = total_possible_games_part_one(EXAMPLE)
    if example_total_possible_games == 8:
        print(f"PASSED TEST: EXAMPLE 1 ({example_total_possible_games})")
        test_one = True
    
    example_total_power = total_power_sets_part_two(EXAMPLE)
    if example_total_power == 2286:
        print(f"PASSED TEST: EXAMPLE 2 ({example_total_power})")
        test_two = True

    if test_one:
        input_total_possible_games = total_possible_games_part_one(INPUT)
        print(f"Total possible games for part one : {input_total_possible_games}") 

    if test_two:
        input_total_power = total_power_sets_part_two(INPUT)
        print(f"total power of sets part two : {input_total_power}")

if __name__ == "__main__":
    main()