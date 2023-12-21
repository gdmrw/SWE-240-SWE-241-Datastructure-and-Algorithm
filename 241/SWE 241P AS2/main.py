def binary_search(li,val):
    """
    :param li: searching list[int]
    :param val: int
    :return: target position, if not exist will return [-1,-1]
    """
    result_index = []     # initialize result list to show the result in the list at an end
    left = 0                # initialize start and end index
    right = len(li) - 1
    while left <= right:                # start binary searching
        mid = (left + right) // 2
        if li[mid] == val:
            result_index.append(mid)     # add the index to result list if target found
            left_mbrepeat = mid - 1         # start traverse for multi match answer
            while li[left_mbrepeat] == val:
                result_index.insert(0,left_mbrepeat)  # add the result at the head of the result list
                left_mbrepeat -= 1
            right_mbrepeat = mid + 1
            while li[right_mbrepeat] == val:
                result_index.append(right_mbrepeat)  # add the result at the tail of the result list
                right_mbrepeat += 1        # end traverse for multi match answer
            break  # break to avoid infinite loop

        elif li[mid] > val:                 # if not match, start position judgment and start the next round of search
            right = mid - 1

        else:
            left = mid + 1

    else:
        result_index = [-1, -1]           # Not result found, jump out the while loop and return require list

    print(result_index)                     # Output

# test case
nums = [2,4,6,8,10,14,16]
nums_target_val = 12

binary_search(nums,nums_target_val)


def matrix_binary_search(matrix, target):
    """
    :param matrix: matrix list[list[int]]
    :param target: int
    :return: bool
    """
    if not matrix or not matrix[0]:  # judge if the matrix is empty or the first row is empty
        return False
    m, n = len(matrix), len(matrix[0])
    low = 0
    high = m * n - 1  # the last index is m*n - 1 because we start counting from 0
    while low <= high:  # continue searching while low is less than or equal to high
        mid = low + (high - low) // 2
        mid_value = matrix[mid // n][mid % n]   # index
        if mid_value == target:
            return True
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return False  # target not found


# # test cases
matrixtest = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matrix_target_val = 12

print(matrix_binary_search(matrixtest, matrix_target_val))
