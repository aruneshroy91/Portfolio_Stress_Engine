# src/data/data_loader.py

import pandas as pd
from datetime import datetime
from typing import Dict

FRED_TREASURY_SERIES: Dict[str, str] = {
    "1M": "DGS1MO",
    "3M": "DGS3MO",
    "6M": "DGS6MO",
    "1Y": "DGS1",
    "2Y": "DGS2",
    "3Y": "DGS3",
    "5Y": "DGS5",
    "7Y": "DGS7",
    "10Y": "DGS10",
    "20Y": "DGS20",
    "30Y": "DGS30",
}

FRED_BASE_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv"


def _load_fred_series(
    series_id: str,
    start: datetime,
    end: datetime
) -> pd.Series:
    """Load a single FRED time series via CSV."""
    url = (
        f"{FRED_BASE_URL}"
        f"?id={series_id}"
        f"&cosd={start.strftime('%Y-%m-%d')}"
        f"&coed={end.strftime('%Y-%m-%d')}"
    )

    df = pd.read_csv(
        url,
        parse_dates=["DATE"],
        index_col="DATE"
    )

    return df[series_id]


def load_treasury_yield_curve(
    start: datetime,
    end: datetime,
    drop_na: bool = True
) -> pd.DataFrame:
    """
    Load US Treasury constant-maturity yields from FRED.

    Parameters
    ----------
    start : datetime
        Start date
    end : datetime
        End date
    drop_na : bool
        Drop rows with missing tenors

    Returns
    -------
    pd.DataFrame
        DataFrame indexed by date, columns = tenors (decimal form)
    """
    rates = {}

    for tenor, series_id in FRED_TREASURY_SERIES.items():
        rates[tenor] = _load_fred_series(series_id, start, end)

    rates = pd.DataFrame(rates)

    if drop_na:
        rates = rates.dropna(how="any")

    # Convert % → decimal
    rates /= 100.0

    return rates
