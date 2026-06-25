import pandas as pd
from inflation import get_inflation_data
from etf_data import get_market_data
from plotting import build_plots

def build_sp_lump():
    sp_lump, years = get_market_data("VUAA.L")

    sp_lump["money_invested_total"] = 7200
    sp_lump["units_bought"] = sp_lump["money_invested_total"] / sp_lump.iloc[0, 1]
    sp_lump["units_total"] = sp_lump["units_bought"]
    sp_lump["portfolio_value"] = sp_lump["units_total"] * sp_lump["close"]
    sp_lump["profit"] = sp_lump["portfolio_value"] - sp_lump["money_invested_total"]

    cagr = round(((sp_lump["portfolio_value"].iloc[-1] / sp_lump["money_invested_total"].iloc[-1]) ** (1 / years) - 1) * 100, 2)

    cpi = get_inflation_data()

    sp_lump["date"] = pd.to_datetime(sp_lump["date"])
    sp_lump = pd.merge_asof(sp_lump, cpi, left_on="date", right_on="observation_date", direction="nearest")
    sp_lump["date"] = sp_lump["date"].dt.year.astype(str) + "-" + sp_lump["date"].dt.month.astype(str)
    sp_lump = sp_lump.drop(columns=["observation_date", "CPIAUCSL"])
    sp_lump["real_portfolio_value"] = sp_lump["portfolio_value"] / sp_lump["inflation_factor"]

    real_cagr = round(((sp_lump["real_portfolio_value"].iloc[-1] / sp_lump["money_invested_total"].iloc[-1]) ** (1 / years) - 1) * 100, 2)

    return sp_lump, cagr, real_cagr,


if __name__ == "__main__":
    sp_lump, cagr, real_cagr = build_sp_lump()

    build_plots(sp_lump, "lump", cagr, real_cagr)






