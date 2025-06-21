import random
from datetime import datetime
from send_to_telegram import send_message

def get_mock_candles():
    return [{"time": t, "open": random.uniform(1.100, 1.120),
             "high": random.uniform(1.120, 1.130),
             "low": random.uniform(1.090, 1.100),
             "close": random.uniform(1.100, 1.120)} for t in range(50)]

def detect_bias(candles):
    avg_open = sum(c["open"] for c in candles) / len(candles)
    avg_close = sum(c["close"] for c in candles) / len(candles)
    return "bullish" if avg_close > avg_open else "bearish"

def find_liquidity(zones):
    return {"buy_side": max(c["high"] for c in zones),
            "sell_side": min(c["low"] for c in zones)}

def decide_trade(bias, liq):
    direction = "buy" if bias == "bullish" else "sell"
    entry = liq["buy_side"] if direction == "buy" else liq["sell_side"]
    tp = entry + 0.003 if direction == "buy" else entry - 0.003
    sl = entry - 0.002 if direction == "buy" else entry + 0.002
    return direction, entry, tp, sl

def run_trading_bot():
    candles = get_mock_candles()
    bias = detect_bias(candles)
    liq = find_liquidity(candles)
    direction, entry, tp, sl = decide_trade(bias, liq)
    
    message = f"🧠 توصية ICT\nBias: {bias}\nEntry: {entry:.4f}\nTP: {tp:.4f}\nSL: {sl:.4f}\nR:R = 1:1.5"
    send_message(message)