import copy

ARROW = ["^", ">", "v", "<"]
DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]
with open("input.txt") as file:
    labs = file.readlines()
LAB = list(map(lambda x: list(x.strip()), labs))

def main():
    pos = (0, 0)
    steps = set()
    facing = 0
    start_face = facing
    start_pos = pos
    total = 0

    for i in range(len(LAB) - 1):
        for j in range(len(LAB[i]) - 1):
            if LAB[i][j] in ARROW:
                facing = ARROW.index(LAB[i][j])
                pos = (j, i)
                start_face = facing
                start_pos = pos

    while 0 <= pos[0] <= len(LAB[0]) - 1 and 0 <= pos[1] <= len(LAB) - 1:
        steps.add(pos)
        if 0 > pos[0] + DIR[facing][0] or pos[0] + DIR[facing][0] >= len(LAB[0]) or 0 > pos[1] + DIR[facing][1] or pos[1] + DIR[facing][1] >= len(LAB):
            print("We done!", len(steps))
            steps_list = list(steps)
            for step in steps_list:
                total += check_loop(step, start_pos, start_face)

            print(total)
            return
        facing, pos, _ = move(LAB, facing, pos)


def move(grid, facing, pos):
    if grid[pos[1] + DIR[facing][1]][pos[0] + DIR[facing][0]] == "#":
        return (facing + 1) % 4, pos, 1
    else:
        return facing, (pos[0] + DIR[facing][0], pos[1] + DIR[facing][1]), 0
    
    
def check_loop(block, pos, facing):
    block_lab = copy.deepcopy(LAB)
    block_lab[block[1]][block[0]] = "#"
    coords = []
    turned = 0

    while 0 <= pos[0] <= len(block_lab[0]) - 1 and 0 <= pos[1] <= len(block_lab) - 1:
        if 0 > pos[0] + DIR[facing][0] or pos[0] + DIR[facing][0] >= len(block_lab[0]) or 0 > pos[1] + DIR[facing][1] or pos[1] + DIR[facing][1] >= len(block_lab):
            return 0
        facing, pos, turned = move(block_lab, facing, pos)

        if turned:
            turned = 0
            if pos in coords and coords[-1] != pos:
                return 1
            coords.append(pos)
            
if __name__ == "__main__":
    main()