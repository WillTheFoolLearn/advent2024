def main():
    with open("input.txt") as file:
        doc = file.read().split("\n\n")

        rules, updates = doc
        rules_lines = rules.split("\n")
        update_lines = updates.split("\n")
        rules_dict = {}
        total = 0
        bad_update = False
        to_add = False

        rules_list = list(map(lambda x: x.split("|"), rules_lines))

        for lists in rules_list:
            if not rules_dict.get(lists[0]):
                rules_dict[lists[0]] = [lists[1]]
            else:
                rules_dict[lists[0]].append(lists[1])

        for update in update_lines:
            split_update = update.split(',')
            bad_update = False
            for i in range(len(split_update)):
                if split_update[i] in rules_dict:
                    for val in rules_dict[split_update[i]]:
                        if val in split_update: 
                            if i > split_update.index(val) and val in split_update:
                                bad_update = True
                                to_add = True
                            else:
                                continue

            while bad_update:
                bad_update = False
                for i in range(len(split_update)):
                    if split_update[i] in rules_dict:
                        for val in rules_dict[split_update[i]]:
                            if val in split_update: 
                                if i > split_update.index(val) and val in split_update:
                                    hold_value = split_update[i]
                                    hold_index = split_update.index(val)
                                    split_update[i] = val
                                    split_update[hold_index] = hold_value
                                    bad_update = True

            if to_add:
                total += int(split_update[(i + 1) // 2])
                to_add = False

        print(total)

if __name__ == "__main__":
    main()