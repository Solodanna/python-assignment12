import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('../db/lesson.db')

# SQL query to get employee revenue data
query = """
SELECT last_name, SUM(price * quantity) AS revenue 
FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id
"""

# Load the data into a DataFrame
employee_results = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(employee_results['last_name'], employee_results['revenue'], color='steelblue', edgecolor='navy', alpha=0.7)

# Add titles and labels
plt.title('Employee Revenue', fontsize=16, fontweight='bold')
plt.xlabel('Employee Last Name', fontsize=12, fontweight='bold')
plt.ylabel('Revenue ($)', fontsize=12, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()
