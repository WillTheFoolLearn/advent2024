with open("input.txt") as file:
    TOPO = topo = list(map(lambda i: i.strip(), file.readlines()))

ROWS = len(TOPO)
COLS = len(TOPO[0])

def main():
    trailheads = 0

    for i in range(len(topo)):
        for j, num in enumerate(TOPO[i]):
            if num == "0":
                trailheads += dfs(i, j, 0)

    print(trailheads)

def dfs(i, j, step):
    if i < 0 or i == ROWS or j < 0 or j == COLS:
        return 0
    
    if TOPO[i][j] != str(step):
        return 0
    
    if TOPO[i][j] == "9" and step == 9:
        return 1

    return dfs(i + 1, j, step + 1) + dfs(i, j + 1, step + 1) + \
        dfs(i - 1, j, step + 1) + dfs(i, j - 1, step + 1)

if __name__ == "__main__":
    main()