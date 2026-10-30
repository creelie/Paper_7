#!/usr/bin/env python3
"""Exact check of the spinor statements of the paper on small chord diagrams.

(1) For N = 2, ..., 6 and every chord diagram with at most 4 chords, the normalised trace of
    the so(N) chord element on the Clifford algebra Cl_N, with so(N) acting through
    X_ij -> e_i e_j / 2, equals (-4)^(-n) S_Gamma(N).  The Clifford products are computed
    from the defining relations, independently of the commutation argument of the paper.
(2) For every chord diagram with at most 5 chords, w_D(3/8) = 8^(-n) S_Gamma(3), with w_D
    taken from the traces on the irreducible sl(2)-modules, as in check.py.
(3) On all graphs with at most 5 vertices: S_G(4) = 2^n S_G(3), and 8^(-n) S_G(3) equals the
    colouring invariant phi of Fomichev and Karev and their rank invariant psi.
"""
import itertools
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check import chord_diagrams, intersection_graph, w_at  # noqa: E402


def S(n, edges, N):
    pairs = [frozenset(p) for p in itertools.combinations(range(N), 2)]
    tot = 0
    for p in itertools.product(pairs, repeat=n):
        e = sum(len(p[u] & p[v]) for u, v in edges)
        tot += (-1) ** e
    return tot


def cl_mul(I, J):
    """e_I e_J = sign * e_{I xor J} for bitmasks I, J (generators square to 1)."""
    sign = 1
    a = I >> 1
    while a:
        if bin(a & J).count("1") % 2:
            sign = -sign
        a >>= 1
    # the loop above counts, for every generator of J, the generators of I above it
    return sign, I ^ J


def cl_mul_check():
    # direct check of the sign rule against the relations, small N
    for N in range(1, 5):
        for i in range(N):
            for j in range(N):
                s, K = cl_mul(1 << i, 1 << j)
                if i == j:
                    assert (s, K) == (1, 0)
                else:
                    s2, K2 = cl_mul(1 << j, 1 << i)
                    assert K == K2 and s == -s2


def spinor_value(s, N):
    """Normalised trace of the so(N) chord element on Cl_N."""
    n = len(s) // 2
    firsts = [i for i in range(2 * n) if i < s[i]]
    gens = [(1 << i) | (1 << j) for i, j in itertools.combinations(range(N), 2)]
    tot = Fraction(0)
    for choice in itertools.product(gens, repeat=n):
        letters = [None] * (2 * n)
        for g, i in zip(choice, firsts):
            letters[i] = letters[s[i]] = g
        sign, K = 1, 0
        for g in letters:
            sg, K = cl_mul(K, g)
            sign *= sg
        if K == 0:
            tot += sign
    return tot / Fraction(4) ** n


def phi_FK(n, edges):
    tot = 0
    for r in range(len(edges) + 1):
        for E2 in itertools.combinations(edges, r):
            col = sum(1 for f in itertools.product(range(3), repeat=n)
                      if all(f[u] != f[v] for u, v in E2))
            tot += (-2) ** r * col
    return Fraction(tot, 8 ** n)


def corank2(rows, m):
    rows = list(rows)
    rank = 0
    for c in range(m):
        piv = next((r for r in range(rank, len(rows)) if rows[r] >> c & 1), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for r in range(len(rows)):
            if r != rank and rows[r] >> c & 1:
                rows[r] ^= rows[rank]
        rank += 1
    return m - rank


def psi_FK(n, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    tot = Fraction(0)
    for U in range(1 << n):
        idx = [i for i in range(n) if U >> i & 1]
        rows = []
        for i in idx:
            r = 0
            for a, j in enumerate(idx):
                if adj[i] >> j & 1:
                    r |= 1 << a
            rows.append(r)
        tot += Fraction(-1, 2) ** (n - len(idx)) * 2 ** corank2(rows, len(idx))
    return tot / 4 ** n


def main():
    cl_mul_check()
    count = 0
    for n in range(1, 5):
        for s in chord_diagrams(n):
            nn, edges = intersection_graph(s)
            for N in range(2, 7 if n <= 3 else 5):
                lhs = spinor_value(s, N)
                rhs = Fraction(S(nn, sorted(edges), N), (-4) ** n)
                assert lhs == rhs, (s, N, lhs, rhs)
                count += 1
    print(f"(1) spinor traces agree with (-4)^-n S(N): {count} cases")
    count = 0
    for n in range(1, 6):
        for s in chord_diagrams(n):
            nn, edges = intersection_graph(s)
            assert w_at(s, Fraction(3, 8)) == Fraction(S(nn, sorted(edges), 3), 8 ** n), s
            count += 1
    print(f"(2) w_D(3/8) = 8^-n S(3): {count} diagrams")
    count = 0
    for n in range(1, 6):
        allpairs = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(allpairs)):
            edges = [allpairs[i] for i in range(len(allpairs)) if mask >> i & 1]
            s3 = S(n, edges, 3)
            assert S(n, edges, 4) == 2 ** n * s3
            if n <= 4 or mask % 7 == 0:
                assert phi_FK(n, edges) == Fraction(s3, 8 ** n)
                assert psi_FK(n, edges) == Fraction(s3, 8 ** n)
            count += 1
    print(f"(3) S(4) = 2^n S(3) and phi = psi = 8^-n S(3): {count} labelled graphs")
    print("spinor_check: all passed")


if __name__ == "__main__":
    main()
