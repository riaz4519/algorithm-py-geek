# need to have a array of inputs
# need to have the number which to find
# need a function itarate the inputs and outputs
# if return is -1 then its not there
# if other wise send back the index

def find_index(arr, n, niddle):

    for i in range(0, n):
        if arr[i] == niddle:
            return i
    return -1


# drive code

if __name__ == "__main__":

    inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    find = 8
    length = len(inputs)

    # with function iterate and find the index
    found = find_index(inputs, length, find)

    if found == -1:
        print("number does not exist")
    else:
        print("found at index", found)
