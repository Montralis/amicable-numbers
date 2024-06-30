import argparse

def calculateDivisors(limit):
    """
    Calculate the sum of proper divisors for each number up to the limit.
    """
    divisors_sum = [0] * (limit + 1)

    for i in range(1, limit // 2 + 1):
        for j in range(2 * i, limit + 1, i):
            divisors_sum[j] += i

    return divisors_sum

def findNumbers(limit: int, print_results: bool = True):
    """
    Find perfect and amicable numbers up to the given limit.
    """
    divisors_sum = calculateDivisors(limit)
    results = []

    for i in range(1, limit + 1):
        sum_i = divisors_sum[i]
        if sum_i < limit + 1:
            if i == sum_i:
                results.append(f"I am a Perfect number: {i}")
            elif sum_i != i and sum_i < limit + 1 and divisors_sum[sum_i] == i:
                results.append(f"I am a friendship number: {i} and {sum_i}")
                divisors_sum[sum_i] = 0  # Mark as processed

    if print_results:
        if results:
            for result in results:
                print(result)
        else:
            print("No perfect or amicable numbers found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find perfect and amicable numbers up to a given limit.")
    parser.add_argument("limit", type=int, nargs='?', default=1500, help="The upper limit for finding numbers (default: 1500)")
    args = parser.parse_args()

    findNumbers(args.limit)
