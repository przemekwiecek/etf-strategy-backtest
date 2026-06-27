import pandas as pd
import yfinance as yf

def get_market_data(ticker: str) -> tuple[pd.DataFrame, float] :
    df = yf.download(ticker, start="2020-01-01", end="2025-12-31")
    df.columns = df.columns.droplevel(1)
    df.columns.name = None

    df = df[["Close"]]
    df = df.resample('MS').first()
    df = df.reset_index()
    df = df.rename(columns={"Date": "date", "Close": "close"})
    years = len(df)/12
    df["date"] = df["date"].dt.year.astype(str) + "-" + df["date"].dt.month.astype(str)

    return df, years