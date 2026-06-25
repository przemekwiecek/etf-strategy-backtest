import pandas as pd
from matplotlib import pyplot as plt

def build_plots(df, strat, nominal, real):
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    ax.plot(df["date"], df["money_invested_total"], label = "Money Invested")
    ax.plot(df["date"], df["portfolio_value"], label = "Portfolio Value")
    ax.plot(df["date"], df["real_portfolio_value"], label = "Real Portfolio Value")
    if strat == "dca":
        ax.text(pd.Timestamp("2025-02-01"), 1000, f"XIRR: {nominal}%")
        ax.text(pd.Timestamp("2025-02-01"), 500, f"Real XIRR: {real}%")
    elif strat == "lump":
        ax.text(pd.Timestamp("2024-12-01"), 6500, f"CAGR: {nominal}%")
        ax.text(pd.Timestamp("2024-12-01"), 6000, f"Real CAGR: {real}%")
    else:
        raise ValueError("Wrong value")
    ax.set_title("Portfolio Value vs Money Invested")
    ax.legend()
    fig.set_size_inches([10, 5])
    ax.set_xlim(pd.Timestamp("2020-01-01"), pd.Timestamp("2025-12-01"))
    plt.tight_layout()

    df.plot(kind="line", y="profit", x="date", figsize=(10, 5))
    plt.title("Profit over time")
    plt.style.use('ggplot')
    plt.legend(["Profit"])
    plt.tight_layout()

    if strat != "lump":
        df.plot(kind="line", y="units_total", x="date", figsize=(10, 5))
        plt.title("Total number of units over time")
        plt.style.use('ggplot')
        plt.legend(["Total Units"])
        plt.tight_layout()

    df.plot(kind="line", y="close", x="date", figsize=(10, 5))
    plt.title("VUAA.L ETF Value")
    plt.style.use('ggplot')
    plt.legend(["Closing Price"])
    plt.tight_layout()

    plt.show()