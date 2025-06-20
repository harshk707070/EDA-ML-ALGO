# Geldium Credit Risk EDA – Tata iQ Analytics Case Study 🧠💳

This project showcases an end-to-end **Exploratory Data Analysis (EDA)** pipeline on Geldium’s customer dataset, as part of the **Tata iQ Credit Risk Challenge**. The goal is to analyze customer behavior and financial data to uncover patterns linked to **credit card delinquency** and help shape future risk intervention strategies.

---

---

## 📌 Project Goals

- Analyze Geldium’s dataset for quality, trends, and delinquency signals.
- Detect missing/inconsistent values and apply best-practice imputation strategies.
- Surface behavioral and financial patterns that influence delinquency.
- Integrate Generative AI (ChatGPT/DeepSeek) to generate structured insights and automate decisions.

---

## 🔍 Dataset Summary

- **Records**: 500 rows × 19 columns  
- **Target Variable**: `Delinquent_Account` (Binary – 0: No, 1: Yes)
- **Key Features**:
  - `Credit_Score`, `Income`, `Loan_Balance`, `Missed_Payments`
  - `Credit_Utilization`, `Debt_to_Income_Ratio`, `Employment_Status`, etc.

---

## 🧠 GenAI-Powered EDA Workflow

This project is aligned with Tata iQ’s official EDA workflow:

### ✅ Step 1: Dataset Review
- Identified missing data in **Income (7.8%)**, **Loan_Balance (5.8%)**, and **Credit_Score (0.4%)**
- Used GenAI to flag anomalies and key predictors:
  - `Missed_Payments`, `Credit_Utilization`, `Credit_Score`

### 🧼 Step 2: Data Cleaning & Imputation
- `Income`: Imputed using **Median**
- `Loan_Balance`: Imputed using **Mean**
- `Credit_Score`: Imputed using **Median**

### 📊 Step 3: Risk Pattern Detection
- Delinquency strongly associated with:
  - **High Missed Payments**
  - **Credit Utilization > 0.6**
  - **Credit Score < 450**
- Visualized distributions & relationships using boxplots, histograms, and bar charts.

---

## 🧪 AI Prompt Usage

This project uses prompt engineering to generate automated insights:

- 📌 _"Summarize key patterns, missing values, and anomalies in this dataset..."_
- 📌 _"Suggest an imputation strategy for missing income values based on financial best practices..."_
- 📌 _"Which features are most predictive of credit card delinquency?"_

✅ Each notebook step ends with:
- **AI Prompt Used**
- **GenAI Output Summary**

---

## 📈 Key Findings

- **16%** of users were flagged as delinquent → target imbalance detected.
- `Missed_Payments` is the most direct and impactful feature.
- Anomalies: Some `Credit_Utilization` values > 1.0 → potential data error or modeling risk.
- `Self-employed` and `Unemployed` segments show higher average delinquency rates.

---

## 📄 Final Deliverables

- 📓 `Geldium_EDA_Final.ipynb`: Step-by-step EDA with AI annotations
- 📃 `Geldium_EDA_Report.pdf`: Structured report for submission
- 🧠 README for portfolio/showcase

---

## 🚀 Next Steps (Future Work)

- Train classification models (Logistic Regression, Random Forest, etc.)
- Address class imbalance via SMOTE or reweighting.
- Build an interactive **Streamlit dashboard** for risk prediction.

---

## 🙌 Author

**Harsh** – [@harshk707070](https://github.com/harshk707070)  
This repository was created as part of the Tata iQ Credit Risk Challenge 2025.

---

## 📜 License

This project is intended for academic, educational, and showcase purposes only.


