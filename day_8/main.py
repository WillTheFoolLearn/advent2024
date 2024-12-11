def main():
    with open("input.txt") as file:
        grid = list(map(lambda x: x.strip(), file.readlines()))

    types = []
    coords = []
    antinodes = set()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                if grid[i][j] not in types:
                    types.append(grid[i][j])
                    coords.append([(j, i)])
                else:
                    coords[types.index(grid[i][j])].append((j, i))

    rows = len(grid)
    cols = len(grid[0])

    for i in range(len(types)):
        for j in range(len(coords[i])):
            for k in range(j + 1, len(coords[i])):
                ij = coords[i][j]
                x, y = ij
                
                comp_x = x - coords[i][k][0]
                comp_y = y - coords[i][k][1]

                count = 0

                while 0 <= x - count * comp_x < cols and 0 <= y - count * comp_y < rows:
                    antinodes.add((x - count * comp_x, y - count * comp_y))
                    count += 1

                count = 0

                while 0 <= x + count * comp_x < cols and 0 <= y + count * comp_y < rows:
                    antinodes.add((x + count * comp_x, y + count * comp_y))
                    count += 1

    print(len(antinodes))

if __name__ == "__main__":
    main()