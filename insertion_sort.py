# Adapted from code by Hritik Shah, as shared on GeeksforGeeks.
# Source: https://www.geeksforgeeks.org/insertion-sort/

# Function to sort array using insertion sort in decreasing order
# Change the array name to match the name as per the pseudocode provided in In Chapter 2 of Introduction to Algorithms
def insertion_Sort(arr):
       # Loop through the array starting at index 1
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        #Change to decreasing insertion assort 
        while j >= 0 and key > arr[j]:
            arr[j +1] = arr[j]
            j -= 1
        arr[j +1] = key

# A utility function to print array of size n
def printArray(arr):
    for i in range(len(arr)):
    #changing final print to have commas and spaces and remove comma from last element
        if i == len(arr) - 1:
         print (arr[i])
        else:
         print(arr[i], end=", ")
    print()

# Driver method
if __name__ == "__main__":
    # adding negatives to the array
    arr = [-1, 3, -0.5, 2, -3]
    insertion_Sort(arr)
    printArray(arr)
