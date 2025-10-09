# Topological Data Analysis of Pediatric Heart Rate Variability

This repository contains all scripts, notebooks, and documentation used in the study:

> **"Age-dependent Topological Signatures of Cardiac Complexity Revealed by Persistent Homology"**

---

## 📁 Repository Structure
```
TDA-HRV-Development/
│
├── data/
│   ├── raw/                           # (reference to PhysioNet dataset)
│   ├── processed/                     # preprocessed RR interval time series
│   └── README.md
│
├── notebooks/
│   ├── 01_Preprocessing_HRV.ipynb
│   ├── 01_HRV_Conventional_Analysis.ipynb
│   ├── 02_Topological_Feature_Extraction.ipynb
│   ├── parameters_embedding.ipynb
│   └── README.md
│
├── results/
│   ├── figures/
│   ├── summary_tables/
│   └── README.md
│
├── src/
│   ├── preprocess.py
│   ├── tda_features.py
│   ├── visualization.py
│   ├── stats_analysis.py
│   └── README.md
│
├── environment.yml
├── LICENSE
├── README.md
└── CITATION.cff
```

---

## ⚙️ Environment Setup
Create the conda environment:
```bash
conda env create -f environment.yml
conda activate tda_hrv
```

**Main dependencies:**
- Python ≥ 3.10
- numpy, pandas, scipy
- matplotlib, seaborn
- ripser, persim, gtda
- tqdm, pingouin

---

## 🧩 Workflow Overview
1. **Preprocessing** (`notebooks/01_Preprocessing_HRV.ipynb`)
   - Loads RR interval time series from PhysioNet
   - Performs artifact filtering, z-score normalization, and truncation (3000 points)

2. **Embedding Parameter Selection** (`parameters_embedding.ipynb`)
   - Estimates optimal delay (τ) and embedding dimension (d)
   - Compares FNN and Cao’s methods

3. **Topological Feature Extraction** (`02_Topological_Feature_Extraction.ipynb`)
   - Builds delay embeddings using τ=10, d=3
   - Computes persistent homology (H₁), landscapes, and persistence entropy

4. **Conventional HRV Analysis** (`01_HRV_Conventional_Analysis.ipynb`)
   - Calculates SDNN, RMSSD, PNN50
   - Performs Kruskal–Wallis tests across developmental age groups

5. **Statistical Analysis & Visualization** (`src/stats_analysis.py`)
   - Correlation analyses between TDA and conventional metrics
   - Landscape distance matrices (intra/inter-group)
   - Generates publication-ready figures and tables

---

## 🧬 Data Availability
Raw RR interval data are publicly available from PhysioNet:
> [RR interval time series from healthy subjects](https://doi.org/10.13026/C2V88V)

All processed data and analysis scripts are available in this repository for full reproducibility.

---

## 🧾 Citation
If you use this code or data, please cite:

```
Domínguez, A. (2025). TDA-HRV-Development: Topological Data Analysis of Pediatric Heart Rate Variability.
GitHub repository: https://github.com/andydom/TDA-HRV-Development
```

---

## 📚 References
- Goldberger AL et al. (2000). *PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals.* Circulation. [https://doi.org/10.1161/01.CIR.101.23.e215](https://doi.org/10.1161/01.CIR.101.23.e215)
- Irurzun IM et al. (2021). *RR interval time series from healthy subjects.* PhysioNet. [https://doi.org/10.13026/C2V88V](https://doi.org/10.13026/C2V88V)
