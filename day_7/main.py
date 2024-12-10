def main():
    with open("input.txt") as file:
        equations = file.readlines()
    
    total = 0

    for equation in equations:
        answer, numbers = equation.split(":")
        num_list = list(map(int, numbers.split()))
        running_total = num_list[0]

        if operand_check(int(answer), num_list[1:], running_total):
            total += int(answer)
    
    print(total)

def operand_check(answer, num_list, running_total):
    if not num_list:
        if answer - running_total == 0:
            return 1
        return 0
    
    if operand_check(answer, num_list[1:], running_total + num_list[0]):
        return 1
    
    if operand_check(answer, num_list[1:], running_total * num_list[0]):
        return 1
    
    if operand_check(answer, num_list[1:], int(str(running_total) + str(num_list[0]))):
        return 1

if __name__ == "__main__":
    main()