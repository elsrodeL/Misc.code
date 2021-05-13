a = [3,4,5,6,8,9]

def closestNumbers(numbers):
    # sort the array
    a = numbers.sort()
    # loop over array and find absolute minimum
    min_diff = 10000000
    for i, j in enumerate(a):
        if abs(j - a[i+1]) < min_diff:
            min_diff = abs(j-a[i+1])
        # smallest diff between ints
        if abs(j - a[i+1]) == 1:
            min_diff = 1
            break
    # find all pairs corresponding to a diff of min_diff
    pairs = []
    for i, j in enumerate(a):
        for _, b in enumerate(a):
            if j != b and abs(j - b) == min_diff:
                pair = j, b
                pairs.append(pair)
    # sort pairs by ascending order
    pairs = list(map(lambda x: swap_vals(x), pairs))
    for p in pairs:
        print(p)

print(closestNumbers(a))