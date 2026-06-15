# Secure vote tally using additive secret sharing.
#
# Each voter splits their vote into 3 random shares that sum to the vote
# (modulo MODULUS). Individually a share reveals nothing; when the matching
# shares from every voter are added up, the totals recombine to the true
# sum of votes. No share ever exposes how anyone voted.
from random import randrange

MODULUS = 100
NUM_SHARES = 3


def split_vote(vote, modulus=MODULUS, num_shares=NUM_SHARES):
    """Split a vote into num_shares random shares that sum to vote (mod modulus)."""
    shares = [randrange(modulus) for _ in range(num_shares - 1)]
    shares.append((vote - sum(shares)) % modulus)
    return shares


def tally(votes, modulus=MODULUS, num_shares=NUM_SHARES):
    """Return per-voter shares and the recombined sum of votes."""
    all_shares = {name: split_vote(v, modulus, num_shares) for name, v in votes.items()}

    # Each "tallier" j adds up the j-th share from every voter.
    column_totals = [
        sum(shares[j] for shares in all_shares.values()) % modulus
        for j in range(num_shares)
    ]
    derived_sum = sum(column_totals) % modulus
    return all_shares, column_totals, derived_sum


def main():
    votes = {"Bob": 5, "Alice": 1, "Carol": 1}
    expected = sum(votes.values()) % MODULUS

    all_shares, column_totals, derived_sum = tally(votes)

    print("Original votes:")
    for name, v in votes.items():
        print("  %s's vote: %d" % (name, v))

    print("\nEach vote split into %d random shares (sum mod %d = the vote):" % (NUM_SHARES, MODULUS))
    for name, shares in all_shares.items():
        print("  %-6s shares: %s  (sum mod %d = %d)"
              % (name, shares, MODULUS, sum(shares) % MODULUS))

    print("\nPer-tallier column totals:", column_totals)
    print("Sum of original votes:    ", expected)
    print("Derived vote (recombined):", derived_sum)
    assert derived_sum == expected, "tally does not match - sharing is broken"
    print("Votes successfully derived.")


if __name__ == "__main__":
    main()
