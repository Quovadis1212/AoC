import re
def is_valid_game(gamevalues):
    if gamevalues["red"] > 12 or gamevalues["green"] > 13 or gamevalues["blue"] > 14:
        return False
    else:
        return True

def get_cubepower(gamevalues):
    return(gamevalues["red"] * gamevalues["green"] * gamevalues["blue"])
    
with open('input.txt') as f:
    string = f.read()
    inputlist = string.split("\n")
    sumofids = 0
    sumcubepower = 0
    for game in inputlist:
        print(game)
        gamevalues = {}
        gameid = re.findall(r'\d+', str(re.findall(r"Game \d*", game))),
        gamered = re.findall(r'\d+', str(re.findall(r'(\d+) red', game))),
        gameblue = re.findall(r'\d+', str(re.findall(r'(\d+) blue', game))),
        gamegreen = re.findall(r'\d+', str(re.findall(r'(\d+) green', game))),
        gamevalues["red"] = max(map(int, gamered[0]))
        gamevalues["green"] = max(map(int, gamegreen[0]))
        gamevalues["blue"] = max(map(int, gameblue[0]))
        print(gamevalues)
        if is_valid_game(gamevalues):
            print("Game", gameid[0], "is valid")
            sumofids += int(gameid[0][0])
        else:
            print("Game", gameid[0], "is invalid")
        sumcubepower += get_cubepower(gamevalues)
    print("The solution to part 1 is:", sumofids)
    print("The solution to part 2 is:", sumcubepower)
