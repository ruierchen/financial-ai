from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from data_loader import load_financial_data
from query_engine import answer_query
import pandas as pd

app = FastAPI(title="Financial Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATAFRAME: pd.DataFrame | None = None

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global DATAFRAME
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Only CSV or XLSX supported")
    DATAFRAME = load_financial_data(file)
    return {"status": "success", "rows": len(DATAFRAME)}

@app.post("/query")
async def query_financials(payload: dict):
    if DATAFRAME is None:
        raise HTTPException(status_code=400, detail="No data uploaded")
    question = payload.get("question")
    if not question:
        raise HTTPException(status_code=400, detail="Question required")
    return answer_query(question, DATAFRAME)

handler = Mangum(app)
