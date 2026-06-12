import pandas as pd
import matplotlib.pyplot as plt
from inflation import get_inflation_data
from etf_data import get_market_data
from pyxirr import xirr

def build_sp_dca():
    sp_dca, years = get_market_data("VUAA.L")

    sp_dca["money_invested"] = 100
    sp_dca["money_invested_total"] = sp_dca["money_invested"].cumsum()
    sp_dca["units_bought"] = 100 / sp_dca["close"]
    sp_dca["units_total"] = sp_dca["units_bought"].cumsum()
    sp_dca["portfolio_value"] = sp_dca["units_total"] * sp_dca["close"]
    sp_dca["profit"] = sp_dca["portfolio_value"] - sp_dca["money_invested_total"]

    dates = pd.to_datetime(sp_dca["date"])
    dates.iloc[-1] = pd.to_datetime("2025-12-31", format="%Y-%m-%d")

    cashflow_nominal = (sp_dca["money_invested"] * (-1)).astype(float)
    cashflow_nominal.iloc[-1] = cashflow_nominal.iloc[-1] + sp_dca["portfolio_value"].iloc[-1]
    xirr_nominal = round(xirr(dates, cashflow_nominal) * 100, 2)

    cpi = get_inflation_data()

    sp_dca["date"] = pd.to_datetime(sp_dca["date"])
    sp_dca = pd.merge_asof(sp_dca, cpi, left_on="date", right_on="observation_date", direction="nearest")
    sp_dca["date"] = sp_dca["date"].dt.year.astype(str) + "-" + sp_dca["date"].dt.month.astype(str)
    sp_dca = sp_dca.drop(columns=["observation_date", "CPIAUCSL"])
    sp_dca["real_portfolio_value"] = sp_dca["portfolio_value"] / sp_dca["inflation_factor"]

    cashflow_real = ((sp_dca["money_invested"] / sp_dca["inflation_factor"]) * (-1)).astype(float)
    cashflow_real.iloc[-1] = cashflow_real.iloc[-1] + sp_dca["real_portfolio_value"].iloc[-1]
    xirr_real = round(xirr(dates, cashflow_real) * 100, 2)

    return sp_dca, xirr_nominal, xirr_real

if __name__ == "__main__":
    sp_dca, xirr_nominal, xirr_real = build_sp_dca()

    plt.style.use('ggplot')
    ax = sp_dca.plot(kind="line", y="money_invested_total", x="date", figsize=(10, 5))
    sp_dca.plot(kind="line", y="portfolio_value", ax=ax)
    sp_dca.plot(kind="line", y="real_portfolio_value", ax=ax)
    plt.title("Portfolio Value vs Money Invested")
    plt.text(63, 500, f"XIRR: {xirr_nominal}%")
    plt.text(63, 0.95, f"Real XIRR: {xirr_real}%")
    plt.legend(["Money Invested", "Portfolio Value", "Real Portfolio Value"])
    plt.tight_layout()

    sp_dca.plot(kind="line", y="profit", x="date", figsize=(10, 5))
    plt.title("Profit over time")
    plt.style.use('ggplot')
    plt.legend(["Profit"])
    plt.tight_layout()

    sp_dca.plot(kind="line", y="units_total", x="date", figsize=(10, 5))
    plt.title("Total number of units over time")
    plt.style.use('ggplot')
    plt.legend(["Total Units"])
    plt.tight_layout()

    sp_dca.plot(kind="line", y="close", x="date", figsize=(10, 5))
    plt.title("VUAA.L ETF Value")
    plt.style.use('ggplot')
    plt.legend(["Closing Price"])
    plt.tight_layout()

    plt.show()





