import math

def task():
    unique_products = sorted(set(i * j for i in range(1, 7) for j in range(1, 7)))
    unique_sums = sorted(set(i + j for i in range(1, 7) for j in range(1, 7)))

    probability_matrix = [[0 for _ in range(len(unique_products))] for _ in range(len(unique_sums))]

    product_index = [0] * (unique_products[-1] + 1)
    for i, value in enumerate(unique_products):
        product_index[value] = i

    sum_index = [0] * (unique_sums[-1] + 1)
    for i, value in enumerate(unique_sums):
        sum_index[value] = i

    for i in range(1, 7):
        for j in range(1, 7):
            sum_idx = sum_index[i + j]
            product_idx = product_index[i * j]
            probability_matrix[sum_idx][product_idx] = 1 if i == j else 2

    for i in range(len(probability_matrix)):
        for j in range(len(probability_matrix[i])):
            probability_matrix[i][j] /= 36

    entropy_sums, entropy_products, joint_entropy, conditional_entropy, mutual_information = 0, 0, 0, 0, 0
    sum_probabilities = []

    for i in range(len(probability_matrix)):
        total_prob = sum(probability_matrix[i])
        sum_probabilities.append(total_prob)
        if total_prob > 0:
            entropy_sums -= math.log2(total_prob) * total_prob

    for j in range(len(probability_matrix[0])):
        total_prob = sum(probability_matrix[i][j] for i in range(len(probability_matrix)))
        if total_prob > 0:
            entropy_products -= math.log2(total_prob) * total_prob

    for i in range(len(probability_matrix)):
        for j in range(len(probability_matrix[i])):
            if probability_matrix[i][j] > 0:
                conditional_entropy -= math.log2(probability_matrix[i][j] / sum_probabilities[i]) * probability_matrix[i][j]

    joint_entropy = entropy_sums + conditional_entropy
    mutual_information = entropy_products - conditional_entropy

    results = [joint_entropy, entropy_sums, entropy_products, conditional_entropy, mutual_information]
    results = [round(value, 2) for value in results]

    return results
