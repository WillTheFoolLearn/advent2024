import time
import numpy as py

with open("input.txt") as file:
    PLOT = list(map(lambda i: i.strip(), file.readlines()))

def main():
    start = time.time()
    visited = set()
    section_total = 0
    peri_total = 0
    type_set = set()
    

    def check_plot(j, i, plot_type):
        if j < 0 or j == len(PLOT[0] )or i < 0 or i == len(PLOT):
            return
        
        if (j, i) in visited:
            return
        
        if plot_type == PLOT[i][j]:
            visited.add((j, i))
            type_set.add((j, i))
            check_plot(j - 1, i, plot_type)
            check_plot(j + 1, i, plot_type)
            check_plot(j, i - 1, plot_type)
            check_plot(j, i + 1, plot_type)
            return
        else:
            return

    
    for i in range(len(PLOT)):
        for j in range(len(PLOT[0])):
            if (j, i) not in visited:
                check_plot(j, i, PLOT[i][j])
                section_total += peri_sides(type_set) * len(type_set)
                peri_total += len(type_set) * ((len(type_set) * 4) - (peri_count(type_set) * 2))
                type_set.clear()

    print("The total for the perimeter calculation is", peri_total, "and the total for the section calculation is", section_total)
    print(time.time() - start)

def peri_count(type_set):
    type_list = list(type_set)
    total = 0
    for i in range(len(type_list) - 1):
        for j in range(i + 1, len(type_list)):
            if (type_list[j][0] - 1, type_list[j][1]) == type_list[i] or (type_list[j][0] + 1, type_list[j][1]) == type_list[i] or (type_list[j][0], type_list[j][1] - 1) == type_list[i] or (type_list[j][0], type_list[j][1] + 1) == type_list[i]:
                total += 1

    return total

def peri_sides(type_set):
    type_list = list(type_set)
    type = PLOT[type_list[0][1]][type_list[0][0]]

    plot_sides_n = {}
    plot_sides_s = {}
    plot_sides_e = {}
    plot_sides_w = {}
    sides = 0
    all_plots = [plot_sides_e, plot_sides_n, plot_sides_s, plot_sides_w]


    for elem in type_list:

        if elem[0] - 1 >= 0:
            if PLOT[elem[1]][elem[0] - 1] != type:
                if elem[0] in plot_sides_w:
                    plot_sides_w[elem[0]].append(elem[1])
                else:
                    plot_sides_w[elem[0]] = [elem[1]]
        else:
            if elem[0] in plot_sides_w:
                plot_sides_w[elem[0]].append(elem[1])
            else:
                plot_sides_w[elem[0]] = [elem[1]]

        if elem[0] + 1 < len(PLOT[0]):
            if PLOT[elem[1]][elem[0] + 1] != type:
                if elem[0] in plot_sides_e:
                    plot_sides_e[elem[0]].append(elem[1])
                else:
                    plot_sides_e[elem[0]] = [elem[1]]
        else:
            if elem[0] in plot_sides_e:
                plot_sides_e[elem[0]].append(elem[1])
            else:
                plot_sides_e[elem[0]] = [elem[1]]

        if elem[1] - 1 >= 0:
            if PLOT[elem[1] - 1][elem[0]] != type:
                if elem[1] in plot_sides_n:
                    plot_sides_n[elem[1]].append(elem[0])
                else:
                    plot_sides_n[elem[1]] = [elem[0]]
        else:
            if elem[1] in plot_sides_n:
                plot_sides_n[elem[1]].append(elem[0])
            else:
                plot_sides_n[elem[1]] = [elem[0]]
        
        if elem[1] + 1 < len(PLOT):
            if PLOT[elem[1] + 1][elem[0]] != type:
                if elem[1] in plot_sides_s:
                    plot_sides_s[elem[1]].append(elem[0])
                else:
                    plot_sides_s[elem[1]] = [elem[0]]
        else:
            if elem[1] in plot_sides_s:
                plot_sides_s[elem[1]].append(elem[0])
            else:
                plot_sides_s[elem[1]] = [elem[0]]

    for plot in all_plots:
        for value in plot.values():
            if len(value) == 0:
                continue
            elif len(value) == 1:
                sides += 1
            else:
                sides += 1
                value.sort()
                diff = py.diff(value)
                if len(diff) == 1 and diff[0] == 1:
                    continue
                for i in range(len(diff)):
                    if diff[i] > 1:
                        sides += 1
        
    return sides

if __name__ == "__main__":
    main()
