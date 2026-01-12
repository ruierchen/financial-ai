import json
import pandas as pd
from llm import parse_question
from plotter import generate_trend_chart

def answer_query(question: str, df: pd.DataFrame):
    parsed = json.loads(parse_question(question))
    companies = parsed["companies"]
    metric = parsed["metric"]
    year = parsed.get("year")
    comparison = parsed["comparison"]

    filtered = df[df["company"].isin(companies)]
    if year:
        filtered = filtered[filtered["year"] == year]

    if filtered.empty:
        return {"answer": "No data found for the query."}

    if comparison and len(companies) > 1:
        chart = generate_trend_chart(filtered, metric)
        return {
            "answer": f"Comparing {metric} for {', '.join(companies)}",
            "chart": chart
        }

    value = filtered.iloc[0][metric]
    return {"answer": f"{companies[0]} {metric.replace('_', ' ')}: {value}"}
