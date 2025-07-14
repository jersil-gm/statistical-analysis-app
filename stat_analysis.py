import numpy as np
from collections import Counter
def get_input():
    value=input("Enter a list of numbers separated by spaces: ")
    try:
        number=list(map(float,value.strip().split()))
        return np.array(number)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return get_input()
def calculate_statistics(data):
    if len(data) == 0:
        return None, None, None, None, None
    
    mean = np.mean(data)
    median = np.median(data)
    mode_data = Counter(data)
    max_freq=max(mode_data.values())
    mode = sorted([float(k) for k, v in mode_data.items() if v == max_freq])
    variance = np.var(data)
    std_dev = np.std(data)
    
    return mean, median, mode, variance, std_dev
def display_statistics(mean, median, mode, variance, std_dev):
    print("Statistics:")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
def main():
    print(" Welcome to Statistical Analyser")
    data = get_input()
    mean, median, mode, variance, std_dev = calculate_statistics(data)
    display_statistics(mean, median, mode, variance, std_dev)

if __name__ == "__main__":
    main()