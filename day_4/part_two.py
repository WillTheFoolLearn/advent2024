MAS = ["M", "A", "S"]
with open("input.txt") as file:
        WS = list(map(str.strip, file.readlines()))

def main():
    coords = []
    total = 0

    for y in range(len(WS)):
        for x in range(len(WS[y])):
            if WS[y][x] == "M":
                if x > 1 and y > 1:
                    if checkNext(x, y, -1, -1, 0) in coords:
                        total += 1
                    else:
                        if checkNext(x, y, -1, -1, 0) != 0:
                            coords.append(checkNext(x, y, -1, -1, 0))
                if x < len(WS[y]) - 2 and y > 1:
                    if checkNext(x, y, 1, -1, 0) in coords:
                        total += 1
                    else:
                        if checkNext(x, y, 1, -1, 0) != 0:
                            coords.append(checkNext(x, y, 1, -1, 0))
                if x < len(WS[y]) - 2 and y < len(WS) - 2:
                    if checkNext(x, y, 1, 1, 0) in coords:
                        total += 1
                    else:
                        if checkNext(x, y, 1, 1, 0) != 0:
                            coords.append(checkNext(x, y, 1, 1, 0))
                if x > 1 and y < len(WS) - 2:
                    if checkNext(x, y, -1, 1, 0) in coords:
                        total += 1
                    else:
                        if checkNext(x, y, -1, 1, 0) != 0:
                            coords.append(checkNext(x, y, -1, 1, 0))
                
    print(total)

def checkNext(x, y, x_dir, y_dir, char):
    if MAS[char] == "S":
        return (x - x_dir, y - y_dir)
    
    if WS[y + y_dir][x + x_dir] == MAS[char + 1]:
        return checkNext(x + x_dir, y + y_dir, x_dir, y_dir, char + 1)
    
    return 0
    

if __name__ == "__main__":
    main()