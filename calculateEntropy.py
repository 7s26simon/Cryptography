# Key entropy: how many bits are needed to represent N equally-likely keys.
import math


def key_entropy(num_keys):
    """Entropy in bits for num_keys equally-likely possibilities."""
    if num_keys < 1:
        raise ValueError("Number of keys must be at least 1.")
    return math.log2(num_keys)


def main():
    n = int(input("Enter number of equally-likely keys (integer): "))
    print("Key entropy =", key_entropy(n), "bits")


if __name__ == "__main__":
    main()
