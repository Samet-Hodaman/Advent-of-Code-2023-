EXAMPLE = "./Day1- Trebuchet/example.txt"
EXAMPLE2 = "./Day1- Trebuchet/example2.txt"

INPUT = "./Day1- Trebuchet/input.txt"

def read_file(filename : str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as file:
        return [list(line.rstrip()) for line in file.readlines()]

def calibration_values_part_one(filename : str) -> int:
    lines = read_file(filename)
    total_calibration_values = 0
    for line in lines:
        calibration_value = 0
        firstDigit = ""
        lastDigit = str
        
        for c in line:
            if c.isdigit():
                if firstDigit == "":
                    firstDigit = c
                lastDigit = c
        calibration_value = int(firstDigit + lastDigit)
        total_calibration_values += calibration_value

    return total_calibration_values

def calibration_values_part_two(filename : str) -> int:
    lines = read_file(filename)
    total_calibration_values = 0
    digit_dict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for line in lines:
        prev_chars = ""
        first_digit = ""
        last_digit = str

        for c in line:
            # If the char is a digit
            if c.isdigit():
                last_digit = c
                if first_digit == "":
                    first_digit = c
                prev_chars = ""
            # If the char is not a digit
            else:
                prev_chars += c
                for key in digit_dict.keys():
                    if key in prev_chars:
                        last_digit = digit_dict.get(key)
                        if first_digit == "":
                            first_digit = digit_dict.get(key)
                        prev_chars = c
                        break
        calibration_value = int(first_digit + last_digit)
        print(calibration_value)
        total_calibration_values += calibration_value

    return total_calibration_values

def main():
    test_one = False
    test_two = False
    
    example_calibration_value = calibration_values_part_one(EXAMPLE)
    if example_calibration_value == 142:
        print(f"PASSED TEST: EXAMPLE 1 ({example_calibration_value})")
        test_one = True

    example_calibration_value2 = calibration_values_part_two(EXAMPLE2)
    if example_calibration_value2 == 281:
        print(f"PASSED TEST: EXAMPLE 2 ({example_calibration_value2})")
        test_two = True

    if test_one:
        input_calibration_value = calibration_values_part_one(INPUT)
        print(f"Total calibration value for part one: {input_calibration_value}")

    if test_two:
        input_calibration_value2 = calibration_values_part_two(INPUT)
        print(f"Total calibration value for part two: {input_calibration_value2}")


if __name__ == "__main__":
    main()