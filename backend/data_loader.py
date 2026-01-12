import pandas as pd
from fastapi import UploadFile

REQUIRED_COLUMNS = {
    "company",
    "year",
    "revenue",
    "net_income",
    "operating_income"
}

def load_financial_data(file: UploadFile) -> pd.DataFrame:
    if file.filename.endswith(".csv"):
        df = pd.read_csv(file.file)
    else:
        df = pd.read_excel(file.file)

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df
