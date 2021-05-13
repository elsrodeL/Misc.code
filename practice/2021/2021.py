import sys

def get_min_op(st,K):
    goodness = 0
    for i in range(int(len(st)/2)):
        if st[i] != st[-i-1]:
            goodness+=1
    return abs(K - goodness)

if __name__ == "__main__":
    for i,line in enumerate(sys.stdin):
        print(i,line)
    