FINANCIAL_QUERY_FUNCTION = {
    "name": "financial_query",
    "description": "Parse a financial analytics question",
    "parameters": {
        "type": "object",
        "properties": {
            "companies": {"type": "array", "items": {"type": "string"}},
            "metric": {
                "type": "string",
                "enum": ["revenue", "net_income", "operating_income"]
            },
            "year": {"type": ["integer", "null"]},
            "comparison": {"type": "boolean"}
        },
        "required": ["companies", "metric", "comparison"]
    }
}
