def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # Change to < for ascending order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage:
scores = [85, 90, 75, 95, 80]
sorted_scores = bubble_sort(scores)
print("Bubble Sort Result:", sorted_scores)
