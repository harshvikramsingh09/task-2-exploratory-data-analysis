"""
Task 2: Exploratory Data Analysis (EDA)
Dataset: Iris
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "iris.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
print("Dataset shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())

numeric_cols = df.select_dtypes(include=np.number).columns
print("\nSummary statistics:\n", df[numeric_cols].describe().T)
print("\nMedian:\n", df[numeric_cols].median())
print("\nSkewness:\n", df[numeric_cols].skew())

# Histograms
plt.figure(figsize=(9, 6))
for col in numeric_cols:
    plt.hist(df[col], bins=12, alpha=0.45, label=col)
plt.title("Distribution of Numeric Features")
plt.xlabel("Value (cm)")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig(OUT / "histograms.png", dpi=160)
plt.show()

# Boxplots
plt.figure(figsize=(9, 5))
sns.boxplot(data=df[numeric_cols])
plt.title("Boxplots of Numeric Features")
plt.tight_layout()
plt.savefig(OUT / "boxplots.png", dpi=160)
plt.show()

# Correlation matrix
plt.figure(figsize=(7, 5))
sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(OUT / "correlation_matrix.png", dpi=160)
plt.show()

# Pairplot
sns.pairplot(df, hue="species", diag_kind="hist")
plt.show()

# Plotly interactive visualization
fig = px.scatter(df, x="petal_length_cm", y="petal_width_cm",
                 color="species", title="Petal Length vs Petal Width")
fig.show()
