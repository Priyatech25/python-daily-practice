# DAY 26 - DSA Practice (Dynamic Array)

def dynamic_array(n, queries):
    seq_list = [[] for _ in range(n)]
    last_answer = 0
    result = []

    for query in queries:
        t, x, y = query

        index = (x ^ last_answer) % n

        if t == 1:
            seq_list[index].append(y)

        elif t == 2:
            size = len(seq_list[index])
            value = seq_list[index][y % size]
            last_answer = value
            result.append(last_answer)

    return result


# Testing
n = 2
queries = [
    [1, 0, 5],
    [1, 1, 7],
    [1, 0, 3],
    [2, 1, 0],
    [2, 1, 1]
]

print("Output:", dynamic_array(n, queries))