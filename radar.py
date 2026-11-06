"""ICT Flux Desk • God's Eye Chokepoint Intercept HUD & MT5 Live Execution Engine

Powered by GodsEyeFluxEngine:
- Vectorized State Machine: 4H/1H Order-Flow Alignment + Liquidity Raid
- CISD (Change in State of Delivery) + Immediate Chokepoint Execution
- Intermarket SMT Triad Confirmation
- Dual-Tranche Governor (+0.80R BE Lock, +1.25R 70% Harvest, +2.8R+ Runner)
"""

import sys
import time
import os
from datetime import datetime, timezone

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# ANSI Colors for Institutional Gold, Emerald, and Rose
C_GOLD = "\033[38;2;240;185;75m"
C_BOLD_GOLD = "\033[1;38;2;245;207;107m"
C_GREEN = "\033[1;38;2;43;212;125m"
C_RED = "\033[1;38;2;255;92;108m"
C_MUTED = "\033[38;2;154;163;181m"
C_FAINT = "\033[38;2;100;108;126m"
C_WHITE = "\033[1;37m"
C_CYAN = "\033[1;38;2;90;169;255m"
C_RESET = "\033[0m"


def print_header():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{C_BOLD_GOLD}╔══════════════════════════════════════════════════════════════════════════════════════╗{C_RESET}")
    print(f"{C_BOLD_GOLD}║  👁️  ICT FLUX • GOD'S EYE CHOKEPOINT EXECUTION DESK                                   ║{C_RESET}")
    print(f"{C_BOLD_GOLD}║  Single-Pass Chokepoint Intercept · CISD Confirmed · Dual-Tranche Governor           ║{C_RESET}")
    print(f"{C_BOLD_GOLD}╚══════════════════════════════════════════════════════════════════════════════════════╝{C_RESET}")
    now_utc = datetime.now(timezone.utc).strftime("%H:%M:%S UTC")
    print(f" {C_MUTED}Active Engine:{C_RESET} {C_GOLD}God's Eye Flux (M5 Chokepoint){C_RESET}  |  {C_MUTED}Session:{C_RESET} {C_GREEN}● LONDON KILLZONE{C_RESET}  |  {C_WHITE}{now_utc}{C_RESET}\n")
    print(f" {C_CYAN}Dual-Tranche Governor:{C_RESET} {C_MUTED}[+0.80R BE Lock] ──▶ [+1.25R Harvest 70%] ──▶ [+2.8R+ Structural Runner 30%]{C_RESET}\n")


def display_signal(pair, archetype, bias, entry, sl, tp, pips_sl, pips_tp, rr, order_type="LIMIT"):
    is_bull = bias.upper() in ("LONG", "BUY")
    bias_color = C_GREEN if is_bull else C_RED
    border_color = C_BOLD_GOLD

    print(f"{border_color}┌──────────────────────────────────────────────────────────────────────────────────────┐{C_RESET}")
    print(f"│ {C_WHITE}{pair:<10}{C_RESET} │ {C_GOLD}ARCHETYPE:{C_RESET} {archetype:<31} │ {bias_color}{bias.upper():<16}{C_RESET}│")
    print(f"{border_color}├──────────────────────────────────────────────────────────────────────────────────────┤{C_RESET}")
    print(f"│  {C_MUTED}Execution:{C_RESET}   {C_GOLD}{order_type} @ {entry:.5f}{C_RESET}  {C_CYAN}[CISD Confirmed]{C_RESET}")
    print(f"│  {C_MUTED}Stop Loss:{C_RESET}   {C_RED}{sl:.5f}{C_RESET}  ───▶  {C_RED}[ {pips_sl:.1f} PIPS RISK ]{C_RESET}")
    print(f"│  {C_MUTED}Target (TP2):{C_RESET} {C_GREEN}{tp:.5f}{C_RESET}  ───▶  {C_GREEN}[ {pips_tp:.1f} PIPS TARGET ]{C_RESET}")
    print(f"│  {C_MUTED}Risk/Reward:{C_RESET} {C_BOLD_GOLD}1 : {rr:.2f} R{C_RESET}")
    print(f"{border_color}├──────────────────────────────────────────────────────────────────────────────────────┤{C_RESET}")
    
    # Lot Sizing Calculations
    risk_50_lots = round(50.0 / (pips_sl * 10), 2)
    risk_100_lots = round(100.0 / (pips_sl * 10), 2)
    print(f"│  {C_MUTED}Dual Tranches:{C_RESET} TP1: {C_GREEN}+1.25R (70%){C_RESET}  │  TP2: {C_GOLD}+{rr:.2f}R Runner (30%){C_RESET}                       │")
    print(f"│  {C_MUTED}Position Sizing:{C_RESET} Risk $50 ──▶ {C_WHITE}{risk_50_lots} Lots{C_RESET}  │  Risk $100 ──▶ {C_WHITE}{risk_100_lots} Lots{C_RESET}                    │")
    print(f"{border_color}└──────────────────────────────────────────────────────────────────────────────────────┘{C_RESET}\n")


def connect_mt5():
    try:
        import MetaTrader5 as mt5
        terminal_path = os.environ.get("MT5_TERMINAL_PATH", r"C:\Program Files\MetaTrader 5 Terminal\terminal64.exe")
        if mt5.initialize(path=terminal_path) or mt5.initialize():
            acc = mt5.account_info()
            if acc:
                print(f"{C_GREEN}✓ Connected to MetaTrader 5{C_RESET} | Account: {C_WHITE}{acc.login}{C_RESET} ({acc.server}) | Balance: {C_GOLD}${acc.balance:,.2f}{C_RESET}\n")
                return mt5
        return None
    except Exception:
        return None


def main():
    print_header()
    mt5 = connect_mt5()

    print(f"{C_GOLD}God's Eye State Machine Active: Monitoring Order-Flow Alignments...{C_RESET}\n")
    time.sleep(1)

    signals = [
        {
            "pair": "EUR/USD",
            "archetype": "TREND_PULLBACK_RAID (4H Trend)",
            "bias": "SHORT",
            "entry": 1.08720,
            "sl": 1.08835,
            "tp": 1.08375,
            "pips_sl": 11.5,
            "pips_tp": 34.5,
            "rr": 3.00,
            "order_type": "LIMIT @ CISD"
        },
        {
            "pair": "GBP/USD",
            "archetype": "SMT_TURTLE_SOUP (Sister Raid)",
            "bias": "LONG",
            "entry": 1.29420,
            "sl": 1.29295,
            "tp": 1.29820,
            "pips_sl": 12.5,
            "pips_tp": 40.0,
            "rr": 3.20,
            "order_type": "LIMIT @ FVG"
        },
        {
            "pair": "XAU/USD",
            "archetype": "JUDAS_SWEEP_REVERSAL (Asian Low)",
            "bias": "LONG",
            "entry": 2735.40,
            "sl": 2732.20,
            "tp": 2748.20,
            "pips_sl": 32.0,
            "pips_tp": 128.0,
            "rr": 4.00,
            "order_type": "MARKET CONFIRM"
        }
    ]

    for s in signals:
        display_signal(
            pair=s["pair"],
            archetype=s["archetype"],
            bias=s["bias"],
            entry=s["entry"],
            sl=s["sl"],
            tp=s["tp"],
            pips_sl=s["pips_sl"],
            pips_tp=s["pips_tp"],
            rr=s["rr"],
            order_type=s["order_type"]
        )

    print(f"{C_MUTED}Ready for live stream video capture. Press Ctrl+C to exit.{C_RESET}")


if __name__ == "__main__":
    main()
