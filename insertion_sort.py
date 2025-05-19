# Adapted from code by Hritik Shah, as shared on GeeksforGeeks.
# Source: https://www.geeksforgeeks.org/insertion-sort/

# Function to sort array using insertion sort
# Change the array name to match the name as per the pseudocode provided in In Chapter 2 of Introduction to Algorithms
def insertion_Sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Change to decreaseing instertion assort 
        while j >= 0 and key > arr[j]:
            arr[j +1] = arr[j]
            j -= 1
            arr[j +1] = key

# A utility function to print array of size n
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver method
if __name__ == "__main__":
    # change in numbers for the array
    arr = [323, 23, 1, 0.01, 3.2]
    insertion_Sort(arr)
    printArray(arr)
