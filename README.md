# 🔄 AI ETL Pipeline

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-1C3C3C?style=flat)](https://langchain.com)
[![Airflow](https://img.shields.io/badge/Apache_Airflow-2.9-017CEE?style=flat&logo=apache-airflow)](https://airflow.apache.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **AI-powered ETL pipeline** — LLM-based schema inference, automated data cleaning, anomaly detection, and intelligent transformation suggestions for messy real-world data.

## ✨ Highlights

- 🧠 **Schema inference** — GPT-4o analyzes raw data and infers column types, relationships, constraints
- 🧹 **Auto-cleaning** — detects and fixes nulls, duplicates, outliers, format inconsistencies
- 🚨 **Anomaly detection** — statistical + LLM-based detection of data quality issues
- 🔄 **Smart transforms** — suggests and applies normalization, encoding, feature engineering
- 🗺️ **Schema mapping** — automatically maps source schemas to target schemas with confidence scores
- ✈️ **Airflow DAGs** — production-ready orchestration with retry logic and alerting

## Quick Start

```bash
git clone https://github.com/rutvik29/ai-etl-pipeline
cd ai-etl-pipeline
pip install -r requirements.txt

# Analyze and clean a CSV
python pipeline.py --source ./data/messy.csv --target ./data/clean.csv

# Infer schema
python infer_schema.py --source ./data/sample.csv
```

## License
MIT © Rutvik Trivedi
