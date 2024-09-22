import pandas as pd

class Sale:
    def __init__(self) -> None:
        self.path = 'data/Sale dataset.xlsx'

    def load(self): 
        return pd.read_excel(self.path, header=0)
    
    def clean(self, df: pd.DataFrame)-> pd.DataFrame:
        # Strip whitespaces from all column names
        df.columns = df.columns.str.strip()
        print(df.columns.tolist())
        df = df.rename(columns={'Sale ID': 'sale_id', 
                                'Date': 'date',
                                'Product': 'product',
                                'Category': 'category',
                                'Quantity': 'quantity',
                                'Price per Unit': 'price_per_unit',
                                'Revenue': 'revenue',
                                'Payment Method': 'payment_method'
                               })
        
        return df
    

sale = Sale()
df = sale.load()
df = sale.clean(df)

print(df.columns.tolist())

# Using Sale dataset:
# 1. Find the average revenue of each month.
import pandas as pd

# Assuming the DataFrame is already loaded as 'df'

# Step 1: Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Step 2: Group by month and calculate the average revenue
df['month'] = df['date'].dt.to_period('M')  # Extract month and year as 'YYYY-MM'
avg_revenue_by_month = df.groupby('month')['revenue'].mean()

# Display the result
print("Average Revenue by Month:")
print(avg_revenue_by_month)

#2. Find the total revenue of all months.
# Group by month and calculate total revenue
total_revenue_by_month = df.groupby('month')['revenue'].sum()

# Display the result
print("Total Revenue by Month:")
print(total_revenue_by_month)

# 3. Top 3 sale products (Quantity)
# Step 1: Group by 'product' and calculate the total quantity sold for each product
total_quantity_by_product = df.groupby('product')['quantity'].sum()

# Step 2: Sort the products by quantity sold in descending order
top_3_products = total_quantity_by_product.sort_values(ascending=False).head(3)

# Display the top 3 products
print("Top 3 Products by Quantity Sold:")
print(top_3_products)

#4. 3 top products which generated most revenue
# Step 1: Group by 'product' and calculate the total revenue for each product
total_revenue_by_product = df.groupby('product')['revenue'].sum()

# Step 2: Sort the products by revenue in descending order
top_3_revenue_products = total_revenue_by_product.sort_values(ascending=False).head(3)

# Display the top 3 products by revenue
print("Top 3 Products by Revenue Generated:")
print(top_3_revenue_products)

#5 Find the revenue of each payment method
# Step 1: Group by 'payment_method' and calculate the total revenue for each payment method
total_revenue_by_payment_method = df.groupby('payment_method')['revenue'].sum()

# Display the result
print("Total Revenue by Payment Method:")
print(total_revenue_by_payment_method)

#6
# Group by 'payment_method' and 'month' and calculate total revenue for each group
revenue_by_payment_and_month = df.groupby(['payment_method', 'month'])['revenue'].sum()

# Display the result
print("Revenue by Payment Method in Each Month:")
print(revenue_by_payment_and_month)

#7 top 10 products which is the ost sale
most_sold_products = df['product'].value_counts()

# Step 2: Select the top 10 most sold products
top_10_sold_products = most_sold_products.head(10)

# Display the top 10 most sold products
print("Top 10 Most Sold Products:")
print(top_10_sold_products)