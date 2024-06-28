EXAMPLE = "Day18- Lavaduct Lagoon\example.txt"
INPUT = "Day18- Lavaduct Lagoon\input.txt"

def get_dig_plan(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.split() for line in file]

def start_plan(plans : list):
    x, y = 0, 0
    record = []
    moves = {'R': (1, 0),'D': (0, 1),'L': (-1, 0),'U': (0, -1)}
    for direction, number, code in plans:
        dx, dy = moves[direction]
        for _ in range(int(number)):
            record.append((y, x))
            x += dx
            y += dy
    return record

def calculate_area(records) -> int:
    total = 0
    for i in range(len(records)-1):
        y1, x1 = records[i]
        y2, x2 = records[i+1]
        total += x1*y2 - x2*y1
    return abs(total) // 2

def calculate_cubic_meters_part_one(filename: str) -> int:
    plan = get_dig_plan(filename)
    records = start_plan(plan)
    perimeter = len(records)
    area = calculate_area(records)
    return area + perimeter // 2 + 1

def start_plan_part_two(plans : list):
    x, y = 0, 0
    record = []
    moves = {'0': (1, 0),'1': (0, 1),'2': (-1, 0),'3': (0, -1)}
    for direction, number, code in plans:
        code = code.strip('(#)')
        number = int(code[:5],16)
        dx, dy = moves[code[5]]
        for _ in range(number):
            record.append((y, x))
            x += dx
            y += dy
    return record

def calculate_cubic_meters_part_two(filename: str) -> int:
    plan = get_dig_plan(filename)
    records = start_plan_part_two(plan)
    perimeter = len(records)
    area = calculate_area(records)
    return area + perimeter // 2 + 1

def main() -> None:
    test_one = False
    test_two = False
    
    example_cubic_meters = calculate_cubic_meters_part_one(EXAMPLE)
    if example_cubic_meters == 62:
        print(f"PASSED TEST: EXAMPLE 1({example_cubic_meters})")
        test_one = True

    if test_one:
        input_cubic_meters = calculate_cubic_meters_part_one(INPUT)
        print(f"Cubic meters part one: {input_cubic_meters}")
    
    example_cubic_meters2 = calculate_cubic_meters_part_two(EXAMPLE)
    if example_cubic_meters2 == 952408144115:
        print(f"PASSED TEST: EXAMPLE 2({example_cubic_meters2})")
        test_two = True

    if test_two:
        input_cubic_meters2 = calculate_cubic_meters_part_two(INPUT)
        print(f"Cubic meters part two: {input_cubic_meters2}")

if __name__ == "__main__":
    main()