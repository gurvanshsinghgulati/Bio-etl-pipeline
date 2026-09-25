# Bio-ETL Pipeline: Gene Expression Processing

A small ETL (Extract, Transform, Load) pipeline that loads gene expression
data from a CSV file into a SQLite database, then analyzes and visualizes
expression levels across samples.

## What it does

1. **Load** (`create_table.py`, `load_data.py`): Reads gene expression data
   from `sample_gene_expression.csv`, converts fields to the correct data
   types (integers, floats), and loads it into a SQLite database
   (`gene_data.db`). Re-running the loader clears old data first, so it can
   be safely run multiple times without creating duplicates.
2. **Analyze** (`analyze_data.py`): Calculates the average expression value
   per gene (across all samples) and flags any gene whose average exceeds
   a threshold (currently 15) as "high expression."
3. **Visualize** (`plot_data.py`): Reads the data back out with pandas and
   generates a grouped bar chart (using seaborn) comparing expression
   levels across genes and samples, saved as `gene_expression_chart.png`.

## Example output

```
Average expression per gene:
BRCA1    12.47
EGFR     22.33
KRAS     14.63
MYC      18.70
PTEN      5.47
TP53      8.80

Genes with high average expression (above 15):
⚠️ EGFR: 22.33
⚠️ MYC: 18.70
```

## Setup

```bash
pip install pandas matplotlib seaborn
```

## Usage

Run these in order:

```bash
python create_table.py    # creates the database schema
python load_data.py       # loads the CSV data into the database
python analyze_data.py    # prints average expression and flags high-expression genes
python plot_data.py       # generates the bar chart
```

## Files

- `create_table.py` — creates the `expression_data` table
- `load_data.py` — loads and cleans CSV data into the database
- `analyze_data.py` — calculates per-gene averages and flags high expression
- `plot_data.py` — generates the comparison bar chart
- `sample_gene_expression.csv` — sample dataset (6 genes x 3 samples)
- `gene_expression_chart.png` — generated chart output
- `.gitignore` — excludes the generated database file from version control

## Notes

Currently uses a small hand-crafted sample dataset. A planned next step is
to swap this for real gene expression data pulled from NCBI GEO.
