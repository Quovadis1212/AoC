import re

def get_gear_ratio(digit_positions, symbol_positions, lines):
    print("Digit positions:", digit_positions)
    print("Symbol positions:", symbol_positions)
    print("Lines:", lines)
    print(enumerate(lines))
    gear_ratios = []
    gear_positions = {}
    for i, line in enumerate(lines):
            matches = [(m.start(), m.group()) for m in re.finditer('[*]', line)]
            if matches:
                gear_positions[i] = matches
    print("Gear positions:", gear_positions)

    for gear_symbol, gear_position in gear_positions.items():
        
        print(f"line: {gear_symbol}")
        print(f"Gear Symbol: {gear_position}")

        for gear_item_pos in gear_position:
            gear_matches = []
            print(f"Gear Item Pos: {gear_item_pos}")
            #check current line for matching digits
            try:
                digit_pos = digit_positions.get(gear_symbol)
                for digit_item in digit_pos:
                    if gear_item_pos[0] in range (digit_item[0] - 1, digit_item[0] + len(str(digit_item[1])) + 1):
                        print("Gear part Found:", digit_item[1])
                        gear_matches.append(digit_item[1])
            except:
                print(f"No Match for digit in line:", gear_symbol)
            #check previous line for matching digits
            try:
                digit_pos = digit_positions.get(gear_symbol - 1)
                for digit_item in digit_pos:
                    if gear_item_pos[0] in range (digit_item[0] - 1, digit_item[0] + len(str(digit_item[1])) + 1):
                        print("Gear part Found:", digit_item[1])
                        gear_matches.append(digit_item[1])
            except:
                print(f"No Match for prvious of line:", gear_symbol)
            #check next line for matching digits
            try:
                digit_pos = digit_positions.get(gear_symbol + 1)
                for digit_item in digit_pos:
                    if gear_item_pos[0] in range (digit_item[0] - 1, digit_item[0] + len(str(digit_item[1])) + 1):
                        print("Gear part Found:", digit_item[1])
                        gear_matches.append(digit_item[1])
            except:
                print(f"No Match for next of line:", gear_symbol)
            #if gear matches are bigger than 1, we calculate the gear ratio
            if len(gear_matches) > 1:
                gear_ratio = int(gear_matches[0]) * int(gear_matches[1])
                print("Gear Matches:", gear_matches)
                print("Item Gear Ratio:", gear_ratio)
                gear_ratios.append(gear_ratio)
            else:
                print("Not enough gear parts found")
    
    print("Gear Ratios:", gear_ratios)
    return sum(gear_ratios)


       

def get_valid_parts(digit_positions, symbol_positions, lines):
    print("Digit positions:", digit_positions)
    print("Symbol positions:", symbol_positions)
    print("Lines:", lines)
    print(enumerate(lines))
    
    valid_parts = []

    for line_number, line_content in enumerate(lines):
        print(f"Line {line_number}: {line_content}")

        try:
            digit_pos = digit_positions.get(line_number)
            print("Digit Pos:", digit_pos)
        except:
            print(f"No Match for digit in line:", line_number)
            continue

        # check current line   
        try:
            symbol_pos = symbol_positions.get(line_number)
            print("Symbol Pos:", symbol_pos)

            if symbol_pos is not None:
                for digit_item in digit_pos:
                    valid_part_found = False
                    for symbol_item in symbol_pos:
                        if symbol_item[0] in range(digit_item[0] - 1, digit_item[0] + len(str(digit_item[1])) + 1):
                            print("Valid part:", digit_item[1])
                            valid_parts.append(digit_item[1])
                            valid_part_found = True

                    if not valid_part_found:
                        print(f"No valid part found in Line:", line_number)
        except:
            print(f"No Match for symbol in line:", line_number)

        # check previous line
        try:
            symbol_pos_prev = symbol_positions.get(line_number - 1)
            print("Symbol Pos Prev:", symbol_pos_prev)

            if symbol_pos_prev is not None:
                for digit_item in digit_pos:
                    for symbol_item in symbol_pos_prev:
                        if symbol_item[0] in range(digit_item[0] - 1, digit_item[0] + len(str(digit_item[1])) + 1):
                            print("Valid part:", digit_item[1])
                            valid_parts.append(digit_item[1])
                else:
                    print(f"No valid part found in Line:", line_number)
        except Exception as e:
            print(f"Error: {e}")
            print(f"No Symbol Match in previous Line of:", line_number)

        # check next line
        try:
            symbol_pos_next = symbol_positions.get(line_number + 1)
            print("Symbol Pos Next:", symbol_pos_next)

            if symbol_pos_next is not None:
                for digit_item in digit_pos:
                    for symbol_item in symbol_pos_next:
                        if symbol_item[0] in range(digit_item[0] - 1, digit_item[0] + len(str(digit_item[1])) + 1):
                            print("Valid part:", digit_item[1])
                            valid_parts.append(digit_item[1])
                else:
                    print(f"No valid part found in Line:", line_number)
        except Exception as e:
            print(f"Error: {e}")
            print(f"No Symbol Match in next Line of:", line_number)
    return valid_parts


def solve():
    with open('input.txt') as f:
        lines = f.readlines()
        digit_positions = {}
        for i, line in enumerate(lines):
            matches = [(m.start(), m.group()) for m in re.finditer('\d+', line)]
            if matches:
                digit_positions[i] = matches
        print(digit_positions)
        
        symbol_positions = {}
        for i, line in enumerate(lines):
            matches = [(m.start(), m.group()) for m in re.finditer('[^.\d\s]', line)]
            if matches:
                symbol_positions[i] = matches
        print(symbol_positions)
        
        valid_parts = get_valid_parts(digit_positions, symbol_positions, lines)
        print("Valid Parts:", valid_parts)
        valid_parts = [int(part) for part in valid_parts]
        print(sum(valid_parts))
        
        gear_ratio = get_gear_ratio(digit_positions, symbol_positions, lines)
        print("Sum of Gear Ratio:", gear_ratio)

solve()
