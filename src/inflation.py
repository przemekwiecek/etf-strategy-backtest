import pandas as pd

def get_inflation_data() -> pd.DataFrame:
    cpi = pd.read_csv("CPIAUCSL.csv")
    cpi["observation_date"] = pd.to_datetime(cpi["observation_date"])
    cpi = cpi[cpi["observation_date"] >= "2020-01-01"]
    cpi["CPIAUCSL"] = cpi["CPIAUCSL"].ffill()
    cpi_base = cpi.iloc[0, 1]
    cpi["inflation_factor"] = cpi["CPIAUCSL"] / cpi_base

    return cpi

