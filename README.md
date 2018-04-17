# Requirements
- python 3.x
- Cython
- numpy

# Instructions
- change path to UD version 2.1 in `check_oracle.py` and `compute_coverage.py`
- run `python compute_coverage.py` to get the coverage statistics reported in the paper
- run `python check_oracle.py` if you would like to confirm that the dynamic programming gives the same result as the static oracle as used in `compute_coverage.py`

# Notes
- The dynamic programming models used in `check_oracle.py` implements the straightforward O(n^8) algorithms for clarity and simplicity. But one may apply the "hook trick" and arrive at O(n^7) implementation.
- For checking coverage, the static oracle implemented in `compute_coverage.py` has linear complexity and is more efficient than the DP algorithms. 

# Reference
If you make use of our code or data for research purposes, we'll appreciate citing the following:

```
@InProceedings{shi+gomez+lee2018,
    author    = {Tianze Shi and Carlos G{\'o}mez-Rodr{\'i}guez and Lillian Lee},
    title     = {Improving Coverage and Runtime Complexity for Exact Inference in Non-Projective Transition-Based Dependency Parsers},
    booktitle = {Proceedings of NAACL},
    month     = {June},
    year      = {2018},
    address   = {New Orleans, Louisiana},
    publisher = {Association for Computational Linguistics},
    pages     = {(To appear)}
}
```
