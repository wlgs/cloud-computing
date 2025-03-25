import ray
import random
from fractions import Fraction

ray.init(address='auto')

@ray.remote
def pi4_sample(sample_count):
    """pi4_sample runs sample_count experiments, and returns the 
    fraction of time it was inside the circle. 
    """
    in_count = 0
    for i in range(sample_count):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            in_count += 1
    return Fraction(in_count, sample_count)


# Run the experiments

# Number of experiments to run
num_samples = 10000000
num_experiments = 10000

# Run the experiments
results = ray.get([pi4_sample.remote(num_samples) for _ in range(num_experiments)])

# Calculate the average
avg = sum(results for results in results) / num_experiments * 4
avg_float = float(avg)
print(f"Pi is approximately {avg_float:.5f}")
