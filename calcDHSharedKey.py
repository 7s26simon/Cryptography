# Diffie-Hellman - derive the shared secret key.
# Both parties end up with the same key without ever sending it directly.


def calc_shared_key(g, n, x, y):
    """
    g, n : public base and prime modulus, agreed in the open.
    x, y : Alice's and Bob's private exponents.
    """
    # Public values each party sends to the other.
    a = pow(g, x, n)          # Alice -> Bob
    b = pow(g, y, n)          # Bob   -> Alice

    # Each side raises the value it received by its own private exponent.
    key_from_alice = pow(b, x, n)   # Alice computes B^x mod n
    key_from_bob = pow(a, y, n)     # Bob   computes A^y mod n

    print()
    print("A = g^x mod n = %d^%d mod %d = %d" % (g, x, n, a))
    print("B = g^y mod n = %d^%d mod %d = %d" % (g, y, n, b))
    print("Alice's key = B^x mod n = %d^%d mod %d = %d" % (b, x, n, key_from_alice))
    print("Bob's   key = A^y mod n = %d^%d mod %d = %d" % (a, y, n, key_from_bob))

    if key_from_alice == key_from_bob:
        print("Shared key agreed:", key_from_alice)
    else:  # only happens with invalid (e.g. non-prime) inputs
        print("Keys do NOT match - check that N is prime.")
    print()
    return key_from_alice


def main():
    g = int(input("Enter G (public base): "))
    n = int(input("Enter N (prime modulus): "))
    x = int(input("Enter X (Alice's private exponent): "))
    y = int(input("Enter Y (Bob's private exponent): "))
    calc_shared_key(g, n, x, y)


if __name__ == "__main__":
    main()
