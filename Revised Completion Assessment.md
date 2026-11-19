# 📊 Spatial Data Analysis — Revised Completion Assessment

**Exercise Sheet 1: Spatial Autocorrelation**  
**Updated: 19 November 2026**

This assessment reflects the practical work completed, the GeoDa visualisations confirmed, and the contents of the updated `Exercise_1-1_Report_updated.docx`.

---

# 🟢 1. Exercise 1–1 — Getting to Know the Data and Software

| Requirement | Revised status | Assessment |
|---|---|---|
| 1. Download and open data in GIS and R | 🟡 Partially verified | GIS and Python work are established. The report identifies QGIS, GeoDa and R (`sf`, `spdep`), but actual R loading and inspection outputs still need verification. |
| 2. Explore data visually and histogram | 🟢 Substantially complete | EFDI descriptive statistics, histogram and distribution map are discussed. Check that the actual figures are present and remove obsolete figure placeholders. |
| 3. Understand EFDI | 🟢 Complete | Four domains, interpretation and limitations are discussed. |
| 4. Understand LSOAs | 🟢 Complete | LSOA characteristics and geographical units are explained. |
| 5. Discuss index, units and spatial distribution | 🟢 Substantially complete | The report discusses relative accessibility, affordability, MAUP, spatial dependence by construction, edge effects, unequal unit sizes and mixed time references. |

### Report review

The updated report contains:

- Dataset overview and attribute descriptions.
- EFDI domains and interpretation.
- LSOA characteristics.
- Descriptive statistics and spatial exploration.
- Discussion of the index and spatial units.
- Limitations of the dataset and geographical units.

**Remaining corrections:**

1. Reconcile the reported EFDI minimum of 0.00 with the 2,365-observation analysis minimum of 3.5098.
2. Treat the explanation for the 90 missing observations as a hypothesis until the 2001 and 2011 LSOA identifiers and boundaries are checked.
3. Clearly distinguish the 2,455 original polygons from the 2,365 observations with EFDI values.
4. Verify that the histogram and distribution map are actually embedded and remove any obsolete figure placeholders.

**Assessment:** Exercise 1–1 is nearly complete. The main outstanding verification is the R requirement and final report corrections.

---

# 🟡 2. Exercise 1–2 — Identifying Suitable Spatial Weights

| Requirement | Revised status | Assessment |
|---|---|---|
| 1. Discuss alternative spatial weights and justify selection | 🟢 Complete | Queen, KNN6, 6 km distance band and inverse-distance weights have been discussed. |
| 2. Create weights in GeoDa and inspect connectivity graph, neighbourhood map and histogram | 🟢 Complete | All four spatial weights have been created/loaded. The three required GeoDa visualisations have been confirmed for all four methods. |
| 3. Implement weights in R using `spdep` | 🔴 Not verified | Python implementations exist, but the required R code and outputs have not been established. |
| 4. Examine the `listw` object | 🟡 Conceptually complete | The structure is understood, but inspection of the actual R `listw` object remains to be confirmed. |
| 5. Calculate eigenvalues and apply scaling | 🔴 Outstanding | Eigenvalue results and the required scaling calculation have not been confirmed. |

### 📌 Four spatial weights established

1. Queen contiguity — `wm_queen`
2. K-nearest neighbours (KNN6) — `wm_knn6`
3. Distance band (6 km) — `wm_dist_6km`
4. Inverse distance (6 km, power 1) — `wm_idw_6km_p1`

### GeoDa visualisation verification

| Spatial weights | Connectivity graph | Neighbourhood map | Weights histogram |
|---|---|---|---|
| Queen | ✅ | ✅ | ✅ |
| KNN6 | ✅ | ✅ | ✅ |
| Distance band 6 km | ✅ | ✅ | ✅ |
| Inverse distance 6 km (p = 1) | ✅ | ✅ | ✅ |

**Assessment:** The GeoDa visualisation requirement is complete for all four methods. The updated report currently documents the Queen weights in detail; the other three methods should be included in the written comparison if the report is intended to document all four.

### Queen weights — confirmed statistics

| Statistic | Value |
|---|---:|
| Observations | 2,365 |
| Directed non-zero links | 13,724 |
| Minimum neighbours | 1 |
| Maximum neighbours | 21 |
| Mean neighbours | 5.80 |
| Median neighbours | 6 |
| Percentage non-zero | 0.25% |

The report includes the GeoDa Queen weights summary and a comparison with Python. The R column and R summary figure remain incomplete.

---

# 🟡 3. Exercise 1–3 — Calculation and Interpretation of Moran's I

| Requirement | Revised status | Assessment |
|---|---|---|
| 1. Global Moran's I under different null hypotheses and inference methods | 🟡 Partially complete | Global Moran's I and permutation randomisation have been calculated in Python. The comparison of `moran.test()` and `moran.mc()` in R under different inference assumptions remains outstanding. |
| 2. Calculate Local Moran's I and add I-values, p-values and local variances | 🟡 Partially complete | Local I, p-values and quadrants are stored in Python. Local variances have not been added. |
| 3. Map all values meaningfully and assess results | 🟡 Mostly complete | EFDI distribution and LISA cluster maps have been created. Local I and local variance maps still need consideration. |
| 4. Discuss overall results and justify the most appropriate approach | 🟡 Partially complete | Results have been interpreted, but the final comparison and methodological justification remain necessary. |
| 5. Create Moran scatterplots in GeoDa and interpret them | 🔴 Outstanding / not verified | The updated report still has a placeholder for the Moran scatterplot (Figure 10). |

### 📈 Global Moran's I — established result

| Statistic | Verified result |
|---|---:|
| Observed Global Moran's I | +0.453153 |
| Expected I | −0.000423 |
| Permutations | 999 |
| Permutation p-value | 0.001 |

**Interpretation:** The positive Global Moran's I indicates positive spatial autocorrelation. Similar EFDI values tend to be located near one another.

**Important correction concerning 9,999 permutations:** Code was written to run 9,999 permutations, but the subsequent execution produced an error. A successful output has not been confirmed. Therefore, the verified result remains the earlier run with 999 permutations and p = 0.001.

### 🗺️ Local Moran's I — LISA results

| Classification | Number of LSOAs |
|---|---:|
| 🔴 High–High | 307 |
| 🔵 Low–Low | 348 |
| 🩵 Low–High | 32 |
| 🟠 High–Low | 31 |
| ⚪ Not significant | 1,647 |
| **Total** | **2,365** |

*Counts use the unadjusted p-value threshold of 0.05.*

**Completed:**

- Local Moran's I values (`local_I`).
- Local permutation p-values (`p_sim`).
- Quadrant classifications (`quadrant`).
- LISA cluster map.
- Interpretation of local clusters and spatial outliers.

**Outstanding:**

- Add local variances of I to the data.
- Map and interpret the local variance results.
- Complete the requested Moran scatterplot in GeoDa.

---

# 🧭 4. Updated List of Outstanding Work

The following order avoids repeating completed analyses.

| No. | Outstanding task | Status |
|---|---|---|
| 1 | Implement Queen, KNN and distance-based neighbours in R using `spdep` | 🔴 Outstanding |
| 2 | Inspect the actual R `nb` and `listw` objects | 🟡 To verify |
| 3 | Calculate eigenvalues using `eigenw()` and apply the required scaling | 🔴 Outstanding |
| 4 | Compare Global Moran's I using `moran.test()` and `moran.mc()` in R | 🔴 Outstanding |
| 5 | Calculate and add local variances of I | 🔴 Outstanding |
| 6 | Map and interpret local I and local variance | 🟡 Incomplete |
| 7 | Create and interpret GeoDa Moran scatterplots | 🔴 Outstanding |
| 8 | Complete the final methodological discussion | 🟡 Incomplete |

### Eigenvalue scaling formula

The scaling factor specified by the lecturer is:

\[
\frac{n}{\sum_i\sum_j w_{ij}}
\]

This calculation should be completed using the appropriate spatial weights and their corresponding weight matrix.

---

# 📝 5. Report Corrections Before Submission

1. **EFDI minimum:** Reconcile the reported minimum of 0.00 with the minimum of 3.5098 in the 2,365-observation analytical sample.
2. **Missing observations:** Describe the possible 2001/2011 LSOA boundary mismatch as a hypothesis until the identifiers and boundaries are verified.
3. **Observation counts:** Distinguish the 2,455 original polygons from the 2,365 observations with valid EFDI values.
4. **R evidence:** Complete the missing R summary figure and the R results columns in the comparison tables.
5. **Four spatial weights:** Add a comparison of Queen, KNN6, distance band and inverse distance to the report.
6. **Moran scatterplot:** Replace the Figure 10 placeholder with the actual GeoDa scatterplot and interpretation.
7. **Figure placeholders:** Check that all figures are embedded correctly and remove obsolete instructions such as `[Figure to be added]`.

---

# 🎯 6. Final Verdict

| Exercise | Assessment |
|---|---|
| Exercise 1–1 | 🟢 Nearly complete |
| Exercise 1–2 | 🟡 Partially complete — all four GeoDa visualisation sets are complete |
| Exercise 1–3 | 🟡 Partially complete |

**Important distinction:** The worksheet requests work using R (`sf`, `spdep`, `spatialreg`) and GeoDa. Python has helped us understand and verify many spatial concepts, but Python results alone do not demonstrate completion of the requested R tasks.

### Recommended next step

Start with **Exercise 1–2, Question 3: R implementation of spatial weights**. Then inspect the actual `nb` and `listw` objects before proceeding to eigenvalues.

This provides the logical foundation for the remaining R-based analyses without repeating the four sets of GeoDa connectivity visualisations that are already complete.