# Topological Data Analysis of Pediatric Heart Rate Variability

This repository contains all scripts used in the study:

> **"Age-dependent Topological Signatures of Cardiac Complexity Revealed by Persistent Homology, PLoS One, In review (Oct 2025)"**

---


##  Workflow overview
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

5. **Statistical Analysis & Visualization** (`stats_analysis.py`)
   - Correlation analyses between TDA and conventional metrics
   - Landscape distance matrices (intra/inter-group)
   - Generates publication-ready figures and tables

---

##  Data availability
Raw RR interval data are publicly available from PhysioNet:
> [RR interval time series from healthy subjects]([https://doi.org/10.13026/C2V88V](https://doi.org/10.13026/51yd-d219))

---


GitHub repository: https://github.com/andydom/TDA-HRV-Development
```
