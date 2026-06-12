# Portfolio Performance Backtest

In this project I have backtested two portfolios with two different investment strategies. 
Both portfolios are fully based on the VUAA.L exchange-traded fund, using price history from Yahoo Finance. 
The data is wrangled to make it suitable for analysis and visualization.

**"DCA Strategy" Portfolio** — This portfolio uses a dollar-cost averaging strategy in order to minimize the average price per unit. 
For the backtest, I decided to base this strategy on regular monthly investments of 100 USD. I used XIRR as the rate of return indicator, since it is the most accurate when there are multiple deposits over a fixed period of time.

**"Lump Sum Strategy" Portfolio** — This strategy follows a simple idea: a single deposit of 7200 USD at the beginning. Also, I have calculated the rate of return with CAGR.

For both, I have included portfolio value with and without the influence of inflation (US CPI). The data about inflation comes from the Federal Reserve Economic Data (FRED) database.

Backtest period: 2020-01-01 – 2025-12-31
