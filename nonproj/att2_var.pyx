#!/usr/bin/env python
# encoding: utf-8

cimport cython

import numpy as np
cimport numpy as np
np.import_array()

from cpython cimport bool

cdef np.float64_t NEGINF = -np.inf
cdef np.float64_t INF = np.inf
cdef inline int int_max(int a, int b): return a if a >= b else b
cdef inline int int_min(int a, int b): return a if a <= b else b
cdef inline np.float64_t float64_max(np.float64_t a, np.float64_t b): return a if a >= b else b
cdef inline np.float64_t float64_min(np.float64_t a, np.float64_t b): return a if a <= b else b


@cython.boundscheck(False)
@cython.wraparound(False)
def att_score(np.ndarray[ndim=2, dtype=np.float64_t] mst_scores):
    cdef int nr, nc, N, h1, i, h2, h3, h4, h5, k, j, r17, r16, r15, r14, r13, r12, r1, r2, r3, r4, r5, r6, r7
    cdef np.float64_t tmp, cand

    cdef np.ndarray[ndim=5, dtype=np.float64_t] table5
    cdef np.ndarray[ndim=2, dtype=np.float64_t] guarded_mst_scores

    nr, nc = np.shape(mst_scores)

    N = nr + 2

    table5 = np.full((N, nr, N, nr, N), NEGINF, dtype=np.float)

    for h3 in range(0, N - 2):
        for j in range(h3 + 1, N - 1):
            table5[h3, j, h3, j, j + 1] = 0

    guarded_mst_scores = np.full((N, N), NEGINF, dtype=np.float)
    for i in range(0, nr):
        for j in range(0, nc):
            guarded_mst_scores[i + 1, j + 1] = mst_scores[i, j]


    for r17 in range(3, N):
        for r16 in range(2, r17):
            for r15 in range(1, r16):
                for r14 in range(2, r16 + 1):
                    for r13 in range(1, r14):
                        for r12 in range(0, r13):
                            for r1 in range(1, r13 + 1):
                                for h1 in range(0, N - r17):
                                    i = h1 + r1
                                    h2 = h1 + r12
                                    h3 = h1 + r13
                                    k = h1 + r14
                                    h4 = h1 + r15
                                    h5 = h1 + r16
                                    j = h1 + r17

                                    tmp = table5[h1, i, h2, h3, k] + table5[h3, k, h4, h5, j]
                                    cand = tmp + float64_max(guarded_mst_scores[h4, h5], guarded_mst_scores[h2, h5])
                                    if cand > table5[h1, i, h2, h4, j]:
                                        table5[h1, i, h2, h4, j] = cand

                                    cand = tmp + guarded_mst_scores[h5, h4]
                                    if cand > table5[h1, i, h2, h5, j]:
                                        table5[h1, i, h2, h5, j] = cand

                                    cand = tmp + guarded_mst_scores[h5, h2]
                                    if cand > table5[h1, i, h4, h5, j]:
                                        table5[h1, i, h4, h5, j] = cand
    return table5[0, 1, 0, 1, N - 1]


@cython.boundscheck(False)
@cython.wraparound(False)
def var_1_score(np.ndarray[ndim=2, dtype=np.float64_t] mst_scores):
    cdef int nr, nc, N, h1, i, h2, h3, h4, h5, k, j, r17, r16, r15, r14, r13, r12, r1, r2, r3, r4, r5, r6, r7
    cdef np.float64_t tmp, cand

    cdef np.ndarray[ndim=5, dtype=np.float64_t] table5
    cdef np.ndarray[ndim=2, dtype=np.float64_t] guarded_mst_scores

    nr, nc = np.shape(mst_scores)

    N = nr + 2

    table5 = np.full((N, nr, N, nr, N), NEGINF, dtype=np.float)

    for h3 in range(0, N - 2):
        for j in range(h3 + 1, N - 1):
            table5[h3, j, h3, j, j + 1] = 0

    guarded_mst_scores = np.full((N, N), NEGINF, dtype=np.float)
    for i in range(0, nr):
        for j in range(0, nc):
            guarded_mst_scores[i + 1, j + 1] = mst_scores[i, j]


    for r17 in range(3, N):
        for r16 in range(2, r17):
            for r15 in range(1, r16):
                for r14 in range(2, r16 + 1):
                    for r13 in range(1, r14):
                        for r12 in range(0, r13):
                            for r1 in range(1, r13 + 1):
                                for h1 in range(0, N - r17):
                                    i = h1 + r1
                                    h2 = h1 + r12
                                    h3 = h1 + r13
                                    k = h1 + r14
                                    h4 = h1 + r15
                                    h5 = h1 + r16
                                    j = h1 + r17

                                    tmp = table5[h1, i, h2, h3, k] + table5[h3, k, h4, h5, j]
                                    cand = tmp + float64_max(guarded_mst_scores[h4, h5], float64_max(guarded_mst_scores[h2, h5], guarded_mst_scores[j, h5]))
                                    if cand > table5[h1, i, h2, h4, j]:
                                        table5[h1, i, h2, h4, j] = cand

                                    cand = tmp + float64_max(guarded_mst_scores[h5, h4], guarded_mst_scores[h2, h4])
                                    if cand > table5[h1, i, h2, h5, j]:
                                        table5[h1, i, h2, h5, j] = cand

                                    cand = tmp + float64_max(guarded_mst_scores[h5, h2], guarded_mst_scores[h4, h2])
                                    if cand > table5[h1, i, h4, h5, j]:
                                        table5[h1, i, h4, h5, j] = cand
    return table5[0, 1, 0, 1, N - 1]


@cython.boundscheck(False)
@cython.wraparound(False)
def var_2_score(np.ndarray[ndim=2, dtype=np.float64_t] mst_scores):
    cdef int nr, nc, N, h1, i, h2, h3, h4, h5, k, j, r17, r16, r15, r14, r13, r12, r1, r2, r3, r4, r5, r6, r7
    cdef np.float64_t tmp, cand

    cdef np.ndarray[ndim=5, dtype=np.float64_t] table5
    cdef np.ndarray[ndim=2, dtype=np.float64_t] guarded_mst_scores

    nr, nc = np.shape(mst_scores)

    N = nr + 2

    table5 = np.full((N, nr, N, nr, N), NEGINF, dtype=np.float)

    for h3 in range(0, N - 2):
        for j in range(h3 + 1, N - 1):
            table5[h3, j, h3, j, j + 1] = 0

    guarded_mst_scores = np.full((N, N), NEGINF, dtype=np.float)
    for i in range(0, nr):
        for j in range(0, nc):
            guarded_mst_scores[i + 1, j + 1] = mst_scores[i, j]


    for r17 in range(3, N):
        for r16 in range(2, r17):
            for r15 in range(1, r16):
                for r14 in range(2, r16 + 1):
                    for r13 in range(1, r14):
                        for r12 in range(0, r13):
                            for r1 in range(1, r13 + 1):
                                for h1 in range(0, N - r17):
                                    i = h1 + r1
                                    h2 = h1 + r12
                                    h3 = h1 + r13
                                    k = h1 + r14
                                    h4 = h1 + r15
                                    h5 = h1 + r16
                                    j = h1 + r17

                                    tmp = table5[h1, i, h2, h3, k] + table5[h3, k, h4, h5, j]
                                    cand = tmp + float64_max(guarded_mst_scores[h4, h5], float64_max(guarded_mst_scores[h2, h5], guarded_mst_scores[j, h5]))
                                    if cand > table5[h1, i, h2, h4, j]:
                                        table5[h1, i, h2, h4, j] = cand

                                    cand = tmp + float64_max(guarded_mst_scores[h5, h4], float64_max(guarded_mst_scores[h2, h4], guarded_mst_scores[j, h4]))
                                    if cand > table5[h1, i, h2, h5, j]:
                                        table5[h1, i, h2, h5, j] = cand

                                    cand = tmp + float64_max(guarded_mst_scores[h5, h2], float64_max(guarded_mst_scores[h4, h2], guarded_mst_scores[j, h2]))
                                    if cand > table5[h1, i, h4, h5, j]:
                                        table5[h1, i, h4, h5, j] = cand
    return table5[0, 1, 0, 1, N - 1]


@cython.boundscheck(False)
@cython.wraparound(False)
def var_3_score(np.ndarray[ndim=2, dtype=np.float64_t] mst_scores):
    cdef int nr, nc, N, h1, i, h2, h3, h4, h5, k, j, r17, r16, r15, r14, r13, r12, r1, r2, r3, r4, r5, r6, r7
    cdef np.float64_t tmp, cand

    cdef np.ndarray[ndim=5, dtype=np.float64_t] table5
    cdef np.ndarray[ndim=2, dtype=np.float64_t] guarded_mst_scores

    nr, nc = np.shape(mst_scores)

    N = nr + 2

    table5 = np.full((N, nr, N, nr, N), NEGINF, dtype=np.float)

    for h3 in range(0, N - 2):
        for j in range(h3 + 1, N - 1):
            table5[h3, j, h3, j, j + 1] = 0

    guarded_mst_scores = np.full((N, N), NEGINF, dtype=np.float)
    for i in range(0, nr):
        for j in range(0, nc):
            guarded_mst_scores[i + 1, j + 1] = mst_scores[i, j]


    for r17 in range(3, N):
        for r16 in range(2, r17):
            for r15 in range(1, r16):
                for r14 in range(2, r16 + 1):
                    for r13 in range(1, r14):
                        for r12 in range(0, r13):
                            for r1 in range(1, r13 + 1):
                                for h1 in range(0, N - r17):
                                    i = h1 + r1
                                    h2 = h1 + r12
                                    h3 = h1 + r13
                                    k = h1 + r14
                                    h4 = h1 + r15
                                    h5 = h1 + r16
                                    j = h1 + r17

                                    tmp = table5[h1, i, h2, h3, k] + table5[h3, k, h4, h5, j]
                                    cand = tmp + float64_max(guarded_mst_scores[h4, h5], float64_max(guarded_mst_scores[h2, h5], guarded_mst_scores[j, h5]))
                                    if cand > table5[h1, i, h2, h4, j]:
                                        table5[h1, i, h2, h4, j] = cand

                                    cand = tmp + float64_max(guarded_mst_scores[h5, h4], float64_max(guarded_mst_scores[h2, h4], guarded_mst_scores[j, h4]))
                                    if cand > table5[h1, i, h2, h5, j]:
                                        table5[h1, i, h2, h5, j] = cand

    return table5[0, 1, 0, 1, N - 1]
