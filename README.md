# The sl(2) weight system at c = -3/32 extends to a graph 4-invariant

Deep Bhattacharjee and Ushashi Bhattacharya. Revision of 30 October 2026 (release v1.1.0).

The paper proves the conjecture of Fomichev, Karev, Pavutnitskiy and Usanov
(arXiv:2607.24217, Section 4): the specialisation of the sl(2) weight system
at c = -3/32 extends to a 4-invariant of graphs, namely
xi(G) = (-32)^{-n} S_G(-2), where S_G(N) counts with signs the maps that send
the n vertices of G to 2-element subsets of {1, ..., N}. Every step is proved
by hand in the paper; the programs here only check its identities on small
cases, and no statement of the paper rests on them.

This revision adds Section 7: for every N, the element of a chord diagram built
from so(N) acts on the spin representation by (-4)^{-n} S_G(N). At N = 3 this
gives w_D(3/8) = 8^{-n} S_G(3), which is the colouring invariant phi of Fomichev
and Karev, so phi is a 4-invariant extending the sl(2) weight system at
c = 3/8 (proved before by Yan, Deng and Jin through a second invariant). With
the Killing form the spin weight system is (8(N-2))^{-n} S_G(N), and the main
theorem is this expression at N = -2.

An earlier and incomplete version appeared on Hexagon as
[hexagon:2610.00320](https://hexagonmath.org/2610.00320); release v1.0.1 of this
repository was posted there as
[hexagon:2610.00320v2](https://hexagonmath.org/2610.00320v2). The earlier
versions are archived on Zenodo under the concept DOI
[10.5281/zenodo.23312529](https://doi.org/10.5281/zenodo.23312529).

## Layout

- `paper/main.tex`, `paper/figures/`: the LaTeX source and the three figures; `paper/main.pdf` the compiled paper (13 pages, amsart, single column).
- `dist/`: the paper as `Sl2WeightSystemAtMinus3Over32_final2.pdf`, its source zip and the arXiv tarball.
- `checks/python/check.py`: exact rational check of the theorem on all chord diagrams with at most 5 chords and of the four-term relation on small graphs.
- `checks/python/proof_steps.py`: exact check of each identity of Sections 3 to 5 on small cases.
- `checks/python/spinor_check.py`: exact check of Theorem 7.1 (Clifford products computed from the defining relations, N = 2 to 6, up to 4 chords), Corollary 7.2 (up to 5 chords) and S_G(4) = 2^n S_G(3), phi = psi = 8^{-n} S_G(3) on all graphs with at most 5 vertices.
- `checks/julia/check.jl`, `checks/c/check.c`, `checks/cpp/check.cpp`: the same checks in modular arithmetic, with larger cases.
- `checks/data/fkpu_table_sample.txt`: values of the extension on 9- and 10-vertex graphs from the data of Fomichev, Karev, Pavutnitskiy and Usanov, reproduced by `check.jl`.
- `run_all.sh`: runs all four checks.

## Running the checks

    ./run_all.sh

Requirements: python3, julia, a C compiler and a C++17 compiler.

## Releases

Releases are published by the workflow `release.yml` from the Actions tab.
Each release carries the paper files of `dist/`. The concept DOI of all releases is [10.5281/zenodo.23658071](https://doi.org/10.5281/zenodo.23658071).

| Release | DOI |
| --- | --- |
| v1.0.0 | superseded by v1.0.1 (authors listed incompletely) |
| v1.0.1 | [10.5281/zenodo.23658136](https://doi.org/10.5281/zenodo.23658136) |
| v1.0.2 | assigned on publication |
| v1.1.0 (this revision) | [10.5281/zenodo.23791376](https://doi.org/10.5281/zenodo.23791376) |

## Authors

Deep Bhattacharjee, Formerly, Electro-Gravitational Space Propulsion Laboratory (EGSPL), Bhubaneswar, Odisha 751030, India; Formerly, University of Calcutta (Heramba Chandra College), 23/49 Gariahat Road, Golpark, Kolkata 700029, West Bengal, India.
Emails: d.bhattacharjee@erl-forschung.de, itsdeep@live.com, egspl@proton.me (GitHub-related contact; GitHub [creelie](https://github.com/creelie)).
ORCID: 0000-0003-0466-750X.

Ushashi Bhattacharya, Formerly, National Taiwan University, Taipei 106319, Taiwan. Email: rai.bhattacharya.in@gmail.com. ORCID: 0009-0002-2254-3914.

## Licence

MIT, see `LICENSE`.
