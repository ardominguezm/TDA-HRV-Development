"""
stats_analysis.py
-----------------
Statistical analysis utilities for comparing conventional HRV and
Topological Data Analysis (TDA) metrics across pediatric developmental groups.
"""

import numpy as np
import pandas as pd
import pingouin as pg
from scipy.stats import kruskal
from scikit_posthocs import posthoc_dunn
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# 1. Kruskal–Wallis + Dunn post-hoc tests by group
# ============================================================

def kruskal_dunn_by_group(df, value_col, group_col="Age_Group"):
    """
    Performs Kruskal–Wallis test followed by Dunn's post-hoc test.

    Parameters
    ----------
    df : pd.DataFrame
        Data containing the metric and the grouping variable.
    value_col : str
        Name of the numeric column to analyze.
    group_col : str
        Categorical grouping variable (default: "Age_Group").

    Returns
    -------
    dict : containing H-statistic, p-value, and Dunn's post-hoc matrix.
    """
    # Kruskal–Wallis
    groups = [group[value_col].dropna().values for _, group in df.groupby(group_col)]
    H, p = kruskal(*groups)

    # Dunn post-hoc (adjusted p-values)
    dunn = posthoc_dunn(df, val_col=value_col, group_col=group_col, p_adjust='bonferroni')

    print(f"\n📊 {value_col}: Kruskal–Wallis H={H:.3f}, p={p:.5f}")
    return {"H": H, "p": p, "dunn": dunn}


# ============================================================
# 2. Correlations between TDA and conventional HRV metrics
# ============================================================

def correlations_tda_hrv(df, tda_cols, hrv_cols):
    """
    Compute pairwise Pearson correlations between TDA descriptors and HRV metrics.

    Parameters
    ----------
    df : pd.DataFrame
        Data containing TDA and HRV metrics.
    tda_cols : list of str
        TDA metric columns.
    hrv_cols : list of str
        HRV metric columns.

    Returns
    -------
    corr_table : pd.DataFrame
        Summary of correlations (r, p).
    """
    results = []
    for tda in tda_cols:
        for hrv in hrv_cols:
            x, y = df[tda].dropna(), df[hrv].dropna()
            common_idx = x.index.intersection(y.index)
            if len(common_idx) < 5:
                continue
            corr = pg.corr(df.loc[common_idx, tda], df.loc[common_idx, hrv])
            results.append({
                "TDA_Feature": tda,
                "HRV_Metric": hrv,
                "r": corr.at[0, 'r'],
                "p": corr.at[0, 'p-val']
            })
    corr_table = pd.DataFrame(results)
    print("\n✅ Correlation analysis completed.")
    return corr_table


# ============================================================
# 3. Visualization utilities
# ============================================================

def plot_group_boxplots(df, metric_cols, group_col="Age_Group", figsize=(12, 6)):
    """
    Create boxplots for a list of metrics across age groups.
    """
    n = len(metric_cols)
    fig, axes = plt.subplots(1, n, figsize=(6*n, 5))
    if n == 1:
        axes = [axes]
    for ax, metric in zip(axes, metric_cols):
        sns.boxplot(data=df, x=group_col, y=metric, ax=ax, palette="Set2")
        sns.stripplot(data=df, x=group_col, y=metric, color='k', size=2, alpha=0.4, ax=ax)
        ax.set_title(metric, fontsize=11)
        ax.set_xlabel("")
        ax.set_ylabel(metric)
        ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(corr_table, figsize=(8,6)):
    """
    Generate a heatmap from the correlation table.
    """
    pivot = corr_table.pivot(index="TDA_Feature", columns="HRV_Metric", values="r")
    plt.figure(figsize=figsize)
    sns.heatmap(pivot, annot=True, cmap="coolwarm", center=0, fmt=".2f", cbar_kws={'label': 'Pearson r'})
    plt.title("Correlation between TDA Descriptors and HRV Metrics")
    plt.tight_layout()
    plt.show()


# ============================================================
# Example usage (can be removed or adapted for notebooks)
# ============================================================

if __name__ == "__main__":
    df = pd.read_csv("results/summary_tables/HRV_TDA_merged.csv")

    # Example Kruskal–Wallis for HRV indices
    for metric in ["mean_RR", "SDNN_RR", "RMSSD_RR", "PNN50_RR"]:
        kruskal_dunn_by_group(df, metric)

    # Example correlations
    tda_features = ["N1", "TP1", "MP1", "mu1", "PE1"]
    hrv_metrics = ["mean_RR", "SDNN_RR", "RMSSD_RR", "PNN50_RR"]
    corr_results = correlations_tda_hrv(df, tda_features, hrv_metrics)
    corr_results.to_csv("results/summary_tables/TDA_HRV_correlations.csv", index=False)
