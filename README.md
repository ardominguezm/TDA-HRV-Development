# Topological Data Analysis of Pediatric Heart Rate Variability

This repository contains the full data-processing pipeline, analysis scripts, and documentation for the study:

> **Domínguez A., Mateos A., Jiménez A.**  
> *Age-dependent patterns of cardiac complexity unveiled by topological data analysis of pediatric heart rate variability*.  
> **PLOS ONE**, 20(11): e0337620.  
> https://doi.org/10.1371/journal.pone.0337620

The repository follows a FAIR-compliant structure, separating raw data, processed data, metadata, analysis products, and executable code.

---

## 📁 Repository Structure

TDA-HRV-Development/
│
├── data/
│ ├── raw/
│ ├── processed/
│ └── metadata/
│
├── code/
├── analysis/
├── docs/
│
└── README.md
---

## Data Sources

### **1. PhysioNet – RR Interval Time Series from Healthy Subjects**
- **Dataset:** RR Interval Time Series from Healthy Subjects  
- **URL:** https://physionet.org/content/rr-interval-healthy-subjects/1.0.0/  
- **Subjects:** 147 healthy individuals (ages 1 month to 55 years)  
- **Notes:** Signals include artifact filtering and DFA metrics (original study)

### **2. Metadata**
Located in: `data/metadata/patient-info.csv`  
Includes:
- Age  
- Sex  
- Recording ID  
- Study source  
- WHO developmental stage grouping  

---

## Workflow Overview

1. **Preprocessing** – `01_Preprocessing_HRV.ipynb`  
2. **Embedding Parameter Selection** – `00-Parameters_embedding.ipynb`  
3. **Topological Feature Extraction** – `02_Topological_Feature_Extraction.ipynb`  
4. **Conventional HRV Metrics** – `03_HRV_Conventional_Analysis.ipynb`  
5. **Statistical Analysis & Visualization** – `stats_analysis.py`

---

## Reproducibility

Install environment:

```bash
pip install -r requirements.txt
