#!/usr/bin/python3
import math
import functools


def calculate_entropy(args=[]):
    entropy = 0
    for p, l in zip(args, map(lambda i: math.log(i, 2), args)):
        entropy += p*l
    return -entropy


def transform(arg):
    return float(arg.strip())


def getInputFromFile(fl):
    res = []
    with open(fl) as f:
        for l in f:
            res.append(transform(l))
    return res


def fano(args):
    '''
    Another way is to start from the beggining of the reversed list (from biggest value) and compare lesser items
    '''
    probs = args.copy()
    # res.sort(reverse=True)
    probs.sort()
    # print(probs)
    m = 0
    r = len(probs) - 1
    l_sum = 0
    r_sum = probs[r]
    for i, e in enumerate(probs):
        l_sum += e
        if (l_sum >= r_sum):
            if(r - i == 1):       # middle part, all elements are summed up
                m = r
                break
            r -= 1
            r_sum += probs[r]

    return [(probs[:m], l_sum), (probs[m:], r_sum)]


if __name__ == '__main__':
    import sys
    # vals = sys.argv.pop() if len(sys.argv) > 1 else ''
    if(len(sys.argv) > 1):
        vals = getInputFromFile(sys.argv.pop())
        print('Input: \n', vals)
        entropy = calculate_entropy(vals)
        print('Entropy: \n', entropy)
        fano_coding = fano(vals)
        print('fano: \n', fano_coding)
    else:
        print('No file is specified.\n\tfano.py FILE_NAME')
