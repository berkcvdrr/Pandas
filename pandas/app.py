import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales.csv')
print(df.head())

df['total_sale'] = df['quantity'] * df['price']

product_sales = df.groupby('product')['total_sale'].sum().reset_index()
print(product_sales)

top_product = product_sales.loc[product_sales['total_sale'].idxmax()]
print(f"En çok satılan ürün: {top_product['product']} - Toplam satış: ${top_product['total_sale']}")


plt.figure(figsize=(10, 6))
plt.bar(product_sales['product'], product_sales['total_sale'], color='skyblue')
plt.title