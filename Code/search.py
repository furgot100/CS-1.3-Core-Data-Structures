#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    '''Best Case: O(1) item is at the beginning of array
        Worst Case: O(n) item is near the end of array
        '''
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    #implement linear search recursively here
    '''Best Case: O(1) item is at the beginning of array
        Worst Case: O(n) item is near the end of array
    ''' 
    if index > (len(array)-1):
        return None

    if item == array[index]:
        return index
    else:
        return linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    '''Should search through the array by halfing off array till array has one and only one answer. If it isn't there
    raise and error(?). Should not go past zero. Is a loop
    Best Case: O(1) Item is the middle item
    Worst Case: O(Logn) last item in the search
    '''
    # implement binary search iteratively here
    left = 0 
    right = len(array) - 1
    while left >= right:
        mid = (left + right) // 2
        if item > array[mid]:
            left = mid + 1
        elif item < array[mid]:
            right = mid - 1
        else:
            return mid
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    


def binary_search_recursive(array, item, left=None, right=None):
    '''Same as above but instead of loop should repeat through the list
    Best Case: O(1) Item is the middle item
    Worst Case: O(Logn) last item in the search
    '''
    # TODO: implement binary search recursively here
    if left == None:
        left = 0
        right = len(array) - 1
    if right >= left:
        target = (right + left) // 2
        if item >array[target]:
            return binary_search_recursive(array, item, target + 1, right)
        elif item < array[target]:
            return binary_search_recursive(array, item, left, target - 1)
        else:
            return target

    return None
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
