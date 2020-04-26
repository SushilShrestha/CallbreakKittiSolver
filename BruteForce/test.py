def find_block(a):
    ones_counts = []
    zeros_counts = []

    ones = 0
    zeros = 0
    for i in a:
        if i == 1:
            ones += 1
        else:
            zeros += 1
        ones_counts.append(ones)
        zeros_counts.append(zeros)

    if abs(ones - zeros) >= 2:
        for i in range(len(ones_counts))[::-1]:
            if abs(ones_counts[i] - zeros_counts[i]) < 2:
                return min(ones_counts[i], zeros_counts[i]) * 2
    return min(ones, zeros) * 2

print(find_block([0,0,1,0,0,0,1,1]))
