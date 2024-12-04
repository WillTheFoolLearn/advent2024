import re

def main():
    with open("input.txt") as file:
        document = file.read()
    
    total = 0
    enabled = True
    regex = "mul\(\d+,\d+\)|don't\(\)|do\(\)"

    matches = re.findall(regex, document)

    for match in matches:
        if match == "do()":
            enabled = True
            continue

        if match == "don't()":
            enabled = False
            continue

        if enabled:
            values = match[4:-1].split(',')
            total += int(values[0]) * int(values[1])

    print(total)

if __name__ == "__main__":
    main()