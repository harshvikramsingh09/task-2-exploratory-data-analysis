## Title

**Task 2: Exploratory Data Analysis (EDA) Using Python**

### GitHub Repository Name
`task-2-exploratory-data-analysis`

## README.md

```markdown
# Task 2: Exploratory Data Analysis (EDA) Using Python

## 📌 Project Overview

This project is part of the **AI & ML Internship – Task 2: Exploratory Data Analysis (EDA)**.

The objective of this task is to understand a dataset using **descriptive statistics, data visualization, correlation analysis, and pattern recognition**.

The analysis is performed using Python libraries such as **Pandas, NumPy, Matplotlib, Seaborn, and Plotly**.

---

## 🎯 Objectives

The main objectives of this project are:

- Generate descriptive statistics such as mean, median, standard deviation, minimum, and maximum.
- Analyze the distribution of numerical features.
- Create histograms and boxplots.
- Analyze relationships between features.
- Create a correlation matrix.
- Create a pairplot for feature-level analysis.
- Identify patterns, trends, and potential anomalies.
- Make basic feature-level inferences from visualizations.

---

## 📊 Dataset

### Iris Dataset

The **Iris dataset** is used for this analysis.

The dataset contains:

- **150 observations**
- **4 numerical features**
- **3 species/classes**

### Features

| Feature | Description |
|---|---|
| `sepal_length_cm` | Sepal length in centimeters |
| `sepal_width_cm` | Sepal width in centimeters |
| `petal_length_cm` | Petal length in centimeters |
| `petal_width_cm` | Petal width in centimeters |
| `species` | Iris species/class |

The dataset is included in the repository under:

```text
data/iris.csv
```

---

## 🛠️ Technologies & Libraries

The following tools and libraries were used:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Jupyter Notebook

---

## 📁 Project Structure

```text
task-2-exploratory-data-analysis/
│
├── data/
│   └── iris.csv
│
├── outputs/
│   ├── boxplots.png
│   ├── correlation_matrix.png
│   ├── histograms.png
│   ├── interactive_scatter.html
│   ├── pairplot.png
│   └── summary_statistics.csv
│
├── EDA_Task2.ipynb
├── eda_analysis.py
├── interview_questions.md
├── requirements.txt
└── README.md
```

---

## 🔍 Exploratory Data Analysis Performed

### 1. Data Inspection

The dataset was inspected to understand:

- Number of rows and columns
- Data types
- Missing values
- Numerical features
- Dataset structure

### 2. Descriptive Statistics

The following statistics were calculated:

- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- Median
- 75th percentile
- Maximum
- Skewness

### 3. Histograms

Histograms were created to understand the distribution of numerical features.

Output:

```text
outputs/histograms.png
```

### 4. Boxplots

Boxplots were created to analyze:

- Data spread
- Median
- Quartiles
- Potential extreme observations

Output:

```text
outputs/boxplots.png
```

### 5. Correlation Analysis

A correlation matrix was created to understand relationships between numerical variables.

Output:

```text
outputs/correlation_matrix.png
```

### 6. Pairplot

A pairplot was created to visualize relationships between numerical features and observe differences between species.

Output:

```text
outputs/pairplot.png
```

### 7. Interactive Visualization

An interactive Plotly scatter plot was created using:

- Petal Length
- Petal Width
- Species

Output:

```text
outputs/interactive_scatter.html
```

---

## 📈 Key Findings

The EDA produced the following observations:

1. The dataset contains **150 observations**.
2. There are **four numerical measurement features**.
3. The dataset contains **three species/classes**.
4. No missing values were found in the dataset.
5. Petal length and petal width show a strong positive relationship.
6. Petal measurements provide clearer separation between species compared with sepal measurements.
7. Histograms help understand the distribution and skewness of numerical variables.
8. Boxplots provide a quick view of feature spread and observations at distribution extremes.

---

## 📊 Summary Statistics

| Feature | Mean | Median | Std. Dev. | Min | Max |
|---|---:|---:|---:|---:|---:|
| Sepal Length | 5.843 | 5.80 | 0.828 | 4.3 | 7.9 |
| Sepal Width | 3.057 | 3.00 | 0.436 | 2.0 | 4.4 |
| Petal Length | 3.758 | 4.35 | 1.765 | 1.0 | 6.9 |
| Petal Width | 1.199 | 1.30 | 0.762 | 0.1 | 2.5 |

Complete statistics are available in:

```text
outputs/summary_statistics.csv
```

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### Step 2: Open the Project

```bash
cd task-2-exploratory-data-analysis
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Python Script

```bash
python eda_analysis.py
```

### Step 5: Run the Jupyter Notebook

Open:

```text
EDA_Task2.ipynb
```

using Jupyter Notebook, JupyterLab, or VS Code.

---

## 💡 Interview Questions

The repository also contains answers to the interview questions provided in the internship task.

File:

```text
interview_questions.md
```

Topics include:

- Purpose of EDA
- Boxplots
- Correlation
- Skewness
- Multicollinearity
- EDA tools
- Practical use of EDA
- Role of visualization in Machine Learning

---

## 📌 Conclusion

Exploratory Data Analysis provides an important foundation for machine learning by helping understand the dataset before model development.

Through descriptive statistics and visualizations, this project identifies feature distributions, relationships, correlations, and class-level patterns that can support subsequent machine learning analysis.

---

## 👩‍💻 Author

**Harsh vikram Singh**

AI & ML Internship

---

## ⭐ Internship Task

**Task:** Task 2 – Exploratory Data Analysis (EDA)

**Focus:** Data Visualization, Descriptive Statistics, and Pattern Recognition
```
