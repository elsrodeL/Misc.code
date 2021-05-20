#%% 

def every_other(chars):
    rv = list(filter(lambda c: chars.index(c) % 2 == 0, chars))
    return ''.join(rv)

tests = ['1a2n4n5n2n','n1m4j7j1u8']
for t in tests:
    print(every_other(t))