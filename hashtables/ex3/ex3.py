def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for item in array:
        for i in item:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
    for index, number in enumerate(cache):
        if cache[number] == len(arrays):
            result.append(number)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
