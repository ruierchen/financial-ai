import matplotlib.pyplot as plt
import io
import base64
import pandas as pd

def generate_trend_chart(df: pd.DataFrame, metric: str):
    fig, ax = plt.subplots()
    for company in df["company"].unique():
        subset = df[df["company"] == company]
        ax.plot(subset["year"], subset[metric], label=company)

    ax.set_xlabel("Year")
    ax.set_ylabel(metric.replace("_", " ").title())
    ax.legend()
    ax.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")
