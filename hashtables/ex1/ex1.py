def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
#    Create a cache
    cache = {}
    for i in range(0, length):
        current_weight = weights[i]
        difference = limit - current_weight
        # Store the difference in a variable
        weight_result = difference
        if weight_result in cache:
            return (i, cache[weight_result])
        cache[current_weight] = i
    return None


def get_check(check):
    if check is not None:
        print(str(check[0]+"_"+check[1]))
    else:
        print("None")
