def knapsack(weights, values, WEIGHT):
    x = [0 for i in range(len(weights))]
    weight = 0
    i = 0

    while (weight < WEIGHT):

        if weight + weights[i] < WEIGHT:
            x[i] = 1
            weight = weight + weights[i]
        else:
            x[i] = (WEIGHT - weight) / weights[i]
            weight = WEIGHT
        i += 1

    return x

def weights_values_precision_expand(weights, values, precision):
    ### caution exponential expansion here
    new_weights = []
    new_values = []
    for index, weight in enumerate(weights):
        value = values[index]
        # print weight, value

        for i in xrange(10 ** precision):
            new_weights.append(float(weight) / (10 ** precision))
            new_values.append(value)

    return new_weights, new_values


def knapsack_dynamic(weights_param, values_param, WEIGHT, precision=0):
    # make weights and values 1 indexed
    weights, values = weights_values_precision_expand(weights_param, values_param, precision)

    weights = [0] + weights
    values = [0] + values

    V = [[0 for i in range(WEIGHT * 10 ** precision + 1)] for j in range(len(weights))]
    for j in range(WEIGHT * 10 ** precision + 1):
        for i in range(1, len(weights)):
            i_index_1 = i - 1
            j_index_1 = j

            V1 = V[i_index_1][j_index_1]

            i_index_2 = i - 1
            j_index_2 = j - int(weights[i] * 10 ** precision)

            if (j_index_2 < 0):
                # for j < 0, V[i,j] = -infinity so V2 < V1 always
                V[i][j] = V1
            else:
                V2 = V[i_index_2][j_index_2] + values[i]
                V[i][j] = max([V1, V2])

    # for item in V:
    #     print item

    # we have the matrix now lets trace the path
    selection = [0 for i in range(len(weights))]

    for i in range(len(weights))[::-1]:
        i_index_1 = i - 1
        j_index_1 = j

        V1 = V[i_index_1][j_index_1]

        i_index_2 = i - 1
        j_index_2 = int(j - (weights[i] * 10 ** precision))

        V2 = V[i_index_2][j_index_2] + values[i]

        if (V[i][j] == V1):
            selection[i] = 0
        else:
            selection[i] = 1
            j = j_index_2

    omit_zero_index_selection = selection[1:]
    normalized_selection = []
    for i in range (0,len(omit_zero_index_selection), 10 ** precision):
        normalized_selection.append(
            float(sum(omit_zero_index_selection[i:i+10**precision])) / 10 ** precision
        )

    return normalized_selection

    # return V


def value_of_sigma_w_v(weights, values, solution):
    return sum([a * b * c for a, b, c in zip(weights, values, solution)])

# print knapsack(weights=[10,20,30,40,50], values=[20,30,66,40,60], WEIGHT=100)
weight_data = [10,20,30,40,50]
value_data = [20,30,66,40,60]
WEIGHT = 100

# sort the weight and value
zipped_wv = zip(weight_data, value_data)
sorted_wv = sorted(zipped_wv, key=lambda x: float(x[1])/x[0], reverse=True)
weight_data, value_data = zip(*sorted_wv)

print "sorted weight: ", weight_data
print "value: ", value_data

greedy_solution = knapsack(weight_data, value_data, WEIGHT)
print "greedy solution", greedy_solution
print "maximization value", value_of_sigma_w_v(weight_data, value_data, greedy_solution)

precision_0 =  knapsack_dynamic(weight_data, value_data, WEIGHT, 0)
print
print "dynamic precision 0", precision_0
print "maximization value", value_of_sigma_w_v(weight_data, value_data, precision_0)


precision_1 =  knapsack_dynamic(weight_data, value_data, WEIGHT, 1)
print
print "dynamic precision 1", precision_1
print "maximization value", value_of_sigma_w_v(weight_data, value_data, precision_1)

precision_2 =  knapsack_dynamic(weight_data, value_data, WEIGHT, 2)
print
print "dynamic precision 2", precision_2
print "maximization value", value_of_sigma_w_v(weight_data, value_data, precision_2)

# precision_3 =  knapsack_dynamic(weight_data, value_data, WEIGHT, 3)
# print "maximize sigma w * v = ", sum([a * b * c for a, b, c in zip(weight_data, value_data, precision_3)])

# precision_1 =  knapsack_dynamic(weight_data, value_data, 11, 1)
# precision_2 =  knapsack_dynamic(weight_data, value_data, 11, 2)
# precision_3 =  knapsack_dynamic(weight_data, value_data, 11, 3)
# precision_4 =  knapsack_dynamic(weight_data, value_data, 11, 4)

