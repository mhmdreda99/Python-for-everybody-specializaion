fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'clown.txt'
    hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

#print(di)

# new code starts from here
#x = sotred(di.items())
#print(x[:5])

#flip for sorting
tmp = list()
for k,v in di.items():
    print(k,v)
    newt = (v,k)
    tmp.append(newt)

#print('Flipped',tmp)

tmp = sorted(tmp, reverse=T)
#print('Sorted',tmp[:5])

#flip back to key
for v,k in tmp[:5]:
    print(k,v)
