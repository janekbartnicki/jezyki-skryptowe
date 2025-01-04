def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


sorting_data = []
with open('./dane_zadanie38.txt') as file:
    sorting_data = list(map(int, file.readlines()))

print(bubble_sort(sorting_data))
print(insertion_sort(sorting_data))
print(quick_sort(sorting_data))


with open('./output_zadanie38.txt', 'w') as file:
    file.writelines(f'{element}\n' for element in quick_sort(sorting_data))
