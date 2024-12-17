import time
from collections import defaultdict


def main():
    start = time.time()
    with open("input.txt") as file:
        stones = file.read()
    
    stone_array = list(map(int, stones.split()))
    flat_array = stone_array[:]
    stone_dict = {}
    blink = 75

    for elem in flat_array:
        if elem in stone_dict:
            stone_dict[elem] += 1
        else:
            stone_dict[elem] = 1

    while blink > 0:
        stone_dict = blink_func(stone_dict)
        blink -= 1
    
    print(sum(stone_dict.values()))
    print(time.time() - start)


def blink_func(stones):
    temp_dict = defaultdict(int)
    for key in stones:
        if key == 0:
            temp_dict[1] += stones[key]
        elif len(str(key)) % 2 == 0:
            string = str(key)
            left = int(string[:(len(string) // 2)])
            right = int(string[(len(string) // 2):])
            temp_dict[left] += stones[key]
            temp_dict[right] += stones[key]
        else:
            temp_dict[key * 2024] += stones[key]

    return temp_dict


if __name__ == "__main__":
    main()