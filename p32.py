#!/usr/bin/python


import time

num_set = set(range(0, 10))
target_set = set()

def solve():
    for a in xrange(1, 9999):
        for b in xrange(1, 10**(5-len(str(a))+1)):
            ssa = str(a)
            ssb = str(b)
            lssa = len(ssa)
            lssb = len(ssb)
            sa = set(ssa)
            lsa = len(sa)
            if '0' in sa or lsa != lssa: continue
            sb = set(ssb)
            lsb = len(sb)
            if '0' in sb or lsb != lssb: continue
            if not sa.isdisjoint(sb): continue
            prod = a * b
            ssp = str(prod)
            lssp = len(ssp)
            sp = set(ssp)
            lsp = len(sp)
            if lsp != lssp or '0' in sp: continue
            if not sp.isdisjoint(sa) or not sp.isdisjoint(sb): continue
            if lsp + lsa + lsb != 9: continue
            if prod not in target_set: target_set.add(prod)
            print a, b, prod
    print sum(target_set)

def main():
    solve()


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
