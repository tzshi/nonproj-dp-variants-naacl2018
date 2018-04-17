#!/usr/bin/env python
# encoding: utf-8

from nonproj.io import read_conll

import pyximport; pyximport.install()
from nonproj.mst import parse_proj
from nonproj.att2_var import att_score, var_1_score, var_2_score, var_3_score
from nonproj.att2_oracle import AttOracle
import os.path
import numpy as np

TREEBANKS ="""af
ar_nyuad
ar
be
bg
ca
cop
cs_cac
cs_cltt
cs_fictree
cs
cu
da
de
el
en_lines
en_partut
en
es_ancora
es
et
eu
fa
fi_ftb
fi
fr_ftb
fr_partut
fr_sequoia
fr
ga
gl_treegal
gl
got
grc_proiel
grc
he
hi
hr
hu
id
it_partut
it_postwita
it
ja
kk
ko
la_ittb
la_proiel
la
lt
lv
mr
nl_lassysmall
nl
no_bokmaal
no_nynorsk
pl
pt_br
pt
ro_nonstandard
ro
ru_syntagrus
ru
sk
sl_sst
sl
sme
sr
sv_lines
sv
swl
ta
te
tr
uk
ur
vi
zh""".split()

for treebank in TREEBANKS:
    print("Checking", treebank)
    filename = "/path/to/ud-treebanks-v2.1/{}-ud-train.conllu".format(treebank)
    if not os.path.isfile(filename):
        print("not found")
        continue

    graphs = read_conll(filename)

    for graph in graphs:
        if len(graph.nodes) > 15:
            continue

        oracle = AttOracle(graph.heads)

        is_proj = oracle.is_proj()
        is_att2 = oracle.is_att2()
        is_var1 = oracle.is_var1()
        is_var2 = oracle.is_var2()
        is_var3 = oracle.is_var3()

        scores = np.zeros((len(graph.nodes), len(graph.nodes)))
        for d, h in enumerate(graph.heads):
            scores[h, d] += 1.
        proj_heads = parse_proj(scores)

        is_proj_dp = (sum(proj_heads == graph.heads) == len(graph.nodes))
        is_att2_dp = (att_score(scores) == len(graph.nodes) - 1)
        is_var1_dp = (var_1_score(scores) == len(graph.nodes) - 1)
        is_var2_dp = (var_2_score(scores) == len(graph.nodes) - 1)
        is_var3_dp = (var_3_score(scores) == len(graph.nodes) - 1)

        assert(is_proj_dp == is_proj)
        assert(is_att2_dp == is_att2)
        assert(is_var1_dp == is_var1)
        assert(is_var2_dp == is_var2)
        assert(is_var3_dp == is_var3)
    print("passed")
