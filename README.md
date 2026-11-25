# Quantvaria Labs · Molecular parity violation

Research repository for an enantiomer-resolved spectroscopy experiment. The working question is whether two independently prepared, mirror-related molecules can be shown to have different transition frequencies because of the electroweak interaction. The project compares Yb(III) near-infrared transitions with Re(I) and Ir(III) charge-transfer alternatives. Atomic Yb parity violation and molecular electron EDM experiments provide distinct experimental precedents.

**Release status:** research design and evidence inventory. The recovered discussion contains a lifetime-to-linewidth calculation and qualitative feasibility assessments. It contains no project structures, synthesis records, electronic-structure runs, PV predictions, or measured spectra. The illustrative 0.01 Hz offset is a sensitivity scenario.

| Track | Immediate question |
| --- | --- |
| Yb(hfac)₃ with chiral bipyridine | Do both ligand enantiomers give intact, mirror-related adducts with identifiable NIR lines? |
| Yb–DOTA | Can a macrocyclic control establish a baseline for speciation, exchange and spectral assignment? |
| Carbon-substituted and bridged DOTA derivatives | Can fixed ligand stereochemistry coexist with reproducible Yb coordination and narrow transitions? |
| Re(I) and Ir(III) | Can a charge-transfer transition produce a larger difference in state PV corrections while retaining useful line-centre precision? |

- [Physics and observables](docs/background.md)
- [Candidate designs and chemical validation](docs/candidates.md)
- [Electronic structure and relativistic PV](docs/computation.md)
- [Spectroscopy and controls](docs/spectroscopy.md)
- [Recovered findings and claim status](docs/evidence.md)
- [Reproducibility and roadmap](docs/roadmap.md)
- [Primary references and software documentation](docs/references.md)

Run the discussion's linewidth example with Python 3 and its standard library:

```sh
python3 scripts/linewidth.py
```

The script evaluates lifetime-limited linewidths and the ratio to the hypothetical offset. Candidate run records can use the [manifest template](records/run-template.json). See [contribution and release guidance](CONTRIBUTING.md) before sharing candidate structures or results.
