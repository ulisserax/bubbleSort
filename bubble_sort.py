#bubble sort algorithm

def bubble_sort(arr):
    j = 0
    while j < len(arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        j += 1
    return arr

print(bubble_sort([3, 2, 1]))