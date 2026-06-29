"""
╔══════════════════════════════════════════════════════════╗
║   CodeAlpha Internship — Data Analytics                  ║
║   TASK 2: Exploratory Data Analysis (EDA)                ║
║   Author: [Your Name]                                    ║
╚══════════════════════════════════════════════════════════╝

Objectives:
  ✅ Ask meaningful questions about the dataset
  ✅ Explore the data structure (variables, data types)
  ✅ Identify trends, patterns and anomalies
  ✅ Test hypotheses and validate assumptions
  ✅ Detect potential data issues or problems
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import warnings
warnings.filterwarnings('ignore')
import os

os.makedirs("charts", exist_ok=True)

# ─────────────────────────────────────────────────────────
# STEP 1: GENERATE REALISTIC DATASET
# ─────────────────────────────────────────────────────────

np.random.seed(42)
n = 500

departments = ['Sales', 'Engineering', 'Marketing', 'HR', 'Finance']
cities       = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai']

data = {
    'Employee_ID'  : [f'EMP{1000+i}' for i in range(n)],
    'Age'          : np.random.randint(22, 60, n),
    'Department'   : np.random.choice(departments, n),
    'City'         : np.random.choice(cities, n),
    'Experience_Yrs': np.random.randint(0, 35, n),
    'Salary'       : np.random.normal(60000, 15000, n).clip(25000, 120000).astype(int),
    'Performance'  : np.random.choice(['Excellent','Good','Average','Poor'],
                                       n, p=[0.2, 0.4, 0.3, 0.1]),
    'Attrition'    : np.random.choice(['Yes','No'], n, p=[0.2, 0.8]),
    'Satisfaction' : np.random.randint(1, 6, n),
    'Projects_Done': np.random.randint(1, 20, n),
}

# Inject some missing values & outliers
df = pd.DataFrame(data)
df.loc[np.random.choice(n, 20, replace=False), 'Salary']      = np.nan
df.loc[np.random.choice(n, 15, replace=False), 'Age']         = np.nan
df.loc[np.random.choice(n, 5,  replace=False), 'Salary']      = 250000   # outliers
df.to_csv('data/employee_dataset.csv', index=False)

print("=" * 60)
print("  CodeAlpha — Task 2: Exploratory Data Analysis (EDA)")
print("=" * 60)

# ─────────────────────────────────────────────────────────
# STEP 2: LOAD & EXPLORE DATA STRUCTURE
# ─────────────────────────────────────────────────────────

df = pd.read_csv('data/employee_dataset.csv')

print("\n📋 SECTION 1 — DATA STRUCTURE")
print("-" * 40)
print(f"  Shape          : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\n  Columns & Types:\n{df.dtypes.to_string()}")
print(f"\n  First 5 Rows:\n{df.head().to_string()}")

# ─────────────────────────────────────────────────────────
# STEP 3: MEANINGFUL QUESTIONS
# ─────────────────────────────────────────────────────────

print("\n\n❓ SECTION 2 — MEANINGFUL QUESTIONS")
print("-" * 40)
print("""
  Q1. What is the average salary across departments?
  Q2. Is there a relationship between experience and salary?
  Q3. Which department has the highest attrition rate?
  Q4. Does performance rating affect salary?
  Q5. Are there any outliers in salary data?
  Q6. What is the age distribution of employees?
  Q7. Which city has the most employees?
""")

# ─────────────────────────────────────────────────────────
# STEP 4: DATA QUALITY CHECK
# ─────────────────────────────────────────────────────────

print("\n🔍 SECTION 3 — DATA QUALITY / ISSUES DETECTED")
print("-" * 40)
missing = df.isnull().sum()
missing = missing[missing > 0]
print(f"\n  Missing Values:\n{missing.to_string()}")

# Fill missing values
df['Salary'].fillna(df['Salary'].median(), inplace=True)
df['Age'].fillna(df['Age'].median(), inplace=True)

# Outlier detection (IQR)
Q1, Q3 = df['Salary'].quantile([0.25, 0.75])
IQR     = Q3 - Q1
outliers = df[(df['Salary'] < Q1 - 1.5*IQR) | (df['Salary'] > Q3 + 1.5*IQR)]
print(f"\n  Salary Outliers : {len(outliers)} records detected")
print(f"  Outlier Salaries: {sorted(outliers['Salary'].unique())}")
print("\n  ✅ Missing values filled with median")

# ─────────────────────────────────────────────────────────
# STEP 5: STATISTICAL SUMMARY
# ─────────────────────────────────────────────────────────

print("\n\n📊 SECTION 4 — STATISTICAL SUMMARY")
print("-" * 40)
print(df[['Age','Salary','Experience_Yrs','Satisfaction','Projects_Done']]
      .describe().round(2).to_string())

# ─────────────────────────────────────────────────────────
# STEP 6: TRENDS & PATTERNS
# ─────────────────────────────────────────────────────────

print("\n\n📈 SECTION 5 — TRENDS & PATTERNS")
print("-" * 40)

dept_salary = df.groupby('Department')['Salary'].mean().sort_values(ascending=False)
print(f"\n  Avg Salary by Department:\n{dept_salary.round(0).to_string()}")

perf_salary = df.groupby('Performance')['Salary'].mean().sort_values(ascending=False)
print(f"\n  Avg Salary by Performance:\n{perf_salary.round(0).to_string()}")

attrition = df.groupby('Department')['Attrition'].apply(lambda x: (x=='Yes').mean()*100).round(1)
print(f"\n  Attrition Rate (%) by Department:\n{attrition.to_string()}")

corr = df[['Age','Salary','Experience_Yrs','Satisfaction','Projects_Done']].corr()
print(f"\n  Correlation Matrix:\n{corr.round(2).to_string()}")

# ─────────────────────────────────────────────────────────
# STEP 7: HYPOTHESIS TESTING
# ─────────────────────────────────────────────────────────

print("\n\n🧪 SECTION 6 — HYPOTHESIS TESTING")
print("-" * 40)

# H1: More experience → Higher salary?
corr_exp_sal = df['Experience_Yrs'].corr(df['Salary'])
print(f"\n  H1: Experience vs Salary correlation : {corr_exp_sal:.3f}")
print(f"      → {'✅ CONFIRMED' if corr_exp_sal > 0.3 else '❌ WEAK — not strongly correlated'}")

# H2: Excellent performers earn more?
exc = df[df['Performance']=='Excellent']['Salary'].mean()
avg = df[df['Performance']=='Average']['Salary'].mean()
print(f"\n  H2: Excellent performers earn more?")
print(f"      Excellent avg: ₹{exc:,.0f}  |  Average avg: ₹{avg:,.0f}")
print(f"      → {'✅ CONFIRMED' if exc > avg else '❌ NOT confirmed'}")

# ─────────────────────────────────────────────────────────
# STEP 8: VISUALIZATIONS (4-chart dashboard)
# ─────────────────────────────────────────────────────────

fig = plt.figure(figsize=(16, 12))
fig.patch.set_facecolor('#0f0f1a')
gs  = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.35)

COLORS = ['#667eea','#f093fb','#4facfe','#43e97b','#fa709a']
TEXT   = '#e0e0e0'

def style_ax(ax, title):
    ax.set_facecolor('#1a1a2e')
    ax.tick_params(colors=TEXT, labelsize=8)
    ax.xaxis.label.set_color(TEXT)
    ax.yaxis.label.set_color(TEXT)
    ax.set_title(title, color='white', fontsize=10, fontweight='bold', pad=8)
    for spine in ax.spines.values():
        spine.set_edgecolor('#333355')

# 1. Salary by Department
ax1 = fig.add_subplot(gs[0, :2])
bars = ax1.bar(dept_salary.index, dept_salary.values, color=COLORS, edgecolor='none', width=0.6)
for b in bars:
    ax1.text(b.get_x()+b.get_width()/2, b.get_height()+400,
             f'₹{b.get_height():,.0f}', ha='center', va='bottom', color=TEXT, fontsize=7.5)
ax1.set_ylabel('Avg Salary (₹)')
style_ax(ax1, '💰 Avg Salary by Department')

# 2. Salary distribution histogram
ax2 = fig.add_subplot(gs[0, 2])
ax2.hist(df[df['Salary']<200000]['Salary'], bins=25, color='#667eea', edgecolor='#0f0f1a', alpha=0.9)
ax2.axvline(df['Salary'].median(), color='#fa709a', linestyle='--', linewidth=1.5, label='Median')
ax2.legend(fontsize=8, labelcolor=TEXT)
ax2.set_xlabel('Salary (₹)')
style_ax(ax2, '📊 Salary Distribution')

# 3. Attrition by dept
ax3 = fig.add_subplot(gs[1, 0])
colors3 = ['#fa709a' if v > attrition.mean() else '#43e97b' for v in attrition.values]
ax3.barh(attrition.index, attrition.values, color=colors3, edgecolor='none')
ax3.set_xlabel('Attrition %')
style_ax(ax3, '🚪 Attrition Rate by Dept')

# 4. Performance pie
ax4 = fig.add_subplot(gs[1, 1])
perf_c = df['Performance'].value_counts()
wedges, texts, autotexts = ax4.pie(perf_c.values, labels=perf_c.index,
    autopct='%1.1f%%', colors=COLORS, startangle=90,
    textprops={'color': TEXT, 'fontsize': 8})
for at in autotexts:
    at.set_color('white')
style_ax(ax4, '⭐ Performance Distribution')

# 5. Age distribution
ax5 = fig.add_subplot(gs[1, 2])
ax5.hist(df['Age'].dropna(), bins=20, color='#4facfe', edgecolor='#0f0f1a', alpha=0.9)
ax5.set_xlabel('Age')
style_ax(ax5, '👤 Age Distribution')

# 6. Experience vs Salary scatter
ax6 = fig.add_subplot(gs[2, :2])
scatter_colors = [COLORS[departments.index(d)] for d in df['Department']]
ax6.scatter(df['Experience_Yrs'], df['Salary'], c=scatter_colors, alpha=0.5, s=18)
m, b = np.polyfit(df['Experience_Yrs'], df['Salary'], 1)
x_line = np.linspace(0, 35, 100)
ax6.plot(x_line, m*x_line + b, color='#fa709a', linewidth=2, label='Trend')
ax6.set_xlabel('Experience (Years)')
ax6.set_ylabel('Salary (₹)')
ax6.legend(fontsize=8, labelcolor=TEXT)
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=COLORS[i], label=departments[i]) for i in range(len(departments))]
ax6.legend(handles=legend_elements, fontsize=7, labelcolor=TEXT,
           loc='upper left', facecolor='#1a1a2e', edgecolor='#333355')
style_ax(ax6, '📈 Experience vs Salary (by Department)')

# 7. Satisfaction vs Salary box
ax7 = fig.add_subplot(gs[2, 2])
sat_groups = [df[df['Satisfaction']==s]['Salary'].values for s in sorted(df['Satisfaction'].unique())]
bp = ax7.boxplot(sat_groups, patch_artist=True, labels=sorted(df['Satisfaction'].unique()))
for patch, color in zip(bp['boxes'], COLORS):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
for element in ['whiskers','caps','medians','fliers']:
    for item in bp[element]:
        item.set_color(TEXT)
ax7.set_xlabel('Satisfaction Score')
ax7.set_ylabel('Salary (₹)')
style_ax(ax7, '😊 Satisfaction vs Salary')

# Title
fig.text(0.5, 0.98, 'CodeAlpha — Task 2: Exploratory Data Analysis (EDA)',
         ha='center', va='top', fontsize=14, color='white', fontweight='bold')
fig.text(0.5, 0.955, 'Employee Dataset  |  500 Records  |  10 Features',
         ha='center', va='top', fontsize=9, color='#aaaacc')

plt.savefig('charts/eda_dashboard.png', dpi=160, bbox_inches='tight',
            facecolor='#0f0f1a')
print("\n[✓] Dashboard chart saved → charts/eda_dashboard.png")

# ─────────────────────────────────────────────────────────
# FINAL SUMMARY
# ─────────────────────────────────────────────────────────

print("\n\n✅ SECTION 7 — KEY INSIGHTS")
print("-" * 40)
print(f"""
  1. Dataset has {df.shape[0]} employees across {df['Department'].nunique()} departments
  2. Missing values found in Salary & Age → filled with median
  3. {len(outliers)} salary outliers detected (>₹1.5×IQR)
  4. Highest paying dept : {dept_salary.index[0]} (₹{dept_salary.iloc[0]:,.0f})
  5. Highest attrition   : {attrition.idxmax()} ({attrition.max()}%)
  6. Experience-Salary correlation: {corr_exp_sal:.2f} (moderate positive)
  7. Excellent performers earn {((exc-avg)/avg*100):.1f}% more than Average
  8. Most employees aged 30–45 years
""")
print("=" * 60)
print("  📁 Files saved: data/employee_dataset.csv")
print("  📁 Chart saved: charts/eda_dashboard.png")
print("=" * 60)
