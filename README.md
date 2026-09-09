
[README_ECOMMERCE.md](https://github.com/user-attachments/files/31981573/README_ECOMMERCE.md)
# E-Commerce Sales & Profitability Analysis

## 📌 Overview
An executive dashboard analyzing global e-commerce order data (51,290 orders, 2011–2014, across 7 markets) to identify where the business drives profit — and where sales volume is not translating into profit.

---

## 🎯 Clear Business Question
> **"Which markets, categories, and shipping modes drive profit — and where are we losing money?"**

Raw sales volume can hide weak profitability. This analysis separates *how much we sell* from *how much we actually keep*, at the category and market level.

---

## 🧹 Data Cleaning & Preparation Process
The raw dataset (`Data & Resources/ECOMM DATA.xlsx`) has 4 related tables: Orders, Returns, People, and a location-mapping sheet.
1. **Missing values:** Only `Postal Code` had nulls (41,296 of 51,290 rows) — not used in any analysis, so left as-is rather than dropping otherwise-valid rows.
2. **Duplicates:** Checked the Orders table — 0 duplicate rows found.
3. **Relational join:** `Returns` only flags returns at the Order ID level (no category field), so category-level return rate was calculated by joining `Orders` to `Returns` on `Order ID`, then aggregating by `Category`.
4. **Data types:** `Order Date` / `Ship Date` were parsed as dates to support year-over-year analysis.

---

## 💡 Key Insights
*(All figures below are calculated from the full, unfiltered dataset)*

1. **Furniture has a profitability problem, not a sales problem.** Furniture generates $4.11M in sales — close to Technology's $4.74M — but converts it into only **7% profit margin**, versus **14%** for both Technology and Office Supplies. Furniture is roughly half as profitable per dollar sold as the other two categories.
2. **Consistent, strong profit growth year over year.** Profit grew from $249K (2011) to $504K (2014) — **+23.5% in 2012, +32.4% in 2013, +23.9% in 2014.** Growth is accelerating, not just recovering.
3. **EMEA is a volume market, not a profit market.** EMEA generates $806K in sales but only a **5% margin** — the lowest of all 7 markets — while Canada, despite tiny sales volume ($67K), runs the highest margin (27%).
4. **Return rates are fairly close across categories** (5.7%–6.5%), so returns are not the main driver of Furniture's weak margin — the issue is more likely pricing/discounting or cost structure, worth investigating further.
5. **Standard Class shipping dominates volume** (~60% of sales) — most customers are not paying for speed, so shipping-cost efficiency on Standard Class has outsized impact on overall margin.

---

## 🚀 Actionable Recommendations
* **Audit Furniture pricing and discounting.** At 7% margin on $4.1M in sales, even a small improvement in discount policy or supplier cost would meaningfully lift overall profit.
* **Re-evaluate EMEA strategy.** A 5% margin market may not be worth the same investment as APAC or EU, which carry 12–13% margins on far larger sales.
* **Protect Standard Class shipping efficiency.** Since most volume ships Standard Class, even small per-order shipping cost increases here erode margin at scale.

---

## 🛠️ Tech Stack & Tools Used
* **Python** (pandas) — data cleaning, table joins, and verification of all figures above (`analysis.py`)
* **SQL** (SQLite) — business-question queries (`analysis_queries.sql`)
* **Power BI** — executive dashboard (`E-Commerce Data Analysis.pbix`)

---

## ▶️ How to Run
1. `python analysis.py` — cleans the data, joins Orders with Returns, and prints/saves all the figures used in the Key Insights above
2. `python load_to_sqlite.py` — loads the cleaned data into a local SQLite database
3. Run `analysis_queries.sql` against the database to reproduce the category/market/return-rate breakdowns
4. Open `E-Commerce Data Analysis.pbix` in Power BI to view the dashboard

---

## 📁 Project Structure
```
data/ECOMM DATA.xlsx                          ← raw dataset (Orders, Returns, People)
analysis.py                                   ← Step 1: cleaning + join + insight calculations
load_to_sqlite.py                             ← Step 2: loads cleaned data into SQLite
analysis_queries.sql                          ← Step 3: SQL business-question queries
E-Commerce Data Analysis.pbix                 ← Power BI dashboard
E-Commerce Data Analysis_page.jpg             ← dashboard screenshot
```


