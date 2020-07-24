def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # set start and end pointers
    floor = -1
    ceiling = len(arr) - 1

    while floor + 1 < ceiling:

        # get total distance
        distance = ceiling - floor

        # find middle value
        mid = round(distance / 2)
        guess_index = floor + mid

        # set middle index as initial search location
        guess_value = arr[guess_index]

        if guess_value == target:
            return arr.index(guess_value)

        # if target greater than mid, search right half of array
        elif guess_value < target:
            floor = guess_index

        # if target less than mid, search left half of array
        else:
            ceiling = guess_index

    # target not found
    return -1
