import re
def get_numbers(string):
    written_to_numeric = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
    values = re.findall(r"(?=(\d{1}|one|two|three|four|five|six|seven|eight|nine))", string)
    values = list(map(lambda x: written_to_numeric[x] if x in written_to_numeric else int(x), values))
    return(values)

def get_calibration_value(values):
    firstdigit = values[0] * 10
    lastdigit = values[-1]
    return(firstdigit+lastdigit)

def combine_calibrations_list(list_of_calibrations):
    return(sum(list_of_calibrations))

with open ('input.txt') as f:
    string = f.read()
    inputlist = string.split("\n")
    calibration_values = []
    for element in inputlist:
        print(element)
        numbers = get_numbers(element)
        print(numbers)
        calibration_value = get_calibration_value(numbers)
        print(calibration_value)
        calibration_values.append(calibration_value)
    print("The Solution is:",combine_calibrations_list(calibration_values))