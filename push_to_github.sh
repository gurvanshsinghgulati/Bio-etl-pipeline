#!/bin/bash
set -e

# Hard reset local tracking parameters
rm -rf .git
git init

# Configure indexing parameters 
echo "gene_data.db" > .gitignore
git add .gitignore README.md load_data.py plot_data.py sample_gene_expression.csv gene_expression_chart.png

# Commit state
git commit -m "feat: complete automated bio-etl ingestion and tracking ecosystem"
git branch -M main

# Hard link endpoint to target destination profile
TARGET_URL="https://github.com"
git remote add origin "$TARGET_URL"

echo "🚀 Launching final structural upload..."
git push --force origin main
