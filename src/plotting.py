from matplotlib import pyplot as plt

def build_plots(df, strat, nominal, real):
    plt.style.use('ggplot')
    ax = df.plot(kind="line", y="money_invested_total", x="date", figsize=(10, 5))
    df.plot(kind="line", y="portfolio_value", ax=ax)
    df.plot(kind="line", y="real_portfolio_value", ax=ax)
    plt.title("Portfolio Value vs Money Invested")
    if strat == "dca":
        plt.text(63, 500, f"XIRR: {nominal}%")
        plt.text(63, 0.95, f"Real XIRR: {real}%")
    elif strat == "lump":
        plt.text(62, 6500, f"CAGR: {nominal}%")
        plt.text(62, 6050, f"Real CAGR: {real}%")
    else:
        raise ValueError("Wrong value")

    plt.legend(["Money Invested", "Portfolio Value", "Real Portfolio Value"])
    plt.tight_layout()

    df.plot(kind="line", y="profit", x="date", figsize=(10, 5))
    plt.title("Profit over time")
    plt.style.use('ggplot')
    plt.legend(["Profit"])
    plt.tight_layout()

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