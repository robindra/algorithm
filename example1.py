# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
import time

def sum_of_n(n):
    the_sum = 0
    for i in range(1,n+1):
        the_sum = the_sum + i
    return the_sum
print(sum_of_n(10))


def sum_of_n_2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
        end = time.time()
    return the_sum,end-start

n_values = [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
# for n in n_values:
#     print("Sum is %d required %10.7f seconds" % sum_of_n_2(n))

def sum_of_n_3(n):
    # Calculate the sum of the first n natural numbers
    return (n * (n + 1)) / 2

# List of different values for n
# n_values = [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]

# Loop to calculate and time each sum for different n values
for n in n_values:
    start_time = time.time()  # Record the start time
    result = sum_of_n_3(n*n)    # Call the sum function
    end_time = time.time()      # Record the end time

    elapsed_time = end_time - start_time  # Calculate the time taken
    print(f"Sum for n={n}: {result}, Time taken: {elapsed_time:.6f} seconds")
