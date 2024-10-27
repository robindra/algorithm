def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
data = [85, 90, 75, 95, 80]
sorted_data = insertion_sort(data)
print("Insertion Sort:", sorted_data)
