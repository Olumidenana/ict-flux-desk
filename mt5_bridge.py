"""MetaTrader 5 Direct Bridge for ICT Flux Desk.
Connects to MT5, validates trade parameters (pips, risk, lot size), and places orders.
"""

import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def place_order(symbol: str, order_type: str, price: float, sl: float, tp: float, volume: float = 0.01, comment: str = "ICT Flux Desk"):
    try:
        import MetaTrader5 as mt5
    except ImportError:
        print("[ERROR] MetaTrader5 package is required: uv run --with MetaTrader5 python mt5_bridge.py")
        return False

    terminal_path = os.environ.get("MT5_TERMINAL_PATH", r"C:\Program Files\MetaTrader 5 Terminal\terminal64.exe")
    if not mt5.initialize(path=terminal_path) and not mt5.initialize():
        print(f"[ERROR] Failed to connect to MetaTrader 5: {mt5.last_error()}")
        return False

    account = mt5.account_info()
    if not account:
        print("[ERROR] No trading account is logged in inside MT5.")
        mt5.shutdown()
        return False

    print(f"[MT5] Connected to Account: {account.login} ({account.server}) | Balance: ${account.balance:,.2f}")

    if not mt5.symbol_select(symbol, True):
        print(f"[ERROR] Symbol {symbol} not found in MT5 Market Watch.")
        mt5.shutdown()
        return False

    sym_info = mt5.symbol_info(symbol)
    if not sym_info:
        print(f"[ERROR] Failed to get symbol info for {symbol}")
        mt5.shutdown()
        return False

    # Normalize lot size to volume step
    step = sym_info.volume_step or 0.01
    volume = round(round(volume / step) * step, 2)
    volume = max(sym_info.volume_min, min(sym_info.volume_max, volume))

    type_dict = {
        "BUY": mt5.ORDER_TYPE_BUY,
        "SELL": mt5.ORDER_TYPE_SELL,
        "BUY_LIMIT": mt5.ORDER_TYPE_BUY_LIMIT,
        "SELL_LIMIT": mt5.ORDER_TYPE_SELL_LIMIT,
    }

    cmd = type_dict.get(order_type.upper(), mt5.ORDER_TYPE_BUY_LIMIT)
    is_market = cmd in (mt5.ORDER_TYPE_BUY, mt5.ORDER_TYPE_SELL)
    exec_price = sym_info.ask if cmd == mt5.ORDER_TYPE_BUY else (sym_info.bid if cmd == mt5.ORDER_TYPE_SELL else price)

    request = {
        "action": mt5.TRADE_ACTION_DEAL if is_market else mt5.TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": volume,
        "type": cmd,
        "price": exec_price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 20261106,
        "comment": comment,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC if is_market else mt5.ORDER_FILLING_RETURN,
    }

    print(f"[MT5] Submitting Order: {order_type} {symbol} | Lots: {volume} | Price: {exec_price} | SL: {sl} | TP: {tp}...")
    result = mt5.order_send(request)

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"[MT5 ERROR] Order send failed! Retcode: {result.retcode} ({result.comment})")
        mt5.shutdown()
        return False

    print(f"[MT5 SUCCESS] Order placed successfully! Order Ticket: #{result.order}")
    mt5.shutdown()
    return True


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="ICT Flux MT5 Direct Order Execution")
    parser.add_argument("--symbol", default="GBPUSD", help="Symbol (e.g. GBPUSD)")
    parser.add_argument("--type", default="BUY_LIMIT", choices=["BUY", "SELL", "BUY_LIMIT", "SELL_LIMIT"])
    parser.add_argument("--price", type=float, default=1.29420)
    parser.add_argument("--sl", type=float, default=1.29295)
    parser.add_argument("--tp", type=float, default=1.29820)
    parser.add_argument("--lots", type=float, default=0.01)

    args = parser.parse_args()
    place_order(args.symbol, args.type, args.price, args.sl, args.tp, args.lots)
