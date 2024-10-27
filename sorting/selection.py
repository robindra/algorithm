def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:  # Change to > for descending order
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage:
scores = [85, 90, 75, 95, 80]
sorted_scores = selection_sort(scores)
print("Selection Sort Result:", sorted_scores)
