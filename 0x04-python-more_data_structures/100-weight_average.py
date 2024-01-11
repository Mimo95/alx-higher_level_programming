#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weighted_sum = 0
    total_weights = 0

    for tuple in my_list:
        weighted_sum += tuple[0] * tuple[1]
        total_weights += tuple[1]

    return (weighted_sum / total_weights)
