
import numpy as np


def task(csv_string):

    matrix = np.array([list(map(int, row.split(','))) for row in csv_string.strip().split('\n')])

    n, k = matrix.shape

    entropy = 0



    for j in range(n):

        for i in range(k):

            l_ij = matrix[j, i]

            if l_ij > 0:

                entropy += (l_ij / (n - 1)) * np.log2(l_ij / (n - 1))

    entropy = -entropy


    return round(entropy, 1)
