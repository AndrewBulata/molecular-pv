# Recovered findings and claim status

This inventory covers the conversation history returned by the chat reader for *Explică experimentul EDM*. It includes six turns and no attachments. The title supplies context for the EDM comparison. The returned turns contain no quantitative EDM analysis performed by Quantvaria Labs. The literature checks performed for this repository are identified below.

## Discussion coverage

- The initial Yb design turn proposed the phenylethyl-substituted bipyridine adduct, the unsubstituted bipyridine control, and a relativistic excited-state workflow.
- The measurement turn covered lifetime and linewidth, enantiomeric purity, exchange, sample environment, signal strength, ligand quenching, fluorination or deuteration, and the parallel Re(I) and Ir(III) routes.
- The stability turn proposed Yb–DOTA as a reference, compared mixed chelates with macrocycles, and raised axial hydration and quenching.
- The chirality correction clarified that unsubstituted DOTA lacks fixed ligand chirality. The design then moved to a ring-carbon methyl substitution, with bridging or multiple substituents as follow-ons.
- The final two turns scoped the repository handoff. The EDM and atomic PV references added to this release provide independent context.

## Evidence inventory

| Item | Evidence classification | What the record supports |
| --- | --- | --- |
| Ligand-bearing Yb(hfac)₃ and near-980 nm emission | Established for published analogues | BODIPY-functionalized bipyridine adducts provide an eight-coordinate structural precedent. A chiral helicene adduct provides a NIR chiroptical precedent. [Y1, Y2](references.md#ytterbium-coordination-and-spectroscopy) |
| Yb–DOTA formation constant | Literature result | The chat quoted an approximate log K of 25. A primary potentiometric study reports log K = 26.4 at 25 °C in 0.1 M tetramethylammonium chloride. Retain medium and method with the value. The number describes equilibrium formation. [Y3](references.md#ytterbium-coordination-and-spectroscopy) |
| DOTA chirality, coordination and hydration | Literature context and proposed control | SAP/TSAP and hydration depend on the species and environment. Related chiral derivatives can favour particular isomers. A bridged tetraamide study reports water exclusion in its system. No project ligand-loss rate or isomer distribution is available. [Y4–Y6](references.md#ytterbium-coordination-and-spectroscopy) |
| Yb design choices and comparative ranking | Hypotheses | Steric inhibition of bipyridine binding, reduced quenching through isotopic or chemical substitution, improved retention with a macrocycle, and improved isomer selection through rigidification require separate tests. A large chiral perturbation may still yield a small difference between state PV corrections. |
| Re(I) and Ir(III) charge transfer | Hypothesis with independent chemistry precedent | The chat proposed both as parallel tracks. No metal-specific PV ranking or project transition prediction was recovered. [T1–T3](references.md#transition-metal-comparators) |
| Atomic PV and molecular eEDM | Published experimental context | The published measurements use distinct observables. No molecular enantiomer splitting for the proposed candidates follows from these experiments. [PV3–PV5](references.md#parity-violation-and-edm) |
| Candidate synthesis, structures, spectra and PV energies | Unavailable | No samples, coordinates, calculation logs or raw data support a candidate result or upper bound in this release. |

## Reproduced calculation from the chat

For a Lorentzian lifetime-limited transition with stable lower state and no pure dephasing, coherence time is twice the excited-state population lifetime. The frequency FWHM in Hz is $\Gamma = 1/(2\pi\tau)$.

| Assumed lifetime (ms) | Calculated FWHM (Hz) |
| ---: | ---: |
| 0.1 | 1591.55 |
| 1 | 159.155 |
| 10 | 15.9155 |

For a hypothetical 0.01 Hz shift, the linewidth at 1 ms is about 15,915 times larger. The prior chat rounded this to 16,000. All lifetimes and the shift are hypothetical inputs. The only project calculation reproduced here is this analytic exercise. The [script](../scripts/linewidth.py) uses no experimental or electronic-structure inputs.
