EXAMPLE = "./Day12- Hot Springs/example.txt"

INPUT = "./Day12- Hot Springs/input.txt"

def increase_string(old_spring : str, indexes : list) -> str:
    spring = old_spring
    indexes_of_hash = []
    for i in indexes:
        if (spring[i] == "."):
            spring = spring[:i] + "#" + spring[i+1:]
            break
        else:
            indexes_of_hash.append(i)
    for i in indexes_of_hash:
        spring = spring[:i] + "." + spring[i+1:]
    return spring

def isSuitable(spring : str, damaged : list) -> bool:
    parts = []
    
    part = ""
    for char in spring:
        if char == "#":
            part += char
        elif char == ".":
            if not part == "":
                parts.append(part)
                part = ""
    if not part == "":
        parts.append(part)
        part = ""

    if not len(parts) == len(damaged):
        return False
    
    for i in range(0,len(parts)):
        if not len(parts[i]) ==  (int)(damaged[i]):
            return False
        
    return True

def isSuitable2(spring : str, damaged : list) -> bool:
    parts = []
    
    before = False
    part = 0
    
    for char in spring:
        if char == "#":
            part += 1
            if not before:
                before = True
        elif char == ".":
            if before:
                parts.append(part)
                before = False
                part = 0
    if before:
        parts.append(part)
        part = 0
        before = False

    if not len(parts) == len(damaged):
        return False
    
    for i in range(0,len(parts)):
        if not parts[i] ==  (int)(damaged[i]):
            return False
        
    return True

def get_possible_arrangement(spring : str, damaged : list) -> int:
    arrangements = 0
    indexes = []
    
    for index in range(0,len(spring)):
        if spring[index] == "?":
            indexes.append(index)
            spring = spring[:index] + "." + spring[index + 1:]

    for _ in range(0,pow(2,len(indexes))):
        if(isSuitable2(spring,damaged)):
            arrangements += 1
        spring = increase_string(spring, indexes)
    indexes.clear()
    return arrangements

def total_arrangement_part_one(filename : str) -> int:
    arrangement_counter = 0
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        i = 1
        for line in lines:
            spring, damaged = line.split(" ")
            damaged = damaged.split(",")
            arrangement_counter += get_possible_arrangement(spring, damaged)
            i+=1
    return arrangement_counter


def total_arrangement_part_two(filename : str) -> int:
    arrangement_counter = 0
    with open(filename, "r", encoding="utf-8") as file:
        lines2 = file.readlines()
        i = 1
        for line in lines2:
            #print(i)
            i += 1
            line = line.rstrip()
            spring, damaged = line.split(" ")
            spring = f"{spring}?{spring}?{spring}?{spring}?{spring}"
            damaged = f"{damaged},{damaged},{damaged},{damaged},{damaged}"
            damaged = damaged.split(",")
            arrangement = get_possible_arrangement(spring, damaged)
            arrangement_counter += arrangement
    
    return arrangement_counter

def main() -> None:
    test_one = False
    test_two = False

    example_total_arrangement = total_arrangement_part_one(EXAMPLE)
    if example_total_arrangement == 21:
        print("PASSED TEST: EXAMPLE 1")
        test_one = True

    example_total_arrangement = total_arrangement_part_two(EXAMPLE)
    print(example_total_arrangement)
    if example_total_arrangement == 525152:
        print("PASSED TEST: EXAMPLE 2")

    if test_one:
        input_total_arrangement = total_arrangement_part_one(INPUT)
        print(f"Total arrangements for Part One: {input_total_arrangement}")

    if test_two:
        input_total_arrangement = total_arrangement_part_two(INPUT)
        print(f"Total arrangements for Part Two: {input_total_arrangement}")


if __name__ == "__main__":
    main()