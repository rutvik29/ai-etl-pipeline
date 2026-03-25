"""AI ETL pipeline entry point."""
import argparse
import pandas as pd
from src.schema_inference import SchemaInferrer
from src.cleaner import DataCleaner
from src.anomaly import AnomalyDetector


def run_pipeline(source: str, target: str):
    print(f"Loading {source}...")
    df = pd.read_csv(source)
    print(f"Shape: {df.shape}")

    print("Inferring schema...")
    inferrer = SchemaInferrer()
    schema = inferrer.infer(df)
    print(f"Schema: {schema}")

    print("Detecting anomalies...")
    detector = AnomalyDetector()
    issues = detector.detect(df)
    print(f"Issues found: {len(issues)}")

    print("Cleaning data...")
    cleaner = DataCleaner(schema=schema)
    df_clean = cleaner.clean(df)

    df_clean.to_csv(target, index=False)
    print(f"Saved cleaned data to {target} ({len(df_clean)} rows)")
    return df_clean


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    run_pipeline(args.source, args.target)
