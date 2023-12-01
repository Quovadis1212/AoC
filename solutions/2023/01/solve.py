import re
def convert_numbers(input_string):
    #Very ugly way to handle the composite Numbers. But hey, it works.
    combined_to_numeric = {
        "oneight": 18,
        "twone": 21,
        "threeight": 38,
        "fiveight": 58,
        "eightwo": 82,
        "eightthree": 83,
        "nineight": 98,        
    }
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
    combined_pattern = re.compile('|'.join(re.escape(key) for key in combined_to_numeric.keys()))
    input_string = combined_pattern.sub(lambda x: str(combined_to_numeric[x.group()]), input_string)
    
    pattern = re.compile('|'.join(re.escape(key) for key in written_to_numeric.keys()))
    converted_string = pattern.sub(lambda x: str(written_to_numeric[x.group()]), input_string)
    return converted_string

with open ('input.txt') as f:
    combinedvalue = 0
    for line in f:
        line = line.strip()
        print(line)
        convertedline = convert_numbers(line)
        #print(convertedline)
        digits = re.findall(r'\d', convertedline)
        firstdigit = int(digits[0]) * 10
        lastdigit = int(digits[-1])
        print(firstdigit+lastdigit)
        combinedvalue += firstdigit + lastdigit
    #print(combinedvalue)



        



