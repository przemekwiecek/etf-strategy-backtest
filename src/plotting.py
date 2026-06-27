import pandas as pd
from matplotlib import pyplot as plt

def build_ax_fig(title: str) -> tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    fig.set_size_inches([10, 5])
    ax.set_xlim(pd.Timestamp("2020-01-01"), pd.Timestamp("2025-12-01"))

    return fig, ax

def build_plots(df: pd.DataFrame, strat: str, nominal: float, real: float):
    plt.style.use('ggplot')
    fig, ax = build_ax_fig("Portfolio Value vs Money Invested")
    ax.plot(df["date"], df["money_invested_total"], label = "Money Invested")
    ax.plot(df["date"], df["portfolio_value"], label = "Portfolio Value")
    ax.plot(df["date"], df["real_portfolio_value"], label = "Real Portfolio Value")
    if strat == "dca":
        ax.text(pd.Timestamp("2024-12-01"), 1000, f"XIRR: {nominal}%")
        ax.text(pd.Timestamp("2024-12-01"), 500, f"Real XIRR: {real}%")
    elif strat == "lump":
        ax.text(pd.Timestamp("2024-12-01"), 6500, f"CAGR: {nominal}%")
        ax.text(pd.Timestamp("2024-12-01"), 6000, f"Real CAGR: {real}%")
    else:
        raise ValueError("Wrong value")
    ax.legend()
    plt.tight_layout()

    if strat != "lump":
        fig, ax = build_ax_fig("Profit over time")
        ax.plot(df["date"], df["profit"], label = "Profit")
        ax.set_title("Profit over time")
        ax.legend()
        plt.tight_layout()

    if strat != "lump":
        fig, ax = build_ax_fig("Total number of units over time")
        ax.plot(df["date"], df["units_total"], label="Total Units")
        ax.legend()
        plt.tight_layout()

    fig, ax = build_ax_fig("VUAA.L ETF Value")
    ax.plot(df["date"], df["close"], label="Closing Price")
    ax.legend()
    plt.tight_layout()

    plt.show()