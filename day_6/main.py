def main():
    with open("test.txt") as file:
        labs = file.readlines()
    steps = 1
    out_of_map = False

    lab = list(map(lambda x: list(x), labs))

    while out_of_map == False:
        for i in range(len(lab)):
            if "^" in lab[i]:
                dir_index = lab[i].index("^")
                if i == 0:
                    out_of_map = True
                    break
                elif lab[i - 1][dir_index] == "." or lab[i - 1][dir_index] == "X":
                    if lab[i - 1][dir_index] == ".":
                        steps += 1
                    lab[i - 1][dir_index] = "^"
                    lab[i][dir_index] = "|"
                    break
                else:
                    lab[i][dir_index] = ">"
                    break
            if ">" in lab[i]:
                dir_index = lab[i].index(">")
                if dir_index == len(lab[i]) - 2:
                    out_of_map = True
                    break
                elif lab[i][dir_index + 1] == "." or lab[i][dir_index + 1] == "X":
                    if lab[i][dir_index + 1] == ".":
                        steps += 1
                    lab[i][dir_index + 1] = ">"
                    lab[i][dir_index] = "-"
                    break
                else:
                    lab[i][dir_index] = "v"
                    break
            if "v" in lab[i]:
                dir_index = lab[i].index("v")
                if i == len(lab) - 1:
                    out_of_map = True
                    break
                elif lab[i + 1][dir_index] == "." or lab[i + 1][dir_index] == "X":
                    if lab[i + 1][dir_index] == ".":
                        steps += 1
                    lab[i + 1][dir_index] = "v"
                    lab[i][dir_index] = "|"
                    break
                else:
                    lab[i][dir_index] = "<"
                    break
            if "<" in lab[i]:
                dir_index = lab[i].index("<")
                if dir_index == 0:
                    out_of_map = True
                    break
                elif lab[i][dir_index - 1] == "." or lab[i][dir_index - 1] == "X":
                    if lab[i][dir_index - 1] == ".":
                        steps += 1
                    lab[i][dir_index - 1] = "<"
                    lab[i][dir_index] = "-"
                    break
                else:
                    lab[i][dir_index] = "^"
                    break

    print(steps)

if __name__ == "__main__":
    main()