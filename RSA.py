# Calculate RSA keys, then encrypt and decrypt a message.
# Educational only - real RSA uses primes hundreds of digits long.
from math import gcd


def egcd(a, b):
    """Extended Euclidean algorithm: returns (g, x, y) with a*x + b*y = g."""
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
    return old_r, old_x, old_y


def modinv(a, m):
    """Modular inverse of a mod m, or None if it does not exist."""
    g, x, _ = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    return x % m


def is_prime(n):
    """Trial-division primality test - fine for the small numbers used here."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def rsa(p, q, e, m):
    if not is_prime(p) or not is_prime(q):
        raise ValueError("P and Q must both be prime.")
    if p == q:
        raise ValueError("P and Q must be different primes.")

    n = p * q
    phi = (p - 1) * (q - 1)

    if m >= n:
        raise ValueError("Message M must be smaller than N = P*Q (%d)." % n)
    if gcd(e, phi) != 1:
        raise ValueError("E must be coprime to phi = %d." % phi)

    d = modinv(e, phi)
    if d is None:  # should not happen given the coprime check above
        raise ValueError("No modular inverse for E mod phi.")

    print("phi =", phi)
    print("public key  [N=%d, E=%d]" % (n, e))
    print("private key [N=%d, D=%d]" % (n, d))
    print("Message =", m)

    c = pow(m, e, n)
    print("encrypted message =", c)

    decrypted = pow(c, d, n)
    print("decrypted message =", decrypted)
    return c, decrypted


def main():
    p = int(input("Enter P (prime 1): "))
    q = int(input("Enter Q (prime 2): "))
    e = int(input("Enter E (public exponent): "))
    m = int(input("Enter M (message): "))
    rsa(p, q, e, m)


if __name__ == "__main__":
    main()
