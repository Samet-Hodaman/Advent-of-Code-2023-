EXAMPLE = "./Day9- Mirage Maintenance/example.txt"

INPUT = "./Day9- Mirage Maintenance/input.txt"

def read_file(filename: str) -> list[list[int]]:
    with open(filename, "r", encoding="utf-8") as file:
        return [list(map(int, line.split())) for line in file.readlines()]

def expand_graph(val:list) -> list:
    graph = [val]
    while not all(x==0 for x in graph[-1]):
        graph.append([graph[-1][i+1] - graph[-1][i] for i in range(len(graph[-1])-1)])
    return graph

def analyze_OASIS_report_part_one(filename:str) -> int:
    lines = read_file(filename)
    total = 0
    for line in lines:
        graph = expand_graph(line)
        total += sum(each[-1] for each in graph)
    return total

def analyze_OASIS_report_part_two(filename:str) -> int:
    lines = read_file(filename)
    total = 0
    for line in lines:
        graph = expand_graph(line)
        even = sum(graph[i][0] for i in range(0,len(graph),2))
        odd = sum(graph[i][0] for i in range(1,len(graph),2))
        total += even-odd
    return total



def main() -> None:
    test_one = False
    test_two = False

    example_oasis_report = analyze_OASIS_report_part_one(EXAMPLE)
    if example_oasis_report == 114:
        print(f"PASSED TEST: EXAMPLE 1 ({example_oasis_report})")
        test_one = True

    example_reverse_oasis_report = analyze_OASIS_report_part_two(EXAMPLE)
    if example_reverse_oasis_report == 2:
        print(f"PASSED EXAM: EXAMPLE 2 ({example_reverse_oasis_report})")
        test_two = True

    if test_one:
        input_oasis_report = analyze_OASIS_report_part_one(INPUT)
        print(f"Oasis report for part one: {input_oasis_report}")

    if test_two:
        input_reverse_oasis_report = analyze_OASIS_report_part_two(INPUT)
        print(f"Reverse oasis report for part two: {input_reverse_oasis_report}")

if __name__ == "__main__":
    main()