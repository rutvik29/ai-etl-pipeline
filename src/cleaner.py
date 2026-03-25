"""Automated data cleaner based on inferred schema."""
import pandas as pd
import numpy as np
from typing import Dict, Any


class DataCleaner:
    def __init__(self, schema: Dict[str, Any] = None):
        self.schema = schema or {}

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df = df.drop_duplicates()
        for col in df.columns:
            if df[col].dtype == object:
                df[col] = df[col].str.strip()
                df[col] = df[col].replace("", np.nan)
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            q1, q3 = df[col].quantile(0.25), df[col].quantile(0.75)
            iqr = q3 - q1
            lower, upper = q1 - 3 * iqr, q3 + 3 * iqr
            df[col] = df[col].clip(lower, upper)
        return df
