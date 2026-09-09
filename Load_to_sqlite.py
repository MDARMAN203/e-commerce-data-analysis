import sqlite3
import pandas as pd

df = pd.read_csv("ecommerce_cleaned.csv")

conn = sqlite3.connect("ecommerce.db")
df.to_sql("orders", conn, if_exists="replace", index=False)
print("Table 'orders' created in ecommerce.db")

result = pd.read_sql("""
    SELECT Category, ROUND(SUM(Sales),0) as Total_Sales, ROUND(SUM(Profit),0) as Total_Profit
    FROM orders
    GROUP BY Category
    ORDER BY Total_Sales DESC
""", conn)
print(result)

conn.close()
