import os
from langchain_openai import ChatOpenAI
from functions import FINANCIAL_QUERY_FUNCTION

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
)

def parse_question(question: str):
    response = llm.invoke(
        messages=[{"role": "user", "content": question}],
        functions=[FINANCIAL_QUERY_FUNCTION],
        function_call={"name": "financial_query"}
    )
    return response.additional_kwargs["function_call"]["arguments"]
