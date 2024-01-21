EXAMPLE = "./Day4- Scratchcards/example.txt"

INPUT = "./Day4- Scratchcards/input.txt"

def read_file(filename : str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.rstrip().split(": ")[1] for line in file.readlines()]

def total_points_part_one(filename : str) -> int:
    lines = read_file(filename)
    total = 0
    for line in lines:
        winnings,cards = line.split("|")
        winnings = winnings.split()
        cards = cards.split()
        point = get_winning_value(cards, winnings)
        if not point == 0:
            total += 2**(point-1)
    return total

def get_winning_value(cards:list, winnings:list) -> int:
    total_win = 0
    for card in cards:
        if card in winnings:
            total_win += 1
    return total_win

def total_scratchcards_part_two(filename : str) -> int:
    lines = read_file(filename)
    total = 0
    scratching = []
    for line in lines:
        winnings,cards = line.split("|")
        winnings = winnings.split()
        cards = cards.split()
        size = len(scratching)
        for i in range(size+1):
            point = get_winning_value(cards,winnings)
            scratching.append(int(point+1))
            total += 1
            
        scratching = [number - 1 for number in scratching]
        scratching = [number for number in scratching if number != 0]
    return total

def main() -> None:
    test_one = False
    test_two = False

    example_total_points = total_points_part_one(EXAMPLE)
    if example_total_points == 13:
        print(f"PASSED TEST: EXAMPLE 1 ({example_total_points})")
        test_one = True

    example_total_scratchcards = total_scratchcards_part_two(EXAMPLE)
    if example_total_scratchcards == 30:
        print(f"PASSED TEST: EXAMPLE 2 ({example_total_scratchcards})")
        test_two = True
    
    if test_one:
        input_total_points = total_points_part_one(INPUT)
        print(f"Total points for part one: {input_total_points}")

    if test_two:
        input_total_scratching = total_scratchcards_part_two(INPUT)
        print(f"Total scratching for part two: {input_total_scratching} ")  


if __name__ == "__main__":
    main()