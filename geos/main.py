
def put_into_dict(filename):
    d = {}
    f = open(filename)

    for x in f:
        l = x.split()
        # K:[V]
        bed = int(l[0].replace(':', ''))
        taxa = [i.replace(',', '') for i in l][1:]
        # Assign taxa and number
        for t in taxa:
            if t not in d.keys():
                d[t] = [bed]
            else:
                d[t] += [bed]
    return d


dn, ds = put_into_dict('northside.txt'),  put_into_dict('southside.txt')



# Lab 2 
# Q5
i,j = [2.05,0.75,0.0007,0.01], [144,5,0.000006,0.000001]
inputs , masses = [x*10**(8) for x in i], [y*10**(14) for y in j]
for index, m in enumerate(masses):
    rt = m/inputs[index]
    print(f'{rt} years')

# Q8
def d18O(sample,smow=1.9934*10**(-3)):
    return ((sample - smow)/smow)*1000

dmalay = d18O(1.1994397*10**(-3))
dchicago = d18O(1.1993466*10**(-3))
dgreenland = d18O(1.9933598 * 10**(-3))

def get_further_traveled(dmalay,dchicago):
    far = min([dmalay,dchicago])
    if far == dmalay:
        print('Malaysian Rainwater')
    else:
        print('Chicago Rainwater')

print(dmalay,dgreenland)



