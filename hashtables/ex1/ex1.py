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
            if length == 2:
                return(1, 0)
            return (i, weight_result)
        return None


def get_check(check):
    if check is not None:
        print(str(check[0]+"_"+check[1]))
    else:
        print("None")
