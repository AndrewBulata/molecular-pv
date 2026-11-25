# Reproducibility and roadmap

| Stage | Deliverable | Decision |
| --- | --- | --- |
| 0. Define species | Atom-mapped connectivities, stereo descriptors, isotope and charge models, matched chemical controls | Advance only unambiguous candidate definitions. |
| 1. Establish baselines | Literature control geometries, convergence checks, benchmark PV sign and scale, candidate speciation | Proceed when the computational benchmark, reflection and null checks pass and chemical identities are defined. |
| 2. Screen candidates in parallel | Yb stability and NIR spectra, Re/Ir excited-state assignment and photophysics, model uncertainties | Down-select based on repeatable chemistry and a measurable transition. Preserve failed and inconclusive screens. |
| 3. Quantify sensitivity | State-resolved PV estimates and error budget, blinded precision and systematics pilot | Compare the predicted signal interval with demonstrated differential precision. Revisit design or report a feasibility limit if uncertainty dominates. |
| 4. Differential study | Prespecified analysis, coded runs, independent samples and complete provenance | Report estimate and uncertainty, including null or upper-limit outcomes where warranted. |

## Record format

Create a new directory `runs/<record-id>/` for a calculation or acquisition and copy the [manifest template](../records/run-template.json). Use immutable IDs and link related structures, samples, controls and repeats. Keep machine-generated raw records and any data exclusions auditable. Use a versioned archive for large files and record its persistent locator and SHA-256 hash. Archive failures with a reason and enough detail to reproduce them.

- **Chemistry:** batch IDs, chemical sources, identity and purity assays, exact conditions, handling time, counterion, water content and structural-assignment evidence.
- **Calculation:** code and build versions, command, inputs, basis and potential files, nuclear model, active orbitals and roots, Hamiltonian and operator, numerical thresholds, geometry and state tracking, restart history, raw logs and convergence outputs.
- **Spectroscopy:** raw signal and frequency axis, sample/blind code, acquisition order, calibration and settings, repeats, fitting script, residuals, uncertainty budget and a record of when masking was lifted.

Use `planned`, `failed` or `completed` for run state and `proposed`, `illustrative`, `literature`, `computed` or `measured` for claim status. For `computed` and `measured` claims, attach raw evidence, units, method and uncertainty or an explicit account of unresolved error sources. Check point estimates and signs against the calculation or acquisition record before citing them in the README.
