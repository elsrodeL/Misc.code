def get_substrings(N, chars):
    rv = [0]*N
    poses = [ord(i) for i in chars]
    for i, c in enumerate(poses):
        if c > poses[i-1]:
            rv[i] = rv[i-1] + 1
        else:
            rv[i] = 1
    return rv

s = 'ZABCS'
n = len(s)


print(get_substrings(n,s))

'''

if __name__ == "__main__":
    t = int(input())
    for i in range(1, t+1):
        n = [i for i in input().split()]
        str_ = [i for i in input().split()]
        ans = get_substrings(int(n[0]), str_[0])
        print("Case #{}: {}".format(i, ans))
'''