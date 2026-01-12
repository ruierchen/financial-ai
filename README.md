# 💰 Financial Chatbot

A AI-powered financial analytics chatbot that lets users query company financial data using natural language.

---

## 🚀 Features

- Natural language financial Q&A
- LangChain + OpenAI Function Calling
- CSV / Excel ingestion
- Automatic trend visualization
- FastAPI backend (EC2 + Lambda compatible)
- React frontend (Vercel-ready)
- Secure API key handling

---

## 🧠 Architecture
```text
React (Vercel)
↓
FastAPI (EC2 / Lambda)
↓
LangChain → OpenAI
↓
Pandas + Matplotlib
```
---
## Deployment

The backend is implemented with **FastAPI** and supports multiple deployment strategies:

- **AWS Lambda + API Gateway** using **Mangum** for serverless execution
- **AWS EC2** using **Uvicorn** for long-running and compute-intensive workloads

The same codebase is used for both deployment options without modification to business logic.

### AWS EC2 (Uvicorn)

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
---

## ⚙️ Running Locally

### Backend
```bash
cd backend
cp .env.example .env
pip install -r requirements.txt
uvicorn app:app --reload

cd frontend
npm install
```
---

## 🛠 Troubleshooting
```text
“No data uploaded”

You must upload file first via UI or /upload.

“Missing columns”

Your uploaded file must contain required schema:
company, year, revenue, net_income, operating_income

“OpenAI API key not found”

Make sure:
	•	backend/.env exists
	•	OPENAI_API_KEY is set
	•	you started backend from backend/ directory (so env loads correctly if you add dotenv later)
```
---

## 🚧 Future Improvements
```text
Persist uploaded data:
	•	store in S3 + DynamoDB/Postgres
User sessions / multi-tenant:
	•	auth + per-user datasets
Caching:
	•	cache parsed queries & computed results
Observability:
	•	structured logging, tracing, metrics
```
