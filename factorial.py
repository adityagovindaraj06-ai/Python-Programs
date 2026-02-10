
import argparse

def factorial(n: int) -> int:
        """Return n! for non-negative integer n."""
        n = int(n)
        if n < 0:
                raise ValueError("factorial() not defined for negative values")
        result = 1
        for i in range(2, n + 1):
                result *= i
        return result

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Compute factorial of a non-negative integer.")
        parser.add_argument("n", type=int, help="non-negative integer")
        args = parser.parse_args()
        print(factorial(args.n))