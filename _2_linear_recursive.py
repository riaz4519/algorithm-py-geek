def linear_search(arra, n, niddle):

    if n == 0:
        return -1
    elif arra[n-1] == niddle:
        return n - 1
    else:
        return linear_search(arra, n-1, niddle)


if __name__ == "__main__":

    inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    find = 8
    length = len(inputs)

    # with function iterate and find the index
    found = linear_search(inputs, length, find)

    if found == -1:
        print("number does not exist")
    else:
        print("found at index", found)
