# Task 2 – Exploratory Data Analysis (EDA)

## Objective
Understand data using statistics and visualizations.

This repository implements the provided internship task:
- Summary statistics (mean, median, standard deviation, etc.)
- Histograms and boxplots for numeric features
- Pairplot and correlation matrix
- Pattern, trend, and anomaly identification
- Basic feature-level inferences

## Dataset
**Iris dataset** — 150 observations, four numeric measurements, and three species classes.

The CSV is included locally in `data/iris.csv`, so no external dataset download is required.

## Tools
Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-learn, Jupyter.

## Repository Structure
```text
task-2-eda/
├── data/iris.csv
├── outputs/
│   ├── boxplots.png
│   ├── correlation_matrix.png
│   ├── histograms.png
│   ├── interactive_scatter.html
│   ├── pairplot.png
│   └── summary_statistics.csv
├── EDA_Task2.ipynb
├── eda_analysis.py
├── interview_questions.md
├── requirements.txt
└── README.md
```

## Run
```bash
python -m pip install -r requirements.txt
python eda_analysis.py
```
Or open `EDA_Task2.ipynb` in Jupyter/VS Code.

## Key Findings
1. The dataset has 150 rows, four numeric measurements, and a species label.
2. No missing values are present.
3. Petal length and petal width have a strong positive correlation.
4. Petal measurements show clearer species separation in the pairplot.
5. Histograms reveal the distribution shape of each numeric feature.
6. Boxplots summarize spread and help identify observations at distribution extremes.

## Submission
The internship instructions require a separate GitHub repository for each task containing the code, dataset, screenshots/outputs if used, and a short README.
