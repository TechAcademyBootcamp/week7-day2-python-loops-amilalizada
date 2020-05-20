def bubble_sort(bubble_list):
    for i in range(len(bubble_list)):
        for j in range(len(bubble_list) - 1):
            if bubble_list[j] > bubble_list[j+1]:
                bubble_list[j], bubble_list[j+1] = bubble_list[j+1], bubble_list[j]
bubble_list = [19, 13, 6, 2, 18, 8]
bubble_sort(bubble_list)
print(bubble_list)                