# 📊 Exploratory Data Analysis (EDA)
### CodeAlpha Data Analytics Internship — Task 2

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.1-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Project Overview

This project performs a complete **Exploratory Data Analysis (EDA)** on an Employee HR Dataset. The goal is to uncover patterns, validate hypotheses, detect anomalies, and extract meaningful business insights using Python.

---

## 🎯 Objectives Covered

| # | Objective | Status |
|---|-----------|--------|
| 1 | Ask meaningful questions about the dataset | ✅ Done |
| 2 | Explore data structure (variables & types) | ✅ Done |
| 3 | Identify trends, patterns and anomalies | ✅ Done |
| 4 | Test hypotheses and validate assumptions | ✅ Done |
| 5 | Detect potential data issues or problems | ✅ Done |

---

## 📁 Project Structure

```
codealpha-eda/
│
├── eda_analysis.py          # Main EDA script (all steps)
│
├── data/
│   └── employee_dataset.csv # Dataset (500 rows × 10 features)
│
├── charts/
│   └── eda_dashboard.png    # 7-chart visual dashboard
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📦 Dataset Description

**Source:** Synthetically generated Employee HR Dataset  
**Records:** 500 employees | **Features:** 10 columns

| Column | Type | Description |
|--------|------|-------------|
| `Employee_ID` | String | Unique ID |
| `Age` | Integer | Employee age |
| `Department` | Category | Sales / Engineering / Marketing / HR / Finance |
| `City` | Category | Mumbai / Delhi / Bangalore / Hyderabad / Chennai |
| `Experience_Yrs` | Integer | Years of experience |
| `Salary` | Float | Annual salary (₹) |
| `Performance` | Category | Excellent / Good / Average / Poor |
| `Attrition` | Binary | Yes / No |
| `Satisfaction` | Integer | Score 1–5 |
| `Projects_Done` | Integer | Number of projects completed |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Python 3.8+` | Core language |
| `Pandas` | Data loading, cleaning, analysis |
| `NumPy` | Numerical operations |
| `Matplotlib` | Data visualization |

---

## 📦 Installation & Run

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/codealpha-eda.git
cd codealpha-eda

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the EDA
python eda_analysis.py
```

---

## 📈 Key Insights Found

1. **500 employees** across **5 departments** analyzed
2. **Missing values** found in Salary (20) & Age (15) → filled with median
3. **6 salary outliers** detected (max ₹2,50,000) using IQR method
4. **Marketing** is the highest-paying department (avg ₹67,901)
5. **Sales** has the highest attrition rate (19%)
6. **Excellent performers** earn **13% more** than Average performers ✅
7. Majority of employees are aged **30–45 years**
8. **Experience vs Salary** correlation is weak (random data)

---

## 🖼️ Dashboard Preview

7 charts generated in one dashboard:
- 💰 Avg Salary by Department
- 📊 Salary Distribution (Histogram)
- 🚪 Attrition Rate by Department
- ⭐ Performance Distribution (Pie)
- 👤 Age Distribution
- 📈 Experience vs Salary (Scatter)
- 😊 Satisfaction vs Salary (Boxplot)

---

## 👤 Author

**[Your Name]**  
CodeAlpha Data Analytics Internship  
📧 [your.email@gmail.com]  
🔗 [LinkedIn Profile]

---

## 📄 License

Educational project — CodeAlpha Internship Program
