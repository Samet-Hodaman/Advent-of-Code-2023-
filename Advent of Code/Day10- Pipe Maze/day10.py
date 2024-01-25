EXAMPLE = "./Day10- Pipe Maze/example.txt"
EXAMPLE2 = "./Day10- Pipe Maze/example2.txt"

INPUT = "./Day10- Pipe Maze/input.txt"

def read_file(filename: str) -> list[list[int]]:
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]
    
def cames_from_right(shape:str,x:int,y:int):
    if shape == "-":
        return [x-1,y,"r"]
    elif shape == "L":
        return [x,y-1,"d"]
    elif shape == "F":
        return [x,y+1,"u"]

def cames_from_left(shape:str,x:int,y:int):
    if shape == "J":
        return [x,y-1,"d"] 
    elif shape == "7":
        return [x,y+1,"u"]
    elif shape == "-":
        return [x+1,y,"l"]
    
def cames_from_up(shape:str,x:int,y:int):
    if shape == "|":
        return [x,y+1,"u"]
    elif shape == "L":
        return [x+1,y,"l"]
    elif shape == "J":
        return [x-1,y,"r"]
    
def cames_from_down(shape:str,x:int,y:int):
    if shape == "|":
        return [x,y-1,"d"]
    elif shape == "7":
        return [x-1,y,"r"]
    elif shape == "F":
        return [x+1,y,"l"]
    
def go_next(prev:list[int,int,str], maze_map) -> list:
    shape = maze_map[prev[1]][prev[0]]
    x, y = prev[0:2]
    if prev[2] == "r":
        return cames_from_right(shape,x,y)
    elif prev[2] == "l":
        return cames_from_left(shape,x,y)
    elif prev[2] == "u":
        return cames_from_up(shape,x,y)
    elif prev[2] == "d":
        return cames_from_down(shape,x,y)
          
def farthest_position_part_one(filename:str) -> int:
    maze_map = read_file(filename)
    start_y,start_x = [(i, row.index("S")) for i, row in enumerate(maze_map) if "S" in row][0]

    around = [[-1,0,"r","LF-"],[1,0,"l","J7-"],[0,-1,"d","7F|"],[0,1,"u","JL|"]]

    tail = []
    for a in around:
        shape = maze_map[start_y+a[1]][start_x+a[0]]
        if shape in a[3] and all(int(x)>=0 for x in [start_x+a[0],start_y+a[1]]):
            tail.append([start_x+a[0],start_y+a[1],a[2]])

    count = 1
    while tail:
        current = [tail.pop() for _ in range(len(tail))]
        for node in current:
            next_one = go_next(node,maze_map)
            tail.insert(0,next_one)
        count +=1
        if tail[0][0:2] == tail[1][0:2]:
            return count

def change_if_open(place:str,x:int,y:int):
    shape = place[y][x]
    x_size = len(place[0])-1
    y_size = len(place)-1

    if shape == ".":
        if (x == x_size or y == y_size) or (x == 0 or y == 0):
            place[y] = place[y][0:x]+"O"+place[y][x+1:]
        else:
            around = [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]
            if any(place[a[1]][a[0]] == "O" for a in around):
                place[y] = place[y][0:x]+"O"+place[y][x+1:]
            else:
                place[y] = place[y][0:x]+"I"+place[y][x+1:]
                return 1
    return 0
    
def enclosed_tiles_part_two(filename:str) -> int:
    maze_map = read_file(filename)

    v_size = len(maze_map)-1
    h_size = len(maze_map[0])-1
    
    total_enclosed = 0
    for i in range(int(h_size/2)): # i=diagonal j=index
        for j in range(i,h_size-i+1):
            total_enclosed += change_if_open(maze_map,j,i) #0->, 0 right
            total_enclosed += change_if_open(maze_map,h_size-j,v_size-i) #e, e left
        
        for j in range(i,v_size-i+1):    
            total_enclosed += change_if_open(maze_map,h_size-i,j) #e, 0 down
            total_enclosed += change_if_open(maze_map,i,v_size-j) #0, e up
        
    return total_enclosed

def main()->None:
    test_one = False
    test_two = False
    
    example_fartest_length = farthest_position_part_one(EXAMPLE)
    if example_fartest_length == 8:
        print(f"PASSED TEST: EXAMPLE 1 ({example_fartest_length})")
        test_one = True

    example_enclosed_tiles = enclosed_tiles_part_two(EXAMPLE2)
    if example_enclosed_tiles == 9:
        print(f"PASSED TEST: EXAMPLE 2 ({example_enclosed_tiles})")
        test_two = True
    
    if test_one:
        input_fartest_length = farthest_position_part_one(INPUT)
        print(f"Length of the farthest position part one: {input_fartest_length}")
    
    if test_two:
        input_enclosed_tiles = enclosed_tiles_part_two(INPUT)
        print(f"Total enclosed tiles part two: {input_enclosed_tiles}")

if __name__ == "__main__":
    main()