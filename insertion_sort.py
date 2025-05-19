# Adapted from code by Hritik Shah, as shared on GeeksforGeeks.
# Source: https://www.geeksforgeeks.org/insertion-sort/

# Function to sort array using insertion sort
def insertion_Sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j +1] = A[j]
            j -= 1
            A[j +1] = key

# A utility function to print array of size n
def printArray(A):
    for i in range(len(A)):
        print(A[i], end=" ")
    print()

# Driver method
if __name__ == "__main__":
    A = [3, 4, 9, 1000, 34.3]
    insertion_Sort(A)
    printArray(A)

