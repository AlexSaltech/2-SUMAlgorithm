def load_file():
    with open('/home/alejandro/Documents/Stanford Algorithms 1/Week 6/test1.txt') as f:  # prob-2sum.txt
        hs = {}
        for line in f:
            if line:
                num = int(line)
                try:
                    hs[num] += 1
                except:
                    hs[num] = 1
    return hs


def two_sum(hs):
    rng = 10
    counter = 0
    for t in range(-rng, rng + 1, 1):
        for x in sorted(hs):
            lookup = t - x
            if x == lookup:
                n = hs[x]
                if n > 1:
                    counter += n - 1
            elif lookup >= x:
                n = hs[x]
                if lookup in hs:
                    counter += n * hs[lookup]
    return counter


hs = load_file()
sm = two_sum(hs)
print hs
print sm
