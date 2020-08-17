def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []

    for sub_array in arrays:
        for num in sub_array:
            if num in cache:
                result.append(num)
            else:
                cache[num] = 1

    result = dict.fromkeys(result) # creates a new list without duplicates in the list
    result = list(result)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
