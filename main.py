import math
import argparse

def divisorGenerator(n):
    """
    Generate all divisors of a given number n.
    """
    large_divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor

def findNumbers(limit: int, print_results: bool = True):
    """
    Find perfect and amicable (friendship) numbers up to the given limit.
    """
    numberDict = {}

    # Populate the dictionary with the sum of proper divisors for each number
    for i in range(1, limit + 1):
        divisors = list(divisorGenerator(i))
        if i in divisors:
            divisors.remove(i)  # Remove the number itself to get the sum of proper divisors
        numberDict[str(i)] = sum(divisors)

    # Create a list of items to avoid modifying the dictionary while iterating
    items = list(numberDict.items())

    results = []

    for key, value in items:
        key_str = str(key)
        value_str = str(value)

        if value_str in numberDict:
            if key_str == value_str:
                results.append(f"I am a Perfect number: {key_str}, {value}")
            elif str(numberDict[value_str]) == key_str:
                results.append(f"I am a friendship number: {key_str}, {value}")
                # Remove the pair from the dictionary to prevent double checking
                numberDict.pop(value_str, None)
                numberDict.pop(key_str, None)
    
    if print_results:
        for result in results:
            print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find perfect and amicable numbers up to a given limit.")
    parser.add_argument("limit", type=int, nargs='?', default=1500, help="The upper limit for finding numbers (default: 1500)")
    args = parser.parse_args()

    findNumbers(args.limit)
