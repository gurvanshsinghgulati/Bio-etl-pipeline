# 🧬 Bio-ETL Pipeline: Gene Expression Processing Framework

A modular, automated **Extract, Load, Transform (ELT/ETL)** pipeline architected to ingest high-throughput differential gene expression metadata, store it within a relational datastore, and generate automated diagnostic visualizations.

## 🏗️ System Architecture
The framework processes laboratory datasets through a fully decoupled three-tier architectural cycle:
1. **Extract & Clean (Data Ingestion)**: Parses raw file systems (`sample_gene_expression.csv`) using defensive coding structures to handle type transformations safely.
2. **Relational Orchestration (Storage)**: Clears obsolete indices and bulk-inserts records into a transactional, indexing-ready schema within an SQLite engine (`gene_data.db`).
3. **Transform & Analytics (Data Visualization)**: Queries analytical database layers to aggregate statistical expression trends across dynamic multi-sample metrics.

## 📊 Analytical Pipeline Insights
The pipeline computes structured aggregations down to specific biological markers:
* **Overexpression Identifiers**: Flags critical oncogenes (e.g., *EGFR* showing heightened spikes scaling above a 25.0 metric score).
* **Suppression Trackers**: Maps baseline expression properties of tumor-suppressive indicators (e.g., *PTEN* monitoring consistent structural constraints lower than a 6.5 value boundary).

## 🛠️ Deployment & Execution Setup

### 1. Environmental Infrastructure Prerequisites
Ensure dependencies are bound correctly to your runtime system environment:
```bash
pip install pandas matplotlib seaborn
```

### 2. Operational Ingestion Phase
Populate the transactional database target structures:
```bash
python3 load_data.py
```

### 3. Analytics & Figure Generation Trigger
Execute the reporting module to compile vector graphics charts:
```bash
python3 plot_data.py
```

## 📂 Repository Registry & Structural Layout
* `load_data.py` — High-efficiency CSV batch loader engine.
* `plot_data.py` — SQL analytic compiler and chart plotter script.
* `sample_gene_expression.csv` — Baseline dataset simulating multi-sample micro-array outputs.
* `gene_expression_chart.png` — Output visualization asset.
* `.gitignore` — Runtime exclusions register.
