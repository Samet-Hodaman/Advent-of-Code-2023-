from heapq import heappush, heappop

EXAMPLE = "./Day17- Clumsy Crucible/example.txt"
INPUT = "./Day17- Clumsy Crucible/input.txt"

def get_map(filename: str) -> list[list[int]]:
    return [list(map(int, line.strip())) for line in open(filename, "r", encoding="utf-8")]


def minimum_heat_loss_part_one(filename : str) -> int:
    area = get_map(filename)
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c,dr, dc, n = heappop(pq)

        if r == len(area) -1 and c == len(area[0]) -1:
            return hl

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))

        # Continue in the same direction
        if n < 3 and (dr,dc) != (0,0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(area) and 0 <= nc < len(area[0]):
                heappush(pq, ((hl + area[nr][nc]), nr, nc, dr, dc, n+1))

        # Check every possible turning
        for (ndr, ndc) in [(0, 1),(1, 0),(0, -1),(-1, 0)]:
            if (ndr, ndc) != (dr,dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(area) and 0 <= nc < len(area[0]):
                    heappush(pq, ((hl + area[nr][nc]), nr, nc, ndr, ndc, 1))

def minimum_heat_loss_part_two(filename: str):
    area = get_map(filename)
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c,dr, dc, n = heappop(pq)

        if r == len(area) -1 and c == len(area[0]) -1:
            return hl

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))

        # Continue in the same direction
        if n < 10 and (dr,dc) != (0,0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(area) and 0 <= nc < len(area[0]):
                heappush(pq, ((hl + area[nr][nc]), nr, nc, dr, dc, n+1))

        # Check every possible turning
        if n >= 4 or (dr, dc) == (0, 0):
            for (ndr, ndc) in [(0, 1),(1, 0),(0, -1),(-1, 0)]:
                if (ndr, ndc) != (dr,dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(area) and 0 <= nc < len(area[0]):
                        heappush(pq, ((hl + area[nr][nc]), nr, nc, ndr, ndc, 1))


def main() -> None:
    test_one = False
    test_two = False
    
    example_heat_loss = minimum_heat_loss_part_one(EXAMPLE)
    if example_heat_loss == 102:
        print(f"PASSED TEST: EXAMPLE 1 ({example_heat_loss})")
        test_one = True
    
    if test_one:
        input_heat_loss = minimum_heat_loss_part_one(INPUT)
        print(f"Minimum heat loss part one: {input_heat_loss}")
    
    example_heat_loss_2 = minimum_heat_loss_part_two(EXAMPLE)
    if example_heat_loss_2 == 94:
        print(f"PASSED TEST: EXAMPLE 2 ({example_heat_loss_2})")
        test_two = True

    if test_two:
        input_heat_loss_2 = minimum_heat_loss_part_two(INPUT)
        print(f"Minimum heat loss part two: {input_heat_loss_2}")

if __name__ == "__main__":
    main()

