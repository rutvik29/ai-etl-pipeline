"""LLM-based schema inference from raw data."""
import json
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

SCHEMA_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """You are a data engineer. Analyze this dataset sample and infer the schema.
For each column, determine: data_type, description, is_nullable, is_unique, example_values.
Return ONLY valid JSON with a "columns" array."""),
    ("human", "Dataset sample (first 5 rows):\n{sample}\n\nColumn names: {columns}\n\nInfer schema as JSON:")
])


class SchemaInferrer:
    def __init__(self, model: str = "gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model, temperature=0)
        self.chain = SCHEMA_PROMPT | self.llm

    def infer(self, df: pd.DataFrame) -> dict:
        try:
            sample = df.head(5).to_string()
            result = self.chain.invoke({"sample": sample, "columns": list(df.columns)})
            schema = json.loads(result.content)
            return schema
        except Exception as e:
            return {"columns": [{"name": c, "data_type": str(df[c].dtype), "is_nullable": df[c].isna().any()} for c in df.columns]}
