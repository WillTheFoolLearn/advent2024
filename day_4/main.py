XMAS = ["X", "M", "A", "S"]
with open("input.txt") as file:
        WS = list(map(str.strip, file.readlines()))

def main():
    total = 0

    for y in range(len(WS)):
        for x in range(len(WS[y])):
            if WS[y][x] == "X":
                if x > 2 and y > 2:
                    total += checkNext(x, y, -1, -1, 0)
                if y > 2:
                    total += checkNext(x, y, 0, -1, 0)
                if x < len(WS[y]) - 3 and y > 2:
                    total += checkNext(x, y, 1, -1, 0)
                if x < len(WS[y]) - 3:
                    total += checkNext(x, y, 1, 0, 0)
                if x < len(WS[y]) - 3 and y < len(WS) - 3:
                    total += checkNext(x, y, 1, 1, 0)
                if 3 and y < len(WS) - 3:
                    total += checkNext(x, y, 0, 1, 0)
                if x > 2 and y < len(WS) - 3:
                    total += checkNext(x, y, -1, 1, 0)
                if x > 2:
                    total += checkNext(x, y, -1, 0, 0)
                
    print(total)

def checkNext(x, y, x_dir, y_dir, char):
    if XMAS[char] == "S":
        return 1
    
    if WS[y + y_dir][x + x_dir] == XMAS[char + 1]:
        return checkNext(x + x_dir, y + y_dir, x_dir, y_dir, char + 1)
    
    return 0
    


if __name__ == "__main__":
    main()