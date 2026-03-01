#Task2

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('../db/lesson.db')

# SQL query to get order_id and total_price for each order
query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""

# Load the data into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Add cumulative column using cumsum()
df['cumulative'] = df['total_price'].cumsum()

# Create a line plot
plt.figure(figsize=(12, 6))
plt.plot(df['order_id'], df['cumulative'], marker='o', linewidth=2, markersize=5, color='steelblue')

# Add titles and labels
plt.title('Cumulative Revenue vs. Order ID', fontsize=16, fontweight='bold')
plt.xlabel('Order ID', fontsize=12, fontweight='bold')
plt.ylabel('Cumulative Revenue ($)', fontsize=12, fontweight='bold')

# Add grid for better readability
plt.grid(True, alpha=0.3, linestyle='--')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()
