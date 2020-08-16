def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {} # dict
    for i in range(len(weights)): # loop over lists of weights
        cache[weights[i]] = i # store each weights list index as its value

    for i in range(len(weights)):
        difference = limit - weights[i]
        if difference in cache:
            return (max(i, cache[difference]), min(i, cache[difference]))    

    return None
