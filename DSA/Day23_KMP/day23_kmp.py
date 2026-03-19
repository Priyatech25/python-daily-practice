# DAY 23 - DSA Practice (KMP String Matching)

# Step 1: Build LPS array
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


# Step 2: KMP Search
def kmp_search(text, pattern):
    lps = compute_lps(pattern)

    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            print("Pattern found at index:", i - j)
            j = lps[j - 1]

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


# Testing
text = "ababcabcabababd"
pattern = "ababd"

kmp_search(text, pattern)