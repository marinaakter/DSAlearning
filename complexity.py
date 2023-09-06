# time complexity: O(1)
# n1= 10
# n2= 20
# print(n1+n2)

# parallal series: O(1)
# a=int(input("enter the number: "))
# summation= a*(a+1)/2
# print(summation)


# linear search:

# n = [5, 7, 23, 56, 33, 55, 77, 88, 99, 100]
# for i in range(len(n)):
#     if n[i] == 88:
#         print("Found at index", i)
        
        
        
#binary search: O(log n)
def binary_search(arr, target):
    left = 0              # Initialize the left pointer to the first index of the array.
    right = len(arr) - 1  # Initialize the right pointer to the last index of the array.

    while left <= right:  # Continue the search as long as the left pointer is less than or equal to the right pointer.
        mid = (left + right) // 2  # Calculate the middle index of the current search range.

        if arr[mid] == target:  # Check if the middle element is equal to the target.
            return mid         # If found, return the index of the target element.

        elif arr[mid] < target:  # If the middle element is less than the target,
            left = mid + 1      # Adjust the left pointer to search the right half of the current range.

        else:                   # If the middle element is greater than the target,
            right = mid - 1     # Adjust the right pointer to search the left half of the current range.

    return -1  # If the target element is not found in the array, return -1 to indicate it was not found.

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 13
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")






