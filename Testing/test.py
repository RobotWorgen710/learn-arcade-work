# Selection Sort
def selection_sort(my_list):

    for current_pos in range(len(my_list)):
        min_pos = current_pos
        for scan_pos in range(current_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        temp = my_list[min_pos]
        my_list[min_pos] = my_list[current_pos]
        my_list[current_pos] = temp


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
selection_sort(my_list)
print(my_list)