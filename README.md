# ICT Flux Desk • Institutional Order Flow Execution Radar

> **High-Fidelity ICT Institutional Order Flow Engine & MetaTrader 5 Bridge**  
> Covering the complete institutional taxonomy: Propulsion Blocks, Breakers, Mitigation Blocks, SMT Divergence, Optimal Trade Entry (OTE), and Volume Imbalances (VIMB).

---

### Features
* **Full ICT Institutional Taxonomy**: Not limited to single models—monitors higher-timeframe draw on liquidity, liquidity voids, displacement, and interbank dealing ranges.
* **Transparent Risk Metrics**: Every single setup displays **Stop Loss in Pips**, **Take Profit in Pips**, and **Risk-to-Reward (R:R)**.
* **Trader Autonomy**: Switch between **Limit Orders (at 50% Consequent Encroachment / OTE)** or **Market Confirmation**.
* **Dynamic Position Sizing**: Instantly maps dollar risk ($50 / $100 / $250) directly to broker lot size based on stop loss distance.
* **Direct MT5 Execution**: Integrated Python bridge connects to MetaTrader 5 to fire limit and market orders directly onto your charts.

---

### Quick Start

#### 1. Open the Interactive Visual Desk
Open `index.html` in any browser. Zero installation required. Loads in < 50ms.

#### 2. Run the Live Terminal HUD
```bash
python radar.py
```

#### 3. Execute Order on MetaTrader 5
```bash
uv run --with MetaTrader5 python mt5_bridge.py --symbol GBPUSD --type BUY_LIMIT --price 1.29420 --sl 1.29295 --tp 1.29820 --lots 0.40
```
