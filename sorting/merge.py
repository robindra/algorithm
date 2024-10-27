def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        L = arr[:mid]        # Split the array into two halves
        R = arr[mid:]

        merge_sort(L)        # Sort the first half
        merge_sort(R)        # Sort the second half

        i = j = k = 0

        # Copy data to temporary arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Example usage:
scores = [85, 90, 75, 95, 80]
sorted_scores = merge_sort(scores)
print("Merge Sort Result:", sorted_scores)
