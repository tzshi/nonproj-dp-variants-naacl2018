#!/usr/bin/env python
# encoding: utf-8

from nonproj.io import read_conll

import pyximport; pyximport.install()
from nonproj.att2_oracle import AttOracle
from collections import Counter
import os.path

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

global_counter = Counter()

print("Treebank-Code", "Total-trees", "Attardi-2-trees", "Variant-1-trees", "Variant-2-trees", "Variant-3-trees")

for treebank in TREEBANKS:
    filename = "/path/to/ud-treebanks-v2.1/{}-ud-train.conllu".format(treebank)
    if not os.path.isfile(filename):
        print(treebank, "not found")
        continue

    graphs = read_conll(filename)

    local_counter = Counter()

    for graph in graphs:
        local_counter["total"] += 1
        global_counter["total"] += 1

        oracle = AttOracle(graph.heads)

        if oracle.is_proj():
            local_counter["proj"] += 1
            global_counter["proj"] += 1

        if oracle.is_att2():
            local_counter["att2"] += 1
            global_counter["att2"] += 1

        if oracle.is_var1():
            local_counter["var1"] += 1
            global_counter["var1"] += 1

        if oracle.is_var2():
            local_counter["var2"] += 1
            global_counter["var2"] += 1

        if oracle.is_var3():
            local_counter["var3"] += 1
            global_counter["var3"] += 1

    print(treebank, local_counter["total"], local_counter["proj"], local_counter["att2"],
            local_counter["var1"], local_counter["var2"], local_counter["var3"])

print("ALL", global_counter["total"], global_counter["proj"], global_counter["att2"],
        global_counter["var1"], global_counter["var2"], global_counter["var3"])

non_proj = global_counter["total"] - global_counter["proj"]
print("Total number of non-projective trees:", non_proj)

att2 = global_counter["att2"] - global_counter["proj"]
print("Out of those,", att2, "({0:.2f}%)".format(att2 / non_proj * 100), "can be covered by Attardi-2")

var1 = global_counter["var1"] - global_counter["proj"]
print("Out of those,", var1, "({0:.2f}%)".format(var1 / non_proj * 100), "can be covered by Variant 1")

var2 = global_counter["var2"] - global_counter["proj"]
print("Out of those,", var2, "({0:.2f}%)".format(var2 / non_proj * 100), "can be covered by Variant 2")

var3 = global_counter["var3"] - global_counter["proj"]
print("Out of those,", var3, "({0:.2f}%)".format(var3 / non_proj * 100), "can be covered by Variant 3")
