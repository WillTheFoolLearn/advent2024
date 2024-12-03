def main():
    file = open("input.txt", "r")
    full_list = file.readlines()
    list_1 = []
    list_2 = []
    total = 0

    for i in range(len(full_list)):
        split_list = full_list[i].split()
        list_1.append(int(split_list[0]))
        list_2.append(int(split_list[1]))

    list_1.sort()
    list_2.sort()


    for i in range(len(list_1)):
        count = list_2.count(list_1[i])
        total += list_1[i] * count

    print(total)

    return

if __name__ == "__main__":
    main()