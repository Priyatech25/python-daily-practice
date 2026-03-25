# DAY 29 - DSA Practice (Sparse Array)

def matching_strings(strings, queries):
    freq = {}

    # Count frequencies
    for s in strings:
        freq[s] = freq.get(s, 0) + 1

    # Answer queries
    result = []
    for q in queries:
        result.append(freq.get(q, 0))

    return result


# Testing
strings = ["aba", "baba", "aba", "xzxb"]
queries = ["aba", "xzxb", "ab"]

print("Result:", matching_strings(strings, queries))