"""Statistical + LLM anomaly detection."""
import pandas as pd
import numpy as np
from typing import List, Dict


class AnomalyDetector:
    def detect(self, df: pd.DataFrame) -> List[Dict]:
        issues = []
        for col in df.columns:
            null_rate = df[col].isna().mean()
            if null_rate > 0.5:
                issues.append({"column": col, "type": "high_null_rate", "value": null_rate})
            if df[col].dtype == object and df[col].nunique() == len(df):
                issues.append({"column": col, "type": "all_unique_strings", "note": "possible ID column"})
        for col in df.select_dtypes(include=[np.number]).columns:
            z_scores = (df[col] - df[col].mean()) / (df[col].std() + 1e-8)
            outlier_count = (z_scores.abs() > 3).sum()
            if outlier_count > 0:
                issues.append({"column": col, "type": "statistical_outliers", "count": int(outlier_count)})
        return issues
