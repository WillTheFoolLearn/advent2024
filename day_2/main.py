def main():
    file = open("input.txt", "r")
    full_list = file.readlines()
    total = 0

    for report in full_list:
        levels = list(map(int, report.split()))

        for i in range(1, len(levels) - 1):
            if levels[i-1] < levels[i] < levels[i+1] or levels[i-1] > levels[i] > levels[i+1]:
                if abs(levels[i-1] -  levels[i]) > 3 or abs(levels[i] -  levels[i + 1]) > 3:
                    if not remove_elem(levels, i):
                        break
            else:
                if not remove_elem(levels, i):
                    break

            if i == len(levels) - 2:
                total += 1

    print(total)

def remove_elem(lvl, idx):
    lvl_l = lvl[:]
    lvl_m = lvl[:]
    lvl_r = lvl[:]
    del lvl_l[idx - 1]
    del lvl_m[idx]
    del lvl_r[idx + 1]

    return check_tolerance(lvl_l) or check_tolerance(lvl_m) or check_tolerance(lvl_r)

def check_tolerance(lvl):
    for i in range(1, len(lvl) - 1):
        if lvl[i-1] < lvl[i] < lvl[i+1] or lvl[i-1] > lvl[i] > lvl[i+1]:
            if abs(lvl[i-1] -  lvl[i]) > 3 or abs(lvl[i] -  lvl[i + 1]) > 3:
                break
        else:
            break

        if i == len(lvl) - 2:
            return True
    
    return False

if __name__ == "__main__":
    main()