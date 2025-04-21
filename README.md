# 🧠 IBM HR Attrition Analysis – A People Analytics Mini Project

This project explores the IBM HR Analytics Employee Attrition dataset to uncover key drivers of employee turnover, segment employee profiles, and build a simple, interpretable model to predict attrition. It combines real-world HR context with hands-on data science.

---

## 🎯 Project Goals

- Identify major drivers of employee attrition
- Cluster employees into behavioral profiles
- Build a logistic regression model to predict attrition
- Visualize insights for actionable HR decision-making

---

## 🗂️ Dataset

- Source: [IBM HR Analytics Employee Attrition & Performance (Kaggle)](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- Format: CSV (1,470 employee records, 35 features)
- Type: Fictional corporate HR dataset created by IBM

---

## 🧪 Key Techniques Used

- `Pandas` & `Seaborn` for EDA and visualizations
- `StandardScaler` for feature scaling
- `KMeans` for unsupervised clustering
- `PCA` for dimensionality reduction and visualization
- `LogisticRegression` for interpretable classification

---

## 🔍 Analysis Overview

### ✅ 1. Data Cleaning & Preprocessing
- Removed irrelevant columns (e.g., EmployeeNumber, StandardHours)
- Encoded binary variables and one-hot encoded categoricals
- Scaled all features for PCA and modeling

### 📊 2. Exploratory Data Analysis (EDA)
- Found strong correlation between attrition and:
  - Overtime
  - Low monthly income
  - Low job satisfaction
  - Long commute distances

### 🧠 3. Clustering with K-Means
- Segmented employees into 3 clusters
- Identified high-risk cluster (young, underpaid, low satisfaction)
- Visualized profiles using normalized barplot and radar chart

### 🔬 4. Dimensionality Reduction with PCA
- Used PCA to reduce feature space to 2D
- Visualized clustering and partial separation of leavers vs. stayers

### 🤖 5. Predictive Modeling (Logistic Regression)
- Accuracy: **88%**
- Precision (leavers): **72%**
- Recall (leavers): **41%**
- Visualized confusion matrix and top feature coefficients
- Key predictors of attrition:
  - `OverTime`, `FrequentTravel`, `YearsSinceLastPromotion`
  - Negative predictors: `JobSatisfaction`, `TotalWorkingYears`, `Age`

---

## 📈 Final Takeaways

- Employees who work overtime, travel frequently, or feel stagnant (no recent promotion) are much more likely to leave.
- Satisfaction and tenure are strong protectors against attrition.
- A basic logistic regression model can serve as a practical early-warning tool to flag flight-risk employees — especially when combined with HR insight.

---

## 🚀 Next Steps (Future Work)

- Handle class imbalance with SMOTE or weighted logistic regression
- Try Random Forest or XGBoost for improved recall
- Tune decision thresholds to reduce false negatives
- Deploy as an interactive dashboard with Streamlit or Power BI

---

## 👤 Author

**Timur Akhtemov**  
Software Developer | Exploring People Analytics 
[LinkedIn](https://www.linkedin.com/in/timurakhtemov/)