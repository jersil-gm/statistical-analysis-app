import numpy as np
from collections import Counter

def calculate_stats(user_input):
    try:
        data = user_input.strip().split()
        float_data = []

        for val in data:
            try:
                float_data.append(float(val))
            except ValueError:
                raise ValueError(f"'{val}' is not a valid number.")

        arr = np.array(float_data)

        mean = np.mean(arr)
        median = np.median(arr)
        variance = np.var(arr)
        std_dev = np.std(arr)

        count = Counter(arr)
        max_freq = max(count.values())
        mode = sorted([float(k) for k, v in count.items() if v == max_freq])

        return mean, median, mode, variance, std_dev

    except ValueError as e:
        return f"Error: {e}"
