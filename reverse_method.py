# O(log n)

def quicksort(my_list):
    quicksortHelper(my_list, 0, len(my_list) - 1)

# recursive function to hide extra arguments for the endpoints of a sublist
def quicksortHelper(my_list, left, right):
    if left < right:
        pivotLocation = partition(my_list, left, right)
        # recursively calls quicksortHelper for the left of the partition
        quicksortHelper(my_list, left, pivotLocation - 1)
        # recursively calls quicksortHelper for the right of the partition
        quicksortHelper(my_list, pivotLocation + 1, right)

def partition(my_list, left, right):
    # find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = my_list[middle]
    my_list[middle] = my_list[right]
    my_list[right] = pivot
    # set boundary point to first position
    boundary = left
    # move items less than pivot to the left
    for index in range(left, right):
        if my_list[index] > pivot:
            swap(my_list, index, boundary)
            boundary += 1
    # exchange the pivot item and the boundary item
    swap(my_list, right, boundary)
    return boundary

# The swap function
def swap(my_list, i, j):
    # exchange the positions of i and j
    temp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp

import random

def main(size = 20, sort_this = quicksort):
    my_list = []
    for count in range(size):
        my_list.append(random.randint(1, size + 1))
    print(my_list)
    sort_this(my_list)
    print(my_list)
    print(my_list[::-1])

main()