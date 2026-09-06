import pandas as pd

# Sales Data Analysis - Week 3
# This project demonstrates loading, exploring, cleaning, and analyzing real data.

# 1. Load the CSV file
df = pd.read_csv("sales_data.csv")

print("SALES DATA ANALYSIS")
print("=" * 45)

# 2. Display the first five rows
print("\nFirst 5 Rows:")
print(df.head())

# 3. Explore the dataset
print("\nDataset Information:")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print(f"Column Names: {list(df.columns)}")

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# 4. Convert columns to suitable data types
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

for column in ["Quantity", "Price", "Total_Sales"]:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# 5. Remove duplicate rows
duplicate_count = df.duplicated().sum()
df = df.drop_duplicates()

# 6. Handle missing values
# Median is used for numerical columns.
for column in ["Quantity", "Price", "Total_Sales"]:
    df[column] = df[column].fillna(df[column].median())

# "Unknown" is used for missing text values.
for column in ["Product", "Customer_ID", "Region"]:
    df[column] = df[column].fillna("Unknown")

# Recalculate total sales using quantity multiplied by price.
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
print(f"\nDuplicate Rows Removed: {duplicate_count}")

# 7. Calculate simple statistics and sales metrics
total_sales = df["Total_Sales"].sum()
average_sales = df["Total_Sales"].mean()
highest_sales = df["Total_Sales"].max()
lowest_sales = df["Total_Sales"].min()
total_quantity = df["Quantity"].sum()

# 8. Find the best-selling product by total revenue
product_revenue = (
    df.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

best_product = product_revenue.index[0]
best_product_revenue = product_revenue.iloc[0]

# 9. Display final results
print("\nFINAL RESULTS")
print("=" * 45)
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Average Sale: ₹{average_sales:,.2f}")
print(f"Highest Sale: ₹{highest_sales:,.2f}")
print(f"Lowest Sale: ₹{lowest_sales:,.2f}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Best-Selling Product: {best_product}")
print(f"Best Product Revenue: ₹{best_product_revenue:,.2f}")

print("\nRevenue by Product:")
print(product_revenue)

print("\nAnalysis completed successfully.")
