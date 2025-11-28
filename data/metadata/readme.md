# README — Metadata

### Source of Original Clinical Metadata (PhysioNet)

The metadata included in this folder originate from the PhysioNet dataset "RR Interval Time Series from Healthy Subjects" (Irurzun, I. M., Garavaglia, L., Defeo, M. M., & Thomas Mailland, J. (2021). RR interval time series from healthy subjects (version 1.0.0). PhysioNet. RRID:SCR_007345. https://doi.org/10.13026/51yd-d219). Clinical and methodological details from the original study are reproduced below for transparency and traceability.

Holter recordings were obtained from healthy subjects who were recruited as volunteers after an exhaustive interview and clinical examination. Approval for this study was granted by the Ethics Committee of the National University of La Plata (UNLP) for data protection and privacy. In accordance with the Declaration of Helsinki, all adult participants provided written informed consent, and for participants under 16 years of age, consent was obtained from a parent or legal guardian. The study included individuals without clinical symptoms of disease, who were not taking medication, and whose electrocardiograms (ECG) were normal according to the criteria summarized below.

### Normality Criteria for Holter Records (Table 1)

| Criterion | Description |
|----------|-------------|
| I  | Minimum nighttime frequency > 60/min |
| II | Nighttime pauses < 3 seconds |
| III | Ventricular extrasystoles < 100 per 24 hours, without couplets, bursts, or polymorphism |
| IV | Supraventricular extrasystoles < 100 per 24 hours, without couplets |
| V  | Absence of blocks or conduction disturbances |

Original dataset: https://physionet.org/content/rr-interval-healthy-subjects/1.0.0/

---

## Contents of This Metadata Folder

This directory contains all metadata files necessary to interpret, classify, and reproduce the heart rate variability analyses conducted in this project.

### patient-info.csv
Contains participant-level information extracted and standardized from the PhysioNet dataset headers. Includes:

- File identifier  
- Age (in years)  
- Gender
  
---

## Developmental Stage Classification (WHO)

To support analyses across pediatric developmental stages, subjects were categorized according to the following age brackets, consistent with the definitions used in the study:

- Neonates (0–1 mo)  
- Early infancy (1–5 mo)  
- Late infancy (6–11 mo)  
- Toddlers (1–2 yr)  
- Preschoolers (3–5 yr)  
- School-age (6–11 yr)  
- Adolescents (12–17 yr)  

---
