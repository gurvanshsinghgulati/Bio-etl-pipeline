import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Read data from your database into a Pandas DataFrame
conn = sqlite3.connect("gene_data.db")
df = pd.read_sql_query("SELECT * FROM expression_data", conn)
conn.close()

# 2. Check if data was retrieved successfully
if df.empty:
    print("❌ The database table is empty. Try running load_data.py first.")
else:
    # 3. Create the bar chart
    plt.figure(figsize=(10, 5))
    sns.set_theme(style="whitegrid")
    
    sns.barplot(data=df, x="gene_name", y="expression_value", hue="sample", palette="viridis")
    
    plt.title("Bio-ETL: Gene Expression Level Analysis by Sample", fontweight='bold', fontsize=14)
    plt.xlabel("Gene Name", fontsize=12)
    plt.ylabel("Expression Metric", fontsize=12)
    plt.tight_layout()
    
    # 4. Save the figure
    plt.savefig("gene_expression_chart.png", dpi=300)
    print("📈 Success! Chart successfully saved as 'gene_expression_chart.png'")
