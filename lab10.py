import numpy as np

def is_zero_free(numbers):

    numbers = np.array(numbers)

    if np.any(numbers == 0):
        return False
    else:
        return True

numbers = [0, 1, 2, 3, 4]
result = is_zero_free(numbers)
print(result)