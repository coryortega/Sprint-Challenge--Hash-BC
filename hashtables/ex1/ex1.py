#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    #implement a function `get_indices_of_item_weights` 
    # that finds two items whose sum of weights equals the weight limit `limit`. 
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    # Your function will return an instance of an `Answer` tuple that has the following form:

    # (zero, one)
    
    for i in range(length):
        next = hash_table_retrieve(ht, (limit - weights[i]))
        if next:
            if next >= 1:
                return [next, i]
            else:
                return [i, next]
        
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
