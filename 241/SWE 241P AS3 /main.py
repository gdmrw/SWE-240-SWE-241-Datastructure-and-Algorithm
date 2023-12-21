# Step 1: groupAnagram function
import timeit
import random
from collections import defaultdict


                # strings, lambda word: ''.join(mergeSort(list(word)
def groupAnagram(strings, sort_func):     # use defaultdict to store multiple value then achieve return list  of lists
    # Initialize a dictionary to store anagrams
    anagrams = defaultdict(list)

    # Iterate through each word in the input list
    for word in strings:
        # Sort the word using the provided sorting function
        sorted_word = sort_func(word)   # key  # put word in origin string and use the sort function to sort and as a key

        # Append the original word to the list of anagrams with the same sorted form
        anagrams[sorted_word].append(word)      # value

    # Return a list of lists containing grouped anagrams
    return list(anagrams.values())          #

# Step 2: sortString using Mergesort


def mergeSort(arr):    # time comp : O(nlogn)  space comp : O(n) need extra space(list) to store

    # Base case: if the array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Split the array in half and recursively sort each half
    middle = len(arr) // 2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements in the left and right lists and merge them in sorted order
    while i < len(left) and j < len(right):   # check if there is still var in list
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from both lists
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Step 2: sortString using Quicksort


# time comp:  avg O(nlogn), space comp avg: O(logn)
# ext worst case O(n^2)  (order decrement) worst O(n) ##recursive occupied the stack space

def quickSort(arr):
    # Base case: if the array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (first element in this case)
    pivot = arr[0]

    # Divide the array into two lists: elements less than or equal to the pivot, and elements greater than the pivot
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    # Recursively sort both sublists and combine them with the pivot
    return quickSort(less) + [pivot] + quickSort(greater)


# Testing

strings = ["bucket","rat","mango","tango","gtano","tar"]

# use sort function sort ASCII and group into a single string again
# Using Mergesort
print(groupAnagram(strings, lambda word: ''.join(mergeSort(list(word)))))   # group anagram from

# Using Quicksort
print(groupAnagram(strings, lambda word: ''.join(quickSort(list(word)))))




#time cost test
# arr = [random.randint(1, 1000) for _ in range(1000)]
# mergesort_execution_time = timeit.timeit(lambda: mergeSort(arr.copy()),number= 1)
# quicksort_execution_time = timeit.timeit(lambda: quickSort(arr.copy()),number= 1)
# # you can see slightly run time different due to constant difference
# print(f"merge sort time cost: {mergesort_execution_time} sec")
# print(f"quick sort time cost: {quicksort_execution_time} sec")


# sort function test
# test_list = [4,2,3,1,7,5]
# print(mergeSort(test_list))
# print(quickSort(test_list))


# print(''.join(mergeSort(list("mango"))))