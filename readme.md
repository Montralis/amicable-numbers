# Perfect and Amicable Numbers Finder

This Python script finds perfect and amicable numbers up to a specified limit.

## How It Works

- `Perfect Numbers`: A number is perfect if the sum of its proper divisors (excluding itself) equals the number.
- `Amicable Numbers`: Two distinct numbers \(a\) and \(b\) are considered amicable if the sum of the proper divisors of \(a\) equals \(b\) and vice versa.

## Improvements

I tried various implementations and listed them named `main_genX.py` where `gen1` was the first implementation. 

### main_gen1.py
This was simple the first implementation where i tried to find a code solution for this problem. I did not care to much about performance.

Uses ``divisorGenerator(n)`` to generate divisors of a number n. It iterates up to the square root of n, appending divisors and their complements.

It computes the sum of proper divisors for each number from 1 to the given limit.
Uses a dictionary to store the sum of proper divisors. Iterates through the dictionary to find perfect and amicable numbers.Checks each number to see if it is a perfect number or part of an amicable pair.

### main_gen2.py
I was not happy with the result time so i tried to deeper understand the mathematics behind this problem. 

Sure, here’s the explanation in a continuous text format:

The efficiency of the algorithm lies in its approach to calculating the sum of divisors for each number up to a given limit. The function calculateDivisors(limit) uses a method that involves two nested loops to precompute these sums efficiently. The outer loop iterates with i ranging from 1 to half of the limit (limit // 2). For each i, the inner loop adds i to the sum of divisors for all its multiples starting from 2*i up to the limit. This way, every proper divisor is counted exactly once for each number, ensuring no redundant calculations.

This method works efficiently because the proper divisors of a number n are always less than n. Therefore, to compute the sum of proper divisors, we only need to consider divisors up to half the limit. For instance, if you consider a number n, its proper divisors will include numbers like 1, 2, 3, and so forth, up to n/2. Any larger number would be a multiple of the number itself, not a proper divisor.

By iterating only up to limit // 2, we ensure that each number and its divisors are processed in an optimal manner. This precomputation allows us to find perfect and amicable numbers more efficiently since we can directly access the precomputed sums and compare them without recalculating divisors repeatedly. As a result, the algorithm performs well even for larger limits, making it a preferred choice for identifying such numbers within a given range.

### main_gen3.py

Im inspried by the [this](https://www.youtube.com/watch?v=Zrv1EDIqHkY) video, so credits to [veritasium](https://www.youtube.com/@veritasium) for the great explanation. Coming soon ...

## Usage

### Requirements

- Python 3.x

### Running the Script

Save the script to a file (e.g., `main.py`) and execute it.

#### Default Limit (1500):

```sh
python3 main.py 2000
```

```sh
I am a Perfect number: 6, 6
I am a Perfect number: 28, 28
I am a friendship number: 220, 284
I am a Perfect number: 496, 496
I am a friendship number: 1184, 1210
```

# Graph Plotting

To plot a graph showing the time taken for different input limits, run the benchmark.py script. The plot will be saved as `plots/FROM-MAX-STEP.jpg`, where:

- `FROM` is the starting number.
- `max_n` is the maximum number analyzed.
- `step` is the step used in the analysis.


```sh
python3 benchmark.py 1000 2000 100
```
This will analyze numbers from 1000 to 2000 with a step of 100 and generate a corresponding plot.


Make sure to adjust the placeholders `FROM`, `max_n`, and `step` accordingly when explaining the command for plotting the graph. This README now includes information about the book that inspired the code, usage examples, and instructions for plotting graphs based on benchmark results.


<p>
<img src="plots/0-15000-100.jpg" alt="Image could not be loaded" width="500"/>
</p>



# Inspiration
The program code was developed based on the book "The Housekeeper and the Professor" by Yoko Ogawa, which served as an inspiration for exploring numerical properties discussed in the book.


Original Japanese Publication: The book was first published under the title "博士の愛した数式" ("Hakase no Aishita Sūgata") in 2003 in Japan. Written by: Yoko Ogawa and published by Shinchosha Publishing Co., Ltd.

English Publication: The English translation titled "The Housekeeper and the Professor" released in 2009. (English Edition): Stephen Snyder