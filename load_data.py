import csv
import sqlite3

def load_data():
    conn = sqlite3.connect("gene_data.db")
    cursor = conn.cursor()
    
    # Clean out any old remaining entries before loading
    cursor.execute("DELETE FROM expression_data")
    
    with open("sample_gene_expression.csv", "r") as f:
        reader = csv.DictReader(f)
        rows_inserted = 0
        
        for r in reader:
            cursor.execute(
                "INSERT INTO expression_data VALUES (?, ?, ?, ?, ?)",
                (int(r['gene_id']), r['gene_name'], int(r['chromosome']), r['sample'], float(r['expression_value']))
            )
            rows_inserted += 1
            
    conn.commit()
    conn.close()
    print(f"📥 Success! Ingested {rows_inserted} rows into your database.")

if __name__ == "__main__":
    load_data()




