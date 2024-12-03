def main():
    file = open("input.txt", "r")
    full_list = file.readlines()
    total = 0

    for report in full_list:
        levels = list(map(int, report.split()))
        state = 0

        for i in range(len(levels) - 1):
            if levels[i] == levels[i + 1]:
                break
            
            if state == 0:
                if levels[i] > levels[i + 1]:
                    state = 1
                else:
                    state = 2
            else:
                if state == 1:
                    if levels[i] < levels[i + 1]:
                        break
                else:
                    if levels[i] > levels[i + 1]:
                        break
            
            if not (-4 < (levels[i] - levels[i + 1]) < 4):
                break

            if i == (len(levels) - 2):
                total += 1
            
    print(total)

    return total

if __name__ == "__main__":
    main()