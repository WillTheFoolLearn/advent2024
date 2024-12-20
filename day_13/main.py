import re

def main():
    with open("input.txt") as file:
        machines = file.read()
    
    machine_list =  machines.split("\n\n")
    
    total = 0  

    for machine in machine_list:
        pattern = r"\d+"
        matches = list(map(int, re.findall(pattern, machine)))

        x1, x2, y1, y2, p1, p2 = matches
        p1 += 10 ** 13
        p2 += 10 ** 13
        machine_1 = [x1, y1, p1]
        machine_2 = [x2, y2, p2]
        lcm = (x1, x2)
        output = []
        y_value = 0
        x_value = 0

        machine_1 = list(map(lambda x: x * lcm[1], machine_1))
        machine_2 = list(map(lambda x: x * lcm[0], machine_2))

        for i in range(len(machine_1)):
            output.append(machine_1[i] - machine_2[i])
        
        if output[2] % output[1] == 0: 
            y_value = abs(output[2] // output[1])

        if (p1 - (y1 * y_value)) % x1 == 0:
            x_value = (p1 - (y1 * y_value)) // x1

        if x_value * x1 + y_value * y1 == p1 and x_value * x2 + y_value * y2 == p2:
            total += x_value * 3 + y_value
        
        # Part 1 solution stuff below
        # while p1 - (x1 * index) > 0:
        #     index += 1
        #     if (p1 - (x1 * index)) % y1 == 0:
        #         if index < 100 and ((p1 - (x1 * index)) // y1) < 100:
        #             get_prize.append((index, ((p1 - (x1 * index)) // y1)))
        
        # for attempt in get_prize:
        #     if attempt[0] * x2 + attempt[1] * y2 == p2:
        #         if attempt[0] + attempt[1] < lowest[0] + lowest[1]:
        #             lowest = (attempt[0], attempt[1])
        
        # if lowest[0] < 101:
        #     total += lowest[0] * 3 + lowest[1]
    
    print(total)
        

if __name__ == "__main__":
    main()