def main():
    file = open("test.txt", "r")
    full_list = file.readlines()
    total = 0
    state = 0

    for report in full_list:
        levels = list(map(int, report.split()))

        for i in range(len(levels) - 1):
            if levels[i] == levels[i + 1]:
                continue
            
            if state == 0:
                if levels[i] > levels[i + 1]:
                    state = 1
                else:
                    state = 2
            else:
                if state == 1:
                    if levels[i] < levels[i + 1]:
                        continue
                else:
                    if levels[i] < levels[i + 1]:
                        continue
            
            if not (-4 < levels[i] - levels[i + 1] < 4):
                continue

            if i == (len(levels) - 1):
                total += 1
            
    print(total)

    return

if __name__ == "__main__":
    main()