EXAMPLE = "./example.txt"

INPUT = "./input.txt"

expanded_x = [] # the cols that contain no galaxies
expanded_y = [] # the rows that contain no galaxies

# scanning all galaxies from the txt file and adding the empty space the expanded lists.
def get_galaxies(filename: str):
    galaxies = []
    expanded_x.clear()
    expanded_y.clear()
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        y_cood = 0
        for i in range(0,len(lines[0])):
            expanded_x.append(i)

        for line in lines:
            x_cood = 0
            isEmptyLine = True
            for c in line:
                if(c == "#"):
                    galaxies.append([x_cood,y_cood])
                    if(x_cood in expanded_x):
                        expanded_x.remove(x_cood)
                    isEmptyLine = False
                x_cood += 1
            if(isEmptyLine):
                expanded_y.append(y_cood)
            y_cood += 1
    return galaxies

# calculation of the distance between two galaxies
def calculate_distance(first : int, second : int, empty_line_size : int, expanded : list) -> int:
    if(first > second):
        first = first + second
        second = first - second
        first = first - second
    
    total_distance = 0
    for i in range(first,second):
        if(i in expanded):
            total_distance += empty_line_size
        else:
            total_distance += 1
    return total_distance

# calculation of the sum of the distance between all galaxies.
def total_distance(filename : str, nongalaxy_line_size : int) -> int:
    totalDistance = 0
    galaxies = get_galaxies(filename)
    
    for i in range(0,len(galaxies)):
        current_x,current_y = galaxies[i]
        for j in range(i,len(galaxies)):
            x,y = galaxies[j]
            totalDistance += calculate_distance(x,current_x,nongalaxy_line_size,expanded_x)
            totalDistance += calculate_distance(y,current_y,nongalaxy_line_size,expanded_y)
    return totalDistance

def main():
    test_one = False
    test_two = False

    example_total_distance = total_distance(EXAMPLE,2)
    if example_total_distance == 374:
        print("PASSED TEST: EXAMPLE 1")
        test_one = True

    example_total_distance = total_distance(EXAMPLE,10)
    if example_total_distance == 1030:
        print("Passed TEST: EXAMPLE 2")
        test_two = True

    if test_one:
        input_total_distance = total_distance(INPUT,2)
        print(f"Total distance for Part One: {input_total_distance}")
    if(test_two):
        input_total_distance = total_distance(INPUT, 1000000)
        print(f"Total distance for Part Two: {input_total_distance}")
    return

if __name__ == "__main__":
    main()