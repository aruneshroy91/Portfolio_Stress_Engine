## Project Structure

```text
portfolio-stress-engine/
├── data/                        # Market data (free, reproducible)
│   ├── raw/
│   │   ├── rates/               # Treasury yield curves
│   │   ├── equities/            # Equity index levels
│   │   └── volatility/          # Volatility proxies (VIX)
│   └── processed/               # Cleaned & aligned datasets
│
├── config/                      # Model & portfolio configuration
│   ├── portfolio.yaml           # Positions, notionals, instruments
│   ├── stress_config.yaml       # Scenario definitions & severities
│   └── regime_config.yaml       # Regime detection parameters
│
├── src/
│   ├── data/
│   │   └── data_loader.py       # Centralized data ingestion
│   │
│   ├── instruments/
│   │   ├── bond.py              # QuantLib-based bond definitions
│   │   └── equity.py            # Equity exposure abstraction
│   │
│   ├── valuation/
│   │   ├── curve_builder.py     # Yield curve construction (QuantLib)
│   │   └── pricing_engine.py    # Baseline & stressed valuation
│   │
│   ├── scenarios/
│   │   ├── historical.py        # Historical crisis scenarios
│   │   ├── hypothetical.py      # Forward-looking stress design
│   │   └── regime_expander.py   # Regime-aware scenario scaling
│   │
│   ├── regimes/
│   │   └── regime_detector.py   # Market regime classification
│   │
│   ├── risk/
│   │   ├── sensitivities.py     # DV01 & linear risk measures
│   │   └── pnl_decomposition.py # Linear vs non-linear loss attribution
│   │
│   ├── engine/
│   │   └── stress_engine.py     # Scenario revaluation orchestration
│   │
│   ├── reporting/
│   │   └── plots.py             # Executive-ready visualizations
│   │
│   └── main.py                  # End-to-end execution entry point
│
├── reports/
│   ├── figures/                 # Charts & heatmaps
│   └── stress_summary.pdf       # Senior management-style report
│
├── notebooks/
│   └── exploration.ipynb        # Exploratory analysis (non-core)
│
├── README.md                    # Project overview & methodology
├── requirements.txt             # Python dependencies
└── LICENSE

> QuantLib is used strictly for **curve construction and scenario-based revaluation**, 
> aligning with how stress testing is implemented in institutional risk teams.

**Design Principles**
- Configuration-driven (YAML)
- Scenario-based revaluation (not pricing models)
- Regime-aware tail risk amplification
- Capital & risk appetite focused outputs
