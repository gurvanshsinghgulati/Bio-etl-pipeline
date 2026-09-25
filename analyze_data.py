import sqlite3
import pandas as pd

conn = sqlite3.connect("gene_data.db")
df = pd.read_sql_query("SELECT * FROM expression_data", conn)
conn.close()

average_expression = df.groupby("gene_name")["expression_value"].mean()
print(average_expression)

threshold = 15
print("\nGenes with high average expression (above " , threshold, "):")

for gene, value in average_expression.items():
    if value > threshold:
        print(f" {gene}:{value:.2f}")
