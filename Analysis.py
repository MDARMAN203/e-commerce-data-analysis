import pandas as pd

xl = pd.ExcelFile("Data & Resources/ECOMM DATA.xlsx")
orders = xl.parse("Orders")
returns = xl.parse("Returns")

print("Shape:", orders.shape)

print("\nNulls per column:")
print(orders.isnull().sum()[orders.isnull().sum() > 0])

print("\nDuplicate rows:", orders.duplicated().sum())

total_sales = orders["Sales"].sum()
total_profit = orders["Profit"].sum()
margin = total_profit / total_sales * 100
print(f"\nTotal Sales: ${total_sales/1e6:.2f}M")
print(f"Total Profit: ${total_profit/1e3:.2f}K")
print(f"Profit Margin: {margin:.2f}%")

cat_stats = orders.groupby("Category").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
cat_stats["Margin_%"] = (cat_stats["Profit"] / cat_stats["Sales"] * 100).round(2)
print("\nCategory Sales / Profit / Margin:")
print(cat_stats.round(0))

market_stats = orders.groupby("Market").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
market_stats["Margin_%"] = (market_stats["Profit"] / market_stats["Sales"] * 100).round(2)
print("\nMarket Sales / Profit / Margin:")
print(market_stats.sort_values("Sales", ascending=False).round(0))

orders["Year"] = orders["Order Date"].dt.year
yoy = orders.groupby("Year")["Profit"].sum()
print("\nProfit by Year:")
print(yoy.round(0))
print("\nYoY % Growth:")
print(yoy.pct_change().round(3) * 100)

merged = orders.merge(returns, on="Order ID", how="left")
merged["Returned"] = merged["Returned"].fillna("No")
return_rate = merged.groupby("Category")["Returned"].apply(lambda x: (x == "Yes").mean() * 100)
print("\nReturn Rate by Category (%):")
print(return_rate.round(2))

ship_stats = orders.groupby("Ship Mode")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Ship Mode:")
print(ship_stats.round(0))

merged.to_csv("ecommerce_cleaned.csv", index=False)
print("\nSaved: ecommerce_cleaned.csv")
