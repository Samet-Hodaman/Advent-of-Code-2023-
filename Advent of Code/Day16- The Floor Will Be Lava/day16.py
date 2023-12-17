import sys
sys.setrecursionlimit(10**6)

EXAMPLE = "./Day16- The Floor Will Be Lava\example.txt"
INPUT = "./Day16- The Floor Will Be Lava\input.txt"

record = {} # {[x_coord,y_coord] : ["left","right","up","down"]}
area = [] # map of the area

def get_map(filename : str) -> list[list]:
    rows = []
    with open(filename, "r", encoding="utf-8") as file:
        rows = [list(line.rstrip()) for line in file.readlines()]
    return rows

def go_left(x_coord : int,y_coord : int) -> None: 

    if x_coord >= 0:
        symbol = area[y_coord][x_coord]
        if symbol == '.' or symbol == '-':
            if record_the_path([x_coord , y_coord], "left"):
                return go_left(x_coord - 1,y_coord)
        
        elif symbol == '\\':
            if record_the_path([x_coord , y_coord], "up"):
                return go_up(x_coord , y_coord - 1)

        elif symbol == '/':
            if record_the_path([x_coord , y_coord], "down"):
                return go_down(x_coord , y_coord + 1)

        elif symbol == '|':
            record_the_path([x_coord , y_coord], "up")
            record_the_path([x_coord , y_coord], "down")
            return go_up(x_coord , y_coord - 1) , go_down(x_coord , y_coord + 1)
        
        else:
            print("Undefined Symbol: ",symbol)

def go_right(x_coord : int,y_coord : int) -> None:

    if x_coord <len(area[0]):
        symbol = area[y_coord][x_coord]
        if symbol == '.' or symbol == '-':
            if record_the_path([x_coord , y_coord],"right"):
                return go_right(x_coord + 1,y_coord)
            
        elif symbol == '\\':
            if record_the_path([x_coord , y_coord], "down"):
                return go_down(x_coord,y_coord + 1)

        elif symbol == '/':
            if record_the_path([x_coord , y_coord], "up"):
                return go_up(x_coord,y_coord - 1)

        elif symbol == '|':
            record_the_path([x_coord , y_coord] , "up")
            record_the_path([x_coord , y_coord] , "down")
            return go_up(x_coord , y_coord - 1) , go_down(x_coord , y_coord + 1)
        
        else:
            print("Undefined Symbol: ",symbol)

def go_up(x_coord : int,y_coord : int) -> None:
    
    if y_coord >= 0:
        symbol = area[y_coord][x_coord]
        if symbol == '.' or symbol == '|':
            if record_the_path([x_coord , y_coord], "up"):
                return go_up(x_coord , y_coord - 1)
            
        elif symbol == '\\':
            if record_the_path([x_coord , y_coord], "left"):
                return go_left(x_coord - 1,y_coord)

        elif symbol == '/':
            if record_the_path([x_coord , y_coord], "right"):
                return go_right(x_coord + 1 , y_coord)

        elif symbol == '-':
            record_the_path([x_coord , y_coord] , "left")
            record_the_path([x_coord , y_coord] , "right")
            return go_left(x_coord - 1 , y_coord) , go_right(x_coord + 1 , y_coord)
        
        else:
            print("Undefined Sybbol: ",symbol)

def go_down(x_coord : int,y_coord : int) -> None:

    if y_coord < len(area):
        symbol = area[y_coord][x_coord]
        if symbol == '.' or symbol == '|':
            if record_the_path([x_coord , y_coord] , "down"):
                return go_down(x_coord , y_coord + 1)

        elif symbol == '\\':
            if record_the_path([x_coord , y_coord] , "right"):
                return go_right(x_coord + 1 , y_coord)

        elif symbol == '/':
            if record_the_path([x_coord , y_coord] , "left"):
                return go_left(x_coord - 1 , y_coord)

        elif symbol == '-':
            record_the_path([x_coord , y_coord] , "left")
            record_the_path([x_coord , y_coord] , "right")
            return go_left(x_coord - 1 , y_coord) , go_right(x_coord + 1 , y_coord)
        
        else:
            print("Undefined Symbol: ",symbol)

def record_the_path(coord : list, operand : str) -> bool: # check if exists
    keys = record.keys()
    if keys:
        if tuple(coord) in record:
            directions = record[tuple(coord)]
            if operand in directions:
                return False # 
            else:
                directions.append(operand)
                return True # Been here before but passed from a different direction.
    record[tuple(coord)] = [operand]
    return True
    
def total_tiles_energized_part_one(filename : str) -> int:
    global area 
    area = get_map(filename)
    go_right(0,0)

    total_tiles = len(record)
    record.clear()
    return total_tiles

def calculate_total_tiles() -> int:
    total_tiles = len(record)
    record.clear()
    return total_tiles

def max_tiles_energized_part_two(filename : str) -> int:
    global area
    area = get_map(filename)
    max_tiles = 0
    right_end = len(area[0])
    bottom_end = len(area)

    for col_index in range(0 , right_end):
        go_down(col_index, 0)
        total = calculate_total_tiles()
        if total > max_tiles:
            max_tiles = total
        go_up(col_index, bottom_end - 1)
        total = calculate_total_tiles()
        if total > max_tiles:
            max_tiles = total

    for row_index in range(0 , bottom_end):
        go_right(0, row_index)
        total = calculate_total_tiles()
        if total > max_tiles:
            max_tiles = total
        
        go_left(right_end - 1, row_index)
        total = calculate_total_tiles()
        if total > max_tiles:
            max_tiles = total
    return max_tiles

def main() -> None:
    test_one = False
    test_two = False

    example_energized_tiles = total_tiles_energized_part_one(EXAMPLE)
    print(example_energized_tiles)
    if example_energized_tiles == 46:
        print("PASSED TEST: EXAMPLE 1")
        test_one = True

    example_max_energized_tiles = max_tiles_energized_part_two(EXAMPLE)
    if example_max_energized_tiles == 51:
        print("PASSED TEST: EXAMPLE 2")
        test_two = True

    if test_one:
        input_total_energized = total_tiles_energized_part_one(INPUT)
        print(f"Total energized tiles for Part One: {input_total_energized}")
    
    if test_two:
        input_max_energized_tiles = max_tiles_energized_part_two(INPUT)
        print(f"Maximum energized tiles for Part Two: {input_max_energized_tiles}")
 

if __name__ == "__main__":
    main()