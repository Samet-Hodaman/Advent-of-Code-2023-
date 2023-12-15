INPUT = "./Day14- Parabolic Reflector Dish/input.txt"

EXAMPLE = "./Day14- Parabolic Reflector Dish/example.txt"

def read_the_map(filename : str) -> list:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        rows = []
        for line in lines:
            line = line.rstrip()
            row = []
            for i in range(0,len(line)):
                row.append(line[i])
            rows.append(row)
    return rows

# Rolling all rocks which can be rolled in the map to the north direction
def roll_to_north(roks_map : list) -> list:
    for col in range(0,len(roks_map)): # rows
        for row in range(1,len(roks_map[0])): # cols    roks_map[row][col]
            if roks_map[row][col] == "O":
                roks_map[row][col] = "."
                current_row = row

                before = roks_map[current_row - 1][col]
                while(not (before == "O" or before == "#") and current_row > 0):
                    current_row -= 1
                    before = roks_map[current_row - 1][col]

                roks_map[current_row][col] = "O"
    return roks_map

# Rolling all rocks which can be rolled in the map to the west direction
def roll_to_west(roks_map : list) -> list:
    for col in range(1,len(roks_map)):
        for row in range(0,len(roks_map[0])):
            if roks_map[row][col] == "O":
                roks_map[row][col] = "."
                current_col = col

                before = roks_map[row][current_col -1]
                while not (before == "O" or before == "#") and current_col > 0:
                    current_col -= 1
                    before = roks_map[row][current_col -1]
                
                roks_map[row][current_col] = "O"
    return roks_map

# Rolling the rocks to the south
def roll_to_south(roll_map : list) -> list:
    roll_map.reverse()
    roll_map = roll_to_north(roll_map)
    roll_map.reverse()
    return roll_map

# Rolling the rocks to the east
def roll_to_east(roks_map : list[list]) -> list:
    temp_map = []
    for row in roks_map: # Reversing the rows in the map
        row.reverse()
        temp_map.append(row)
    temp_map = roll_to_west(temp_map)
    
    new_map = []
    for row in temp_map:
        row.reverse()
        new_map.append(row)
    return new_map

# Calculation of the total load on the north support beams.
def calculate_total_load(roks_map : list[list]) -> int:
    total_load = 0
    value_of_line = len(roks_map[0])
    for row in roks_map:
        number_of_rock = 0
        for c in row:
            if c == "O":
                number_of_rock += 1
        total_load += number_of_rock * value_of_line
        value_of_line -= 1
    return total_load

# Part One
def the_total_load_part_one(filename : str) -> int:
    roks_map = read_the_map(filename)
    roks_map = roll_to_north(roks_map)
    return calculate_total_load(roks_map) 

# Part Two
def the_total_load_part_two(filename : str) -> int:
    number_of_spin_cycle = 1000 # instead of 1000000000 cycles
    roks_map = read_the_map(filename) # Getting the roks map from the file
    
    # Spin cycle
    for _ in range(0,number_of_spin_cycle):
        roks_map = roll_to_north(roks_map)
        roks_map = roll_to_west(roks_map)
        roks_map = roll_to_south(roks_map)
        roks_map = roll_to_east(roks_map)
    return calculate_total_load(roks_map)

def main() -> None:
    test_one = False
    test_two = False

    example_total_load = the_total_load_part_one(EXAMPLE)
    if example_total_load == 136:
        print("PASSED TEST: EXAMPLE 1")
        test_one = True

    example_total_load = the_total_load_part_two(EXAMPLE)
    if example_total_load == 64:
        print("PASSED TEST: EXAMPLE 2")
        test_two = True

    if test_one:
        input_total_load = the_total_load_part_one(INPUT)
        print(f"Total load of rock for Part One: {input_total_load}")

    if test_two:
        input_total_load = the_total_load_part_two(INPUT)
        print(f"Total load of rock for Part Two: {input_total_load}")

if __name__ == "__main__":
    main()