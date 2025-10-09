# Topological Data Analysis of Pediatric Heart Rate Variability

This repository contains all scripts used in the study:

> **"Domínguez A., Mateos A., Jiménez A., Age-dependent patterns of cardiac complexity unveiled by topological data analysis of pediatric heart rate variability, PLoS One, In review (Oct 2025)"**

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
   - figures and tables


##  Data availability
Raw RR interval data are publicly available from PhysioNet:
> [RR interval time series from healthy subjects]([https://doi.org/10.13026/51yd-d219](https://doi.org/10.13026/51yd-d219))

