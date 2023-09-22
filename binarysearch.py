# time complexity: O(1)
# n1= 10
# n2= 20
# print(n1+n2)

# parallal series: O(1)
# a=int(input("enter the number: "))
# summation= a*(a+1)/2
# print(summation)


# linear search:

n = [5, 7, 23, 56, 33, 55, 77, 88, 99, 100]
for i in range(len(n)):
    if n[i] == 88:
        print("Found at index", i)


# binary search: O(log n)
def binary_search(arr, target):
    # Initialize the left pointer to the first index of the array.
    left = 0
    # Initialize the right pointer to the last index of the array.
    right = len(arr) - 1

    # Continue the search as long as the left pointer is less than or equal to the right pointer.
    while left <= right:
        # Calculate the middle index of the current search range.
        mid = (left + right) // 2

        # Check if the middle element is equal to the target.
        if arr[mid] == target:
            # If found, return the index of the target element.
            return mid

        elif arr[mid] < target:  # If the middle element is less than the target,
            # Adjust the left pointer to search the right half of the current range.
            left = mid + 1

        else:                   # If the middle element is greater than the target,
            # Adjust the right pointer to search the left half of the current range.
            right = mid - 1

    # If the target element is not found in the array, return -1 to indicate it was not found.
    return -1


# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 13
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
