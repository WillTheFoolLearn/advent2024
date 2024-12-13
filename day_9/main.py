import time

def main():
    with open("input.txt") as file:
        disk_map = file.read()

    unpacked = []
    total = 0
    
    for i, char in enumerate(disk_map):
        num = int(char)
        if i % 2 == 0:
            while num > 0:
                unpacked.append(i // 2)
                num -= 1
        else:
            while num > 0:
                unpacked.append(".")
                num -= 1

    last_index = -1
    start_index = 0
    cur_id = len(unpacked)

    while abs(last_index) < len(unpacked):
        while unpacked[last_index] == "." or unpacked[last_index] > cur_id:
                last_index -= 1

        if unpacked[last_index] < cur_id:
            cur_id = unpacked[last_index]
            
        counter = 0

        while unpacked[last_index] == cur_id:
            counter += 1
            last_index -= 1
            if abs(last_index) >= len(unpacked):
                break

        dot_count = 0
        index = unpacked.index(".")

        for i in range(index, len(unpacked) + last_index + 1):
            if unpacked[i] == ".":
                if dot_count == 0:
                    start_index = i
                dot_count += 1
                if dot_count == counter:
                    while dot_count > 0:
                        unpacked[start_index + dot_count - 1] = cur_id
                        unpacked[last_index + dot_count] = "."
                        dot_count -= 1
                    break
            else:
                dot_count = 0

    for i, num in enumerate(unpacked):
        if num != ".":
            total += i * num

    print(total)

if __name__ == "__main__":
    main()