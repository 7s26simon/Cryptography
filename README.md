Cryptography Scripts

A small collection of educational Python 3 scripts demonstrating core cryptography concepts: RSA, Diffie–Hellman key exchange, key entropy, and a secure vote tally using additive secret sharing.

⚠️ Educational use only. These scripts use tiny numbers and simple algorithms (e.g. trial-division primality testing) to make the maths easy to follow. They are not secure and must never be used to protect real data.

Requirements
Python 3 (no third-party packages required)
Scripts
RSA.py
Generates an RSA key pair from two primes, then encrypts and decrypts a message.

python3 RSA.py
It prompts for:

P, Q — two distinct prime numbers
E — the public exponent (must be coprime to φ = (P−1)(Q−1))
M — the message as an integer (must be smaller than N = P·Q)
Example (P=5, Q=11, E=7, M=9):

phi = 40
public key  [N=55, E=7]
private key [N=55, D=23]
Message = 9
encrypted message = 4
decrypted message = 9
Inputs are validated: P and Q must be prime and distinct, E must be coprime to φ, and M must be smaller than N.

calcDHSharedKey.py
Demonstrates a Diffie–Hellman key exchange, computing the shared secret from both parties' perspectives to show they arrive at the same key.

python3 calcDHSharedKey.py
It prompts for:

G — the public base
N — a prime modulus
X — Alice's private exponent
Y — Bob's private exponent
Example (G=5, N=23, X=6, Y=15):

A = g^x mod n = 5^6 mod 23 = 8
B = g^y mod n = 5^15 mod 23 = 19
Alice's key = B^x mod n = 19^6 mod 23 = 2
Bob's   key = A^y mod n = 8^15 mod 23 = 2
Shared key agreed: 2
calculateEntropy.py
Calculates the key entropy (in bits) for a given number of equally-likely keys.

python3 calculateEntropy.py
It prompts for the number of equally-likely keys.

Example (256 keys):

Key entropy = 8.0 bits
sfe.py
A secure vote tally using additive secret sharing. Each voter splits their vote into several random shares that sum (mod 100) to their vote. Individually a share reveals nothing, but when the matching shares from every voter are summed, the totals recombine to the true sum of votes — without exposing how anyone voted.

python3 sfe.py
Takes no input; the votes (Bob=5, Alice=1, Carol=1) are defined in main().

Example output (share values are random each run):

Original votes:
  Bob's vote: 5
  Alice's vote: 1
  Carol's vote: 1
Each vote split into 3 random shares (sum mod 100 = the vote):
  Bob    shares: [68, 64, 73]  (sum mod 100 = 5)
  Alice  shares: [66, 74, 61]  (sum mod 100 = 1)
  Carol  shares: [84, 46, 71]  (sum mod 100 = 1)
Per-tallier column totals: [18, 84, 5]
Sum of original votes:     7
Derived vote (recombined): 7
Votes successfully derived.
Notes
Each script wraps its logic in functions behind an if __name__ == "__main__": guard, so they can be imported and reused (or unit tested) as well as run directly.
