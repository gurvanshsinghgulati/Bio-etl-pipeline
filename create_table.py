import sqlite3

connection = sqlite3.connect("gene_data.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expression_data (
    gene_id INTEGER,
    gene_name TEXT,
    chromosome INTEGER,
    sample TEXT,
    expression_value REAL
    
     
)
""")

connection.commit()
connection.close()

print("Table created successfully.")
