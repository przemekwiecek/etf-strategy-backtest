# Portfolio Performance Backtest

In this project I have backtested two portfolios with two different investment strategies. 
Both portfolios are fully based on the VUAA.L exchange-traded fund, using price history from Yahoo Finance. 
The data is wrangled to make it suitable for analysis and visualization.

## Portfolios

**"DCA Strategy" Portfolio** — This portfolio uses a dollar-cost averaging strategy in order to minimize the average price per unit. 
For the backtest, I decided to base this strategy on regular monthly investments of 100 USD. I used XIRR as the rate of return indicator, since it is the most accurate when there are multiple deposits over a fixed period of time.

**"Lump Sum Strategy" Portfolio** — This strategy follows a simple idea: a single deposit of 7200 USD at the beginning. Also, I have calculated the rate of return with CAGR.

For both, I have included portfolio value with and without the influence of inflation (US CPI). The data about inflation comes from the Federal Reserve Economic Data (FRED) database.

Backtest period: 2020-01-01 – 2025-12-31

## Project Structure

`etf_data.py` - Downloads price data for the selected ticker from Yahoo Finance using yfinance, then extracts and formats the most important data using pandas.

`inflation.py` - Reads the _CPIAUCSL.csv_ file containing inflation data and formats it properly.

`sp500_dca.py` - Uses the data from _market_data.py_, adds columns and calculates values to backtest the DCA strategy. The main dataframe is merged with data from _inflation.py_ to calculate real (inflation-adjusted) values. It uses the pyxirr library to compute the XIRR indicator. 

`sp500_lump.py` - Has a similar structure to _sp500_dca.py_, but instead of XIRR it calculates the CAGR using the standard formula.

`plotting.py` - Using Matplotlib library, the script visualises the output.

`comparison.py` - Combines the data from both strategies and visualizes it on a single graph.
