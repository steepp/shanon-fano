#!/usr/bin/python3
import math
from binarytree import Node


def calculate_entropy(args=[]):
    entropy = 0
    for p, l in zip(args, map(lambda i: math.log(i, 2), args)):
        entropy += p*l
    return -entropy


def getInputFromFile(fl):
    with open(fl) as f:
        return [float(l.strip()) for l in f if l.strip()]


def fano(args):
    probs = args.copy()
    # probs.sort()
    m = 0
    r = len(probs) - 1
    l_sum = 0
    r_sum = probs[r]
    for i, e in enumerate(probs):
        if i >= r:       # middle part, all elements are summed up
            m = r
            break
        l_sum += e
        if l_sum > r_sum and r - i > 1:
            r -= 1
            r_sum += probs[r]
    return m


def build_tree(seq):
    if not seq:
        return
    if len(seq) == 1:
        return Node(seq[0])
    seq.sort()
    parent = Node(sum(seq))
    i = fano(seq)
    l = seq[:i]
    r = seq[i:]
    parent.left = build_tree(l)
    parent.right = build_tree(r)
    return parent


if __name__ == '__main__':
    import sys
    if(len(sys.argv) > 1):
        vals = getInputFromFile(sys.argv.pop())
        print('Input: \n', vals)
        entropy = calculate_entropy(vals)
        print('Entropy: \n', entropy)
        print('Fano tree:', build_tree(vals))
    else:
        print('No file is specified.\n\tfano.py FILE_NAME')
