SELECT
    Category,
    ROUND(SUM(Sales), 0) AS Total_Sales,
    ROUND(SUM(Profit), 0) AS Total_Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Margin_Pct
FROM orders
GROUP BY Category
ORDER BY Total_Sales DESC;

SELECT
    Market,
    ROUND(SUM(Sales), 0) AS Total_Sales,
    ROUND(SUM(Profit), 0) AS Total_Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2) AS Margin_Pct
FROM orders
GROUP BY Market
ORDER BY Total_Sales DESC;

SELECT
    Category,
    COUNT(*) AS Total_Line_Items,
    SUM(CASE WHEN Returned = 'Yes' THEN 1 ELSE 0 END) AS Returned_Items,
    ROUND(SUM(CASE WHEN Returned = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS Return_Rate_Pct
FROM orders
GROUP BY Category;

SELECT
    strftime('%Y', "Order Date") AS Order_Year,
    ROUND(SUM(Profit), 0) AS Total_Profit
FROM orders
GROUP BY Order_Year
ORDER BY Order_Year;

SELECT
    "Ship Mode",
    ROUND(SUM(Sales), 0) AS Total_Sales,
    ROUND(SUM(Sales) * 100.0 / (SELECT SUM(Sales) FROM orders), 2) AS Pct_Of_Total
FROM orders
GROUP BY "Ship Mode"
ORDER BY Total_Sales DESC;
