import pandas as pd
import matplotlib.pyplot as plt

from sp500_dca import build_sp_dca
from sp500_lump import build_sp_lump

sp_dca, cagr_dca, real_cagr_dca = build_sp_dca()
sp_lump, cagr_lump, real_cagr_lump = build_sp_lump()

sp_dca = sp_dca[["date", "portfolio_value", "real_portfolio_value"]]
sp_lump = sp_lump[["date", "portfolio_value", "real_portfolio_value"]]

comp = pd.merge(sp_dca, sp_lump, on ="date", suffixes=("_dca", "_lump"))

plt.style.use("ggplot")
ax = comp.plot(kind="line", y="portfolio_value_lump", x = "date")
comp.plot(kind="line", y="portfolio_value_dca", ax=ax)
plt.legend(["Portfolio Value (Lump Sum)", "Portfolio Value (DCA)"])
plt.title("Lump Sum Portfolio vs DCA Portfolio")
plt.tight_layout()
plt.show()

