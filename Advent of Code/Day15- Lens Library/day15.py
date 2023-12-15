EXAMPLE = "Day 15- Lens Library\example.txt"

INPUT = "Day 15- Lens Library\input.txt"

def calculate_hash_value(hash : str) -> int:
    total = 0
    for i in hash:
        unicode = ord(i)
        total += unicode
        total *= 17
        total = total % 256
    return total

def parse_part(part : str) -> str:
    hash,operand,focal = "","",""
    for i in range(0,len(part)):
        char = part[i]
        if char == "-":
            operand = char
            break
        elif char == "=":
            operand = char
            focal = part[i+1]
            break
        hash += char
    return hash,operand,focal

def update_if_exist(boxes : list , hash : str, focal : str) -> bool:
    for box in boxes:
        if box[0] == hash:
            index = boxes.index(box)
            boxes[index] = [hash,focal]
            return True
    return False

def hash_algorithm_part_one(filename : str) -> int:
    total_hash = 0
    
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        parts = []
        for line in lines:
            part_of_line = line.split(",")
            parts.extend(part_of_line)
        for part in parts:
            total_hash += calculate_hash_value(part)
    return total_hash

def boxing(filename : str) -> dict: # boxing means {box_value : [[hash,focal],[hash,focal] ...]}
    all_boxes = {}
    with open(filename, "r", encoding="utf-8") as file:
        parts = []
        for line in file.readlines():
            parts.append(line.split(","))
        parts = parts[0]

        for part in parts:
            hash,operand,focal = parse_part(part)
            box_key = calculate_hash_value(hash)

            current_boxes = all_boxes[box_key] if box_key in all_boxes.keys() else []
            
            # Operation part that decide what to do
            # If operand is appended or updated
            if operand == "=":
                # if exists, update
                if update_if_exist(current_boxes,hash,focal):
                    pass
                # if not exist, append
                else:
                    current_boxes.append([hash,focal])
                all_boxes[box_key] = current_boxes
            # If operand is deleted
            elif operand == "-":
                # if exist, delete
                for box in current_boxes:
                    if box[0] == hash:
                        current_boxes.remove(box)
                        all_boxes[box_key] = current_boxes
                        break
    return all_boxes

def calculate_focusing_power(all_boxes : dict) -> int:
    total = 0
    for key in all_boxes.keys():
        boxes = all_boxes[key]
        if boxes == []:
            continue
        for slot in range(0,len(boxes)):
            hash_value = calculate_hash_value(boxes[slot][0])
            total += (hash_value+1) * (slot + 1) * int(boxes[slot][1])
    return total

def focusing_power_part_two(filename : str) -> int:
    get_all_boxes = boxing(filename)
    return calculate_focusing_power(get_all_boxes)

def main() -> None:
    test_one = False
    test_two = False

    example_total_hash = hash_algorithm_part_one(EXAMPLE)
    if example_total_hash == 1320:
        print("PASSED TEST: EXAMPLE 1")
        test_one = True

    example_focusing_power = focusing_power_part_two(EXAMPLE)
    if example_focusing_power == 145:
        print("PASSED TEST: EXAMPLE 2")
        test_two = True

    if test_one:
        input_total_hash = hash_algorithm_part_one(INPUT)
        print("Total hash for Part One: ",input_total_hash)

    if test_two:
        input_focusing_power = focusing_power_part_two(INPUT)
        print("Total focusing power for Part Two: ",input_focusing_power)

if __name__ == "__main__":
    main()
