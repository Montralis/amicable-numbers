import argparse
import time
import matplotlib.pyplot as plt
import os
from main_gen2 import findNumbers

def measure_time(limit):
    start_time = time.time()
    findNumbers(limit, print_results=False)
    end_time = time.time()
    return end_time - start_time

def plot_benchmark(start, max_n, step, output_dir="plots"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    x_values = range(start, max_n + 1, step)
    y_values = [measure_time(n) for n in x_values]

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Number')
    plt.ylabel('Time (seconds)')
    plt.title('Performance Benchmark')
    plt.grid(True)

    filename = f"{start}-{max_n}-{step}.jpg"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath)
    plt.close()
    print(f"Plot saved as {filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmark the performance of finding perfect and amicable numbers.")
    parser.add_argument("start", type=int, nargs='?', default=0,help="The starting number for the benchmark.")
    parser.add_argument("max_n", type=int, nargs='?', default=1500,help="The maximum number to benchmark.")
    parser.add_argument("step", type=int, nargs='?', default=100, help="The step size for the benchmark.")
    args = parser.parse_args()

    plot_benchmark(args.start, args.max_n, args.step)
