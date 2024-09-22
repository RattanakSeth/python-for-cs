import pandas as pd

class BakeryStoreChain:
    def __init__(self) -> None:
        self.path = 'data/Bakery store chain dataset.xlsx'

    def load(self): 
        return pd.read_excel(self.path, header=0)
    
    def clean(self, df: pd.DataFrame)-> pd.DataFrame:
        # Strip whitespaces from all column names
        df.columns = df.columns.str.strip()
        print(df.columns.tolist())
        df = df.rename(columns={'Product': 'product', 
                                'Product Type': 'product_type',
                                'Quantity Sold': 'quantity_sold',
                                'Unit Price': 'unit_price',
                                'Revenue': 'revenue',
                                'Store Number': 'store_number',
                                'Transaction Date': 'transaction_date',
                                'Seller': 'seller',
                                'Customer': 'customer'
                               })
        
        return df
    
bakeryStore = BakeryStoreChain()
df = bakeryStore.load()
df = bakeryStore.clean(df)
print(df.columns.tolist())

total_revenue_by_product = df.groupby('product')['revenue'].sum()

#1 Find the product that generated the highest revenue
highest_revenue_product = total_revenue_by_product.idxmax()  # Product with the highest revenue
highest_revenue_amount = total_revenue_by_product.max()  # The highest revenue amount

# Display the result
print(f"The product that generated the highest revenue is: {highest_revenue_product} with a total revenue of {highest_revenue_amount:.2f}.")

#2 Which product has the highest sale quantity?
total_quantity_by_product = df.groupby('product')['quantity_sold'].sum()
# print("t: ", total_quantity_by_product)
# Find the product with the highest sale quantity
highest_quantity_product = total_quantity_by_product.idxmax()  # Product with the highest quantity sold
highest_quantity_amount = total_quantity_by_product.max()  # The highest quantity sold

# Display the result
print(f"The product with the highest sale quantity is: {highest_quantity_product} with a total quantity sold of {highest_quantity_amount}.")

#3 Who has generated the most revenue (Seller)?
total_revenue_by_seller = df.groupby('seller')['revenue'].sum()

# Find the seller with the highest total revenue
highest_revenue_seller = total_revenue_by_seller.idxmax()  # Seller with the highest revenue
highest_revenue_amount = total_revenue_by_seller.max()  # The highest revenue amount

# Display the result
print(f"The seller who generated the most revenue is: {highest_revenue_seller} with a total revenue of {highest_revenue_amount:.2f}.")

# 4. Who has bought the most (Customer)?
# Group by 'customer' and calculate the total quantity purchased by each customer
total_quantity_by_customer = df.groupby('customer')['quantity_sold'].sum()

# Find the customer who bought the most
top_customer = total_quantity_by_customer.idxmax()  # Customer with the most quantity purchased
most_quantity_purchased = total_quantity_by_customer.max()  # The total quantity purchased

# Display the result
print(f"The customer who bought the most is: {top_customer} with a total quantity of {most_quantity_purchased}.")

# 5. Who sells the highest Chocolate Chip?
# Filter the DataFrame for the 'Chocolate Chip' product
chocolate_chip_sales = df[df['product_type'].str.strip() == 'Chocolate Chip']
# print("chocolate chip ", chocolate_chip_sales)
# Group by 'seller' and calculate the total quantity sold for each seller
total_quantity_by_seller = chocolate_chip_sales.groupby('seller')['quantity_sold'].sum()
print('t quantity:', total_quantity_by_seller)
# Find the seller with the highest Chocolate Chip sales
top_seller = total_quantity_by_seller.idxmax()  # Seller with the most quantity sold
most_quantity_sold = total_quantity_by_seller.max()  # The highest quantity sold

# Display the result
print(f"The seller who sold the most Chocolate Chip is: {top_seller} with a total quantity of {most_quantity_sold}.")

# 6 Which branch generated the most revenue?
# Group by 'store_number' and calculate the total revenue for each branch
total_revenue_by_branch = df.groupby('store_number')['revenue'].sum()

# Find the branch that generated the most revenue
top_branch = total_revenue_by_branch.idxmax()  # Branch (store_number) with the highest revenue
highest_revenue = total_revenue_by_branch.max()  # The highest revenue amount

# Display the result
print(f"The branch (store_number) that generated the most revenue is: {top_branch} with a total revenue of {highest_revenue:.2f}.")