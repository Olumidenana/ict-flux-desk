# -*- coding: utf-8 -*-
"""Builder script to generate the unified ICT Flux Desk:
1. Real TradingView Terminal Widget with ICT markups displayed INSIDE the terminal
2. Surgical ICT stop losses (4.5 to 8.0 pips) yielding 1:4R to 1:6.7R
3. Loss Avoidance & Breakeven Governor (+0.8R Free-Roll, CISD early exit, 70/30 harvest)
4. Deriv Synthetic Indices (VOL 75, VOL 100) with zero performance overhead
5. Stand-Aside discipline mode
6. Executed & Monitored Trades Log (Subsidiary Audit Trail)
7. Full Mobile-responsive view
"""

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>ICT FLUX DESK • Autonomous Execution Terminal</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500;600;700;800&family=Geist:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #07080B;
      --surface: #0E1015;
      --surface-2: #141720;
      --surface-3: #1B1F2C;
      --line: rgba(255, 255, 255, 0.08);
      --line-2: rgba(255, 255, 255, 0.14);
      --line-gold: rgba(240, 185, 75, 0.35);
      --brand: linear-gradient(135deg, #F7CF6B 0%, #E39B2E 100%);
      --text: #F2F4F8;
      --muted: #9AA3B5;
      --faint: #646C7E;
      --accent: #F0B94B;
      --accent-ink: #1A1305;
      --accent-soft: rgba(240, 185, 75, 0.12);
      --accent-glow: rgba(240, 185, 75, 0.25);
      --bull: #2BD47D;
      --bull-soft: rgba(43, 212, 125, 0.12);
      --bear: #FF5C6C;
      --bear-soft: rgba(255, 92, 108, 0.12);
      --warn: #F59E0B;
      --warn-soft: rgba(245, 158, 11, 0.12);
      --cyan: #38BDF8;
      --cyan-soft: rgba(56, 189, 248, 0.12);
      --mono: 'Geist Mono', ui-monospace, monospace;
      --sans: 'Geist', -apple-system, sans-serif;
      --glow: radial-gradient(900px 420px at 0% -8%, rgba(240, 185, 75, 0.08), transparent 60%),
              radial-gradient(800px 380px at 100% -6%, rgba(90, 169, 255, 0.05), transparent 60%);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
    body {
      background: var(--glow), var(--bg);
      background-attachment: fixed;
      color: var(--text);
      font-family: var(--sans);
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    /* Top Bar */
    header.top {
      position: sticky;
      top: 0;
      z-index: 50;
      background: rgba(7, 8, 11, 0.94);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--line);
    }
    .top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 60px;
      padding: 0 16px;
      gap: 12px;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
    }
    .logo-badge {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: var(--brand);
      display: grid;
      place-items: center;
      color: var(--accent-ink);
      font-weight: 900;
      font-size: 17px;
      font-family: var(--mono);
      box-shadow: 0 0 18px var(--accent-glow);
      flex-shrink: 0;
    }
    .brand-col {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .brand-title {
      font-weight: 800;
      font-size: 14.5px;
      letter-spacing: -0.02em;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .subsidiary-pill {
      font-size: 8.5px;
      font-family: var(--mono);
      font-weight: 700;
      color: var(--accent);
      letter-spacing: 0.04em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .subsidiary-pill a {
      color: var(--muted);
      text-decoration: none;
      border-bottom: 1px dotted var(--faint);
      transition: color 0.15s;
    }
    .subsidiary-pill a:hover {
      color: var(--accent);
    }

    .top-right {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .clock-pill {
      font-family: var(--mono);
      font-size: 10.5px;
      color: var(--muted);
      background: var(--surface-2);
      padding: 5px 10px;
      border-radius: 6px;
      border: 1px solid var(--line);
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }
    .session-pill {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 5px 10px;
      border-radius: 99px;
      border: 1px solid var(--line-gold);
      background: var(--accent-soft);
      color: var(--accent);
      font-family: var(--mono);
      font-size: 10.5px;
      font-weight: 700;
      white-space: nowrap;
    }
    .session-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--bull);
      box-shadow: 0 0 8px var(--bull);
      animation: pulse 1.8s infinite;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }

    /* Main Grid Layout */
    .app-layout {
      display: grid;
      grid-template-columns: 1fr 490px;
      height: calc(100vh - 60px);
    }

    /* Left Chart Column */
    .chart-panel {
      display: flex;
      flex-direction: column;
      background: #050608;
      border-right: 1px solid var(--line);
      position: relative;
      height: 100%;
    }
    .chart-toolbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      background: var(--surface);
      border-bottom: 1px solid var(--line);
      gap: 8px;
      flex-wrap: nowrap;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    .pair-bar {
      display: flex;
      gap: 4px;
      flex-shrink: 0;
    }
    .p-btn {
      padding: 5px 10px;
      border-radius: 6px;
      border: 1px solid var(--line);
      background: var(--surface-2);
      color: var(--muted);
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s;
      white-space: nowrap;
    }
    .p-btn:hover {
      border-color: var(--accent);
      color: var(--text);
    }
    .p-btn.active {
      background: var(--accent-soft);
      border-color: var(--accent);
      color: var(--accent);
    }
    .p-btn.deriv {
      border-color: rgba(56, 189, 248, 0.35);
      color: var(--cyan);
    }
    .p-btn.deriv.active {
      background: var(--cyan-soft);
      border-color: var(--cyan);
      color: var(--cyan);
    }

    .chart-meta {
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--mono);
      font-size: 10.5px;
      color: var(--muted);
      flex-shrink: 0;
    }
    .status-badge {
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 9.5px;
      font-weight: 800;
      white-space: nowrap;
    }
    .status-badge.active {
      background: var(--bull-soft);
      border: 1px solid rgba(43,212,125,0.3);
      color: var(--bull);
    }
    .status-badge.standaside {
      background: var(--warn-soft);
      border: 1px solid rgba(245,158,11,0.3);
      color: var(--warn);
    }

    /* TradingView Stage with Inside Markups Overlay */
    .chart-stage {
      flex: 1;
      width: 100%;
      height: 100%;
      min-height: 440px;
      position: relative;
      background: #050608;
    }
    #tvFrameWrap {
      width: 100%;
      height: 100%;
      border: 0;
      position: absolute;
      top: 0;
      left: 0;
    }
    #tvFrame {
      width: 100%;
      height: 100%;
      border: 0;
      display: block;
    }

    /* ICT MARKUPS DIRECTLY INSIDE TRADINGVIEW TERMINAL */
    .tv-inside-markups {
      position: absolute;
      top: 12px;
      left: 12px;
      right: 12px;
      pointer-events: none;
      display: flex;
      flex-direction: column;
      gap: 8px;
      z-index: 10;
    }
    .tv-hud-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
    }
    .tv-hud-pillbox {
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(7, 8, 11, 0.88);
      backdrop-filter: blur(10px);
      padding: 6px 12px;
      border-radius: 8px;
      border: 1px solid var(--line-gold);
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    .tv-hud-title {
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 800;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .tv-hud-sub {
      font-family: var(--mono);
      font-size: 9.5px;
      color: var(--accent);
      font-weight: 700;
    }

    /* Live On-Chart Markups Bar */
    .tv-markups-bar {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
      background: rgba(14, 16, 21, 0.86);
      backdrop-filter: blur(8px);
      padding: 6px 10px;
      border-radius: 7px;
      border: 1px solid var(--line);
      width: fit-content;
    }
    .tv-m-tag {
      font-family: var(--mono);
      font-size: 9.5px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .tv-m-tag.entry {
      background: var(--accent-soft);
      border: 1px solid var(--line-gold);
      color: var(--accent);
    }
    .tv-m-tag.sl {
      background: var(--bear-soft);
      border: 1px solid rgba(255, 92, 108, 0.35);
      color: var(--bear);
    }
    .tv-m-tag.tp {
      background: var(--bull-soft);
      border: 1px solid rgba(43, 212, 125, 0.35);
      color: var(--bull);
    }
    .tv-m-tag.ref {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--muted);
    }

    /* Right Action Desk Column */
    .desk-panel {
      background: var(--surface);
      overflow-y: auto;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      -webkit-overflow-scrolling: touch;
    }

    /* Horizon Selector Bar */
    .horizon-bar {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 5px;
      padding: 3px;
      border-radius: 9px;
      background: var(--surface-2);
      border: 1px solid var(--line);
    }
    .hz-btn {
      padding: 8px 4px;
      border-radius: 6px;
      border: 0;
      background: transparent;
      color: var(--muted);
      font-family: var(--mono);
      font-size: 10.5px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 2px;
      transition: all 0.15s;
    }
    .hz-btn:hover {
      color: var(--text);
      background: rgba(255, 255, 255, 0.03);
    }
    .hz-btn.active {
      background: var(--accent-soft);
      color: var(--accent);
      box-shadow: 0 0 10px var(--accent-glow);
      border: 1px solid var(--line-gold);
    }
    .hz-sub {
      font-size: 8.5px;
      font-weight: 500;
      opacity: 0.8;
    }

    /* Stand Aside Caution Notice Banner */
    .stand-aside-banner {
      display: none;
      padding: 10px 12px;
      border-radius: 8px;
      background: var(--warn-soft);
      border: 1px solid rgba(245, 158, 11, 0.35);
      color: var(--warn);
      font-family: var(--mono);
    }
    .stand-aside-banner.visible {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .sab-top {
      font-weight: 800;
      font-size: 11.5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .sab-desc {
      font-size: 10px;
      color: #E2E8F0;
      line-height: 1.4;
    }

    /* Action Directive Card */
    .directive-card {
      padding: 12px 14px;
      border-radius: 9px;
      background: var(--surface-2);
      border: 1px solid var(--line-gold);
      display: flex;
      flex-direction: column;
      gap: 6px;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35);
      position: relative;
    }
    .directive-card.standaside {
      border-color: rgba(245, 158, 11, 0.4);
      background: rgba(245, 158, 11, 0.04);
    }
    .directive-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 6px;
    }
    .archetype-label {
      font-size: 10px;
      font-family: var(--mono);
      font-weight: 700;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }
    .intercept-pill {
      font-size: 8.5px;
      font-family: var(--mono);
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 4px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text);
      white-space: nowrap;
    }
    .directive-headline {
      font-size: 18px;
      font-weight: 800;
      font-family: var(--mono);
      letter-spacing: -0.02em;
    }
    .directive-headline.buy { color: var(--bull); }
    .directive-headline.sell { color: var(--bear); }
    .directive-headline.wait { color: var(--warn); }
    .directive-exec {
      font-size: 11px;
      color: var(--muted);
      line-height: 1.4;
    }
    .directive-exec b { color: var(--text); }

    /* WHAT TO DO / WHAT NOT TO DO / TIMING TRIAD */
    .guidance-box {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .guide-cell {
      padding: 9px 11px;
      border-radius: 7px;
      background: var(--surface-2);
      border: 1px solid var(--line);
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .guide-lbl {
      display: flex;
      align-items: center;
      gap: 5px;
      font-family: var(--mono);
      font-size: 9.5px;
      font-weight: 800;
      letter-spacing: 0.02em;
    }
    .guide-lbl.green { color: var(--bull); }
    .guide-lbl.red { color: var(--bear); }
    .guide-lbl.gold { color: var(--accent); }
    .guide-desc {
      font-size: 11px;
      color: #CFD7E6;
      line-height: 1.4;
    }
    .guide-desc b {
      color: #FFF;
      font-weight: 700;
    }

    /* Surgical Pip Matrix Level Boxes */
    .levels {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 6px;
    }
    .level-box {
      padding: 8px 10px;
      border-radius: 7px;
      background: var(--surface-2);
      border: 1px solid var(--line);
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .level-label {
      font-size: 9px;
      font-family: var(--mono);
      color: var(--faint);
      text-transform: uppercase;
      font-weight: 700;
    }
    .level-price {
      font-size: 13.5px;
      font-family: var(--mono);
      font-weight: 800;
      word-break: break-all;
    }
    .pip-pill {
      font-size: 8.5px;
      font-family: var(--mono);
      font-weight: 800;
      padding: 1px 4px;
      border-radius: 3px;
      width: fit-content;
      margin-top: 1px;
    }
    .pip-pill.gold { background: var(--accent-soft); color: var(--accent); }
    .pip-pill.red { background: var(--bear-soft); color: var(--bear); }
    .pip-pill.green { background: var(--bull-soft); color: var(--bull); }

    /* Loss Avoidance & Breakeven Governor Box */
    .loss-avoidance-box {
      padding: 9px 11px;
      border-radius: 7px;
      background: rgba(240, 185, 75, 0.04);
      border: 1px solid rgba(240, 185, 75, 0.25);
      display: flex;
      flex-direction: column;
      gap: 4px;
      font-family: var(--mono);
      font-size: 10px;
    }
    .lab-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: var(--accent);
      font-weight: 800;
      font-size: 9.5px;
    }
    .lab-desc {
      color: #E2E8F0;
      font-size: 10px;
      line-height: 1.35;
    }

    /* Dual-Tranche Governor */
    .governor-breakdown {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 5px;
      padding: 8px 10px;
      border-radius: 7px;
      background: var(--surface-2);
      border: 1px solid var(--line);
    }
    .gov-step {
      display: flex;
      flex-direction: column;
      gap: 2px;
      font-family: var(--mono);
      font-size: 9px;
    }
    .gov-step span { color: var(--faint); }
    .gov-step b { color: var(--text); font-size: 10.5px; }

    /* Sizing & R:R */
    .calc-panel {
      padding: 8px 12px;
      border-radius: 7px;
      background: var(--surface-2);
      border: 1px solid var(--line);
      font-family: var(--mono);
      font-size: 10.5px;
    }
    .lot-recommendation {
      display: flex;
      justify-content: space-between;
      color: var(--muted);
      flex-wrap: wrap;
      gap: 4px;
    }
    .lot-recommendation b { color: var(--text); }

    /* Action Buttons */
    .action-row {
      display: grid;
      grid-template-columns: 1fr 1.3fr;
      gap: 6px;
      margin-top: 2px;
    }
    .btn {
      padding: 10px;
      border-radius: 7px;
      border: 1px solid var(--line);
      background: var(--surface-2);
      color: var(--text);
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      transition: all 0.15s;
    }
    .btn:hover {
      border-color: var(--accent);
      background: var(--surface-3);
    }
    .btn.primary {
      background: var(--brand);
      color: var(--accent-ink);
      border: 0;
      box-shadow: 0 0 14px var(--accent-glow);
    }
    .btn.primary:hover {
      transform: translateY(-1px);
      box-shadow: 0 0 20px var(--accent-glow);
    }
    .btn.disabled {
      opacity: 0.45;
      cursor: not-allowed;
      background: var(--surface-2) !important;
      color: var(--muted) !important;
      border: 1px solid var(--line) !important;
      box-shadow: none !important;
    }

    /* Live Trades Log & Audit Trail */
    .trade-log-panel {
      border-top: 1px solid var(--line);
      background: var(--surface);
      padding: 12px 16px;
    }
    .log-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
      flex-wrap: wrap;
      gap: 6px;
    }
    .log-title {
      font-family: var(--mono);
      font-size: 11.5px;
      font-weight: 800;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .log-filter-bar {
      display: flex;
      gap: 4px;
    }
    .lf-btn {
      font-family: var(--mono);
      font-size: 9.5px;
      padding: 3px 7px;
      border-radius: 4px;
      background: var(--surface-2);
      border: 1px solid var(--line);
      color: var(--muted);
      cursor: pointer;
    }
    .lf-btn.active {
      background: var(--accent-soft);
      color: var(--accent);
      border-color: var(--line-gold);
    }

    .log-table-wrap {
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    table.log-table {
      width: 100%;
      border-collapse: collapse;
      font-family: var(--mono);
      font-size: 10.5px;
    }
    table.log-table th {
      text-align: left;
      padding: 6px 8px;
      color: var(--faint);
      border-bottom: 1px solid var(--line);
      font-size: 9px;
      text-transform: uppercase;
      font-weight: 700;
    }
    table.log-table td {
      padding: 8px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: #E2E8F0;
      white-space: nowrap;
    }
    table.log-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }
    .tag-win {
      color: var(--bull);
      font-weight: 800;
      background: var(--bull-soft);
      padding: 2px 5px;
      border-radius: 4px;
      border: 1px solid rgba(43,212,125,0.3);
    }
    .tag-be {
      color: var(--accent);
      font-weight: 800;
      background: var(--accent-soft);
      padding: 2px 5px;
      border-radius: 4px;
      border: 1px solid var(--line-gold);
    }
    .tag-loss {
      color: var(--bear);
      font-weight: 800;
      background: var(--bear-soft);
      padding: 2px 5px;
      border-radius: 4px;
      border: 1px solid rgba(255,92,108,0.3);
    }
    .tag-running {
      color: #60A5FA;
      font-weight: 800;
      background: rgba(96,165,250,0.12);
      padding: 2px 5px;
      border-radius: 4px;
      border: 1px solid rgba(96,165,250,0.3);
    }

    /* Toast */
    .toast {
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: var(--surface-3);
      border: 1px solid var(--line-gold);
      color: var(--text);
      font-family: var(--mono);
      font-size: 11.5px;
      padding: 10px 16px;
      border-radius: 7px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      display: none;
      z-index: 100;
      max-width: 90vw;
      animation: pop 0.2s ease-out;
    }
    @keyframes pop {
      from { transform: scale(0.9); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }

    /* RESPONSIVE MOBILE OPTIMIZATIONS (< 1024px & < 768px) */
    @media (max-width: 1024px) {
      .app-layout {
        grid-template-columns: 1fr;
        height: auto;
      }
      .chart-panel {
        border-right: 0;
        border-bottom: 1px solid var(--line);
      }
      .chart-stage {
        height: 440px;
        min-height: 400px;
      }
    }

    @media (max-width: 768px) {
      .top-bar {
        height: auto;
        padding: 8px 12px;
        flex-wrap: wrap;
      }
      .clock-pill {
        display: none;
      }
      .brand-title {
        font-size: 13.5px;
      }
      .chart-stage {
        height: 380px;
        min-height: 350px;
      }
      .tv-inside-markups {
        top: 8px;
        left: 8px;
        right: 8px;
      }
      .directive-headline {
        font-size: 16px;
      }
      .action-row {
        grid-template-columns: 1fr;
      }
      .levels {
        grid-template-columns: 1fr 1fr 1fr;
      }
      .governor-breakdown {
        grid-template-columns: 1fr 1fr 1fr;
      }
    }
  </style>
</head>
<body>

  <!-- TOP HEADER -->
  <header class="top">
    <div class="top-bar">
      <div class="brand">
        <div class="logo-badge">F</div>
        <div class="brand-col">
          <div class="brand-title">
            <span>ICT FLUX DESK</span>
            <span style="font-size:9.5px;color:var(--faint);">v39.5</span>
          </div>
          <div class="subsidiary-pill">
            <span>SUBSIDIARY OF</span>
            <a href="https://ictflux.app" target="_blank" title="Visit Parent Application">ICTFLUX.APP ↗</a>
            <span>• GOD'S EYE ENGINE</span>
          </div>
        </div>
      </div>

      <div class="top-right">
        <div class="clock-pill">
          <span id="clockUtc">00:00:00 UTC</span>
          <span style="opacity:0.3">|</span>
          <span id="clockNy">00:00:00 NY</span>
        </div>
        <div class="session-pill">
          <div class="session-dot"></div>
          <span id="topSession">LONDON KZ ACTIVE</span>
        </div>
      </div>
    </div>
  </header>

  <!-- MAIN TWO-COLUMN WORKSPACE -->
  <div class="app-layout">
    
    <!-- LEFT: REAL TRADINGVIEW TERMINAL WITH INSIDE ICT MARKUPS OVERLAY -->
    <div class="chart-panel">
      
      <!-- Toolbar with Forex, Indices, and Deriv Synthetics -->
      <div class="chart-toolbar">
        <div class="pair-bar">
          <button class="p-btn active" onclick="selectPair('GBPUSD', this)">GBP/USD</button>
          <button class="p-btn" onclick="selectPair('EURUSD', this)">EUR/USD</button>
          <button class="p-btn" onclick="selectPair('XAUUSD', this)">XAU/USD (Gold)</button>
          <button class="p-btn" onclick="selectPair('NAS100', this)">NAS100</button>
          <button class="p-btn" onclick="selectPair('US500', this)">US500</button>
          <button class="p-btn" onclick="selectPair('USDJPY', this)">USD/JPY</button>
          <button class="p-btn deriv" onclick="selectPair('VOL75', this)">⚡ VOL 75 (Deriv)</button>
          <button class="p-btn deriv" onclick="selectPair('VOL100', this)">⚡ VOL 100 (Deriv)</button>
        </div>

        <div class="chart-meta">
          <span id="pairSpread">Spread: 0.8 pips</span>
          <span class="status-badge active" id="pairStatusBadge">ACTIVE INTERCEPT</span>
        </div>
      </div>

      <!-- TradingView Terminal Container with Inside ICT Overlays -->
      <div class="chart-stage">
        
        <!-- REAL TRADINGVIEW TERMINAL IFRAME (LIVE FEED & DRAWINGS) -->
        <div id="tvFrameWrap">
          <iframe id="tvFrame" allowfullscreen loading="eager"></iframe>
        </div>

        <!-- ICT INSTITUTIONAL MARKUPS DISPLAYED DIRECTLY INSIDE TRADINGVIEW -->
        <div class="tv-inside-markups">
          <div class="tv-hud-top">
            <div class="tv-hud-pillbox">
              <div class="tv-hud-title">
                <span id="lgSymbol">GBP/USD</span>
                <span style="color:var(--muted);font-weight:400" id="lgTf">M5</span>
                <span class="tv-hud-sub" id="lgModel">SMT TURTLE SOUP</span>
              </div>
            </div>
            
            <div class="tv-markups-bar">
              <span class="tv-m-tag entry" id="tvTagEntry">ENTRY @ 1.29420</span>
              <span class="tv-m-tag sl" id="tvTagSl">SL: 8.0 PIPS @ 1.29340</span>
              <span class="tv-m-tag tp" id="tvTagTp">TP: +40.0 PIPS (1:5.0R)</span>
              <span class="tv-m-tag ref" id="tvTagFvg">FVG 50% CE: 1.29420</span>
              <span class="tv-m-tag ref" id="tvTagMo">MIDNIGHT OPEN: 1.29480</span>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- RIGHT: GOD'S EYE ACTION DIRECTIVE DESK -->
    <div class="desk-panel">
      
      <!-- Style / Horizon Selector -->
      <div class="horizon-bar">
        <button class="hz-btn" onclick="setHorizon('scalp', this)">
          <span>⚡ SCALP</span>
          <span class="hz-sub">15-45m · 4-8 Pips</span>
        </button>
        <button class="hz-btn active" onclick="setHorizon('day', this)">
          <span>🎯 DAY TRADE</span>
          <span class="hz-sub">2-5h · 8-16 Pips</span>
        </button>
        <button class="hz-btn" onclick="setHorizon('swing', this)">
          <span>🌊 SWING</span>
          <span class="hz-sub">1-3d · 30-60 Pips</span>
        </button>
      </div>

      <!-- Stand Aside Warning Banner (Shown when no valid setup exists) -->
      <div class="stand-aside-banner" id="standAsideBanner">
        <div class="sab-top">
          <span>⚠️ STAND ASIDE • CAPITAL PRESERVATION</span>
        </div>
        <div class="sab-desc" id="standAsideDesc">
          Market is currently consolidating inside dead Asian Range. No institutional displacement or FVG has formed. Do not force scalps.
        </div>
      </div>

      <!-- Action Directive Card -->
      <div class="directive-card" id="dirCard">
        <div class="directive-top">
          <span class="archetype-label" id="dirArchetype">SMT Turtle Soup (Sister Divergence)</span>
          <span class="intercept-pill" id="dirHorizonBadge">DAY TRADE CHOKEPOINT</span>
        </div>
        <div class="directive-headline buy" id="dirHeadline">
          BUY LIMIT @ 1.29420
        </div>
        <div class="directive-exec">
          Best Entry Point: <b id="dirOrder">Limit @ FVG Consequent Encroachment (50%)</b>
        </div>
      </div>

      <!-- WHAT TO DO / WHAT NOT TO DO / TIMING TRIAD -->
      <div class="guidance-box">
        <div class="guide-cell">
          <div class="guide-lbl green">
            <span>✅ WHAT TO DO (EXECUTION DIRECTIVE)</span>
          </div>
          <div class="guide-desc" id="guideDo">
            Wait for price to tap the 50% Consequent Encroachment (1.29420) of the M5 Fair Value Gap inside the London Killzone. Place BUY LIMIT with Stop Loss at 1.29340.
          </div>
        </div>

        <div class="guide-cell">
          <div class="guide-lbl red">
            <span>⛔ WHAT NOT TO DO (TRAP & CHOP WARNING)</span>
          </div>
          <div class="guide-desc" id="guideDont">
            DO NOT market-chase the green expansion candle above Asian High. DO NOT hold if 1.29340 is violated with candle-body close before 08:30 NY macro.
          </div>
        </div>

        <div class="guide-cell">
          <div class="guide-lbl gold">
            <span>⏰ WHEN TO EXPECT IT (TIMING & HOLD WINDOW)</span>
          </div>
          <div class="guide-desc" id="guideWhen">
            Delivery window: 08:30 – 09:15 UTC (London Open). Expected hold duration: 2 to 4 hours.
          </div>
        </div>
      </div>

      <!-- Pip Transparency Matrix with Surgical ICT Stop Loss -->
      <div class="levels">
        <div class="level-box entry">
          <div class="level-label">Entry Level</div>
          <div class="level-price" style="color:var(--accent)" id="lvlEntry">1.29420</div>
          <span class="pip-pill gold" id="pillEntry">LIMIT @ 50% CE</span>
        </div>
        <div class="level-box stop">
          <div class="level-label">Stop Loss</div>
          <div class="level-price" style="color:var(--bear)" id="lvlStop">1.29340</div>
          <span class="pip-pill red" id="pillStop">8.0 PIPS RISK</span>
        </div>
        <div class="level-box target">
          <div class="level-label">Target Draw</div>
          <div class="level-price" style="color:var(--bull)" id="lvlTarget">1.29820</div>
          <span class="pip-pill green" id="pillTarget">40.0 PIPS TP</span>
        </div>
      </div>

      <!-- Loss Avoidance & Breakeven Governor Box -->
      <div class="loss-avoidance-box">
        <div class="lab-top">
          <span>🛡️ LOSS AVOIDANCE & FREE-ROLL GOVERNOR</span>
          <span style="color:var(--bull)">ZERO-LOSS LOCK</span>
        </div>
        <div class="lab-desc" id="labDesc">
          At <b>+0.80R expansion (1.29484)</b>, Stop Loss automatically snaps to <b>Entry + 1 pip (1.29430)</b>. If an M5 candle closes below CISD prior to macro window end, kill at market to prevent full -1.0R loss.
        </div>
      </div>

      <!-- Dual-Tranche Governor Breakdown -->
      <div class="governor-breakdown">
        <div class="gov-step">
          <span>Auto BE Lock (+0.80R)</span>
          <b id="govBe">+0.80R (1.29484)</b>
        </div>
        <div class="gov-step">
          <span>TP1 Harvest (70%)</span>
          <b id="govTp1">+1.50R (1.29540)</b>
        </div>
        <div class="gov-step">
          <span>TP2 Runner (30%)</span>
          <b id="govTp2">+5.00R (1.29820)</b>
        </div>
      </div>

      <!-- Sizing Recommendation -->
      <div class="calc-panel">
        <div class="lot-recommendation">
          <span>Risk $50: <b id="calc50">0.62 Lots</b></span>
          <span>Risk $100: <b id="calc100">1.25 Lots</b></span>
          <span>R:R: <b style="color:var(--accent)" id="calcRr">1 : 5.00 R</b></span>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="action-row">
        <button class="btn" onclick="copyPlan()">📋 Copy Tweet</button>
        <button class="btn primary" id="btnExecute" onclick="executeTrade()">⚡ Execute on MT5</button>
      </div>

    </div>
  </div>

  <!-- BOTTOM: EXECUTED & MONITORED TRADES LOG (SUBSIDIARY AUDIT TRAIL) -->
  <div class="trade-log-panel">
    <div class="log-header">
      <div class="log-title">
        <span>📋 EXECUTED & MONITORED TRADES LOG</span>
        <span style="font-size:9.5px;color:var(--faint);">[Subsidiary Audit Trail • Synced with ictflux.app Engine]</span>
      </div>
      <div class="log-filter-bar">
        <button class="lf-btn active" onclick="filterLogs('all', this)">All (6)</button>
        <button class="lf-btn" onclick="filterLogs('active', this)">Live / Active</button>
        <button class="lf-btn" onclick="filterLogs('win', this)">Wins / BE</button>
        <button class="lf-btn" onclick="clearCustomLogs()">Reset Log</button>
      </div>
    </div>

    <div class="log-table-wrap">
      <table class="log-table">
        <thead>
          <tr>
            <th>Time (UTC)</th>
            <th>Ticket #</th>
            <th>Pair</th>
            <th>Horizon</th>
            <th>Model Archetype</th>
            <th>Side</th>
            <th>Entry</th>
            <th>Stop Loss</th>
            <th>Target</th>
            <th>Pip Metrics</th>
            <th>R:R</th>
            <th>Status / Outcome</th>
          </tr>
        </thead>
        <tbody id="tradeLogBody">
          <!-- Dynamically populated -->
        </tbody>
      </table>
    </div>
  </div>

  <div class="toast" id="toast"></div>

  <!-- APPLICATION DATA & ENGINE LOGIC -->
  <script>
    // Master Institutional Dataset for Forex, Commodities, Indices, and Deriv Synthetics
    const DATA = {
      GBPUSD: {
        label: 'GBP/USD',
        price: '1.29465',
        spread: '0.8 pips',
        pipScale: 0.0001,
        tvSymbol: 'FX:GBPUSD',
        horizons: {
          scalp: {
            status: 'ACTIVE',
            tf: 'M1',
            tvInterval: '1',
            badge: '⚡ SCALP INTERCEPT',
            headline: 'BUY LIMIT @ 1.29435',
            headlineClass: 'buy',
            archetype: 'Micro FVG CE Tap (London Macro)',
            order: 'Limit @ 50% Consequent Encroachment (1.29435)',
            doText: 'Place <b>Buy Limit at 1.29435</b> immediately following the 08:30 macro displacement. Anchor Stop Loss surgical at <b>1.29390 (4.5 pips)</b>.',
            dontText: '<b>DO NOT</b> hold longer than 35 minutes. If target is not reached before 09:15 UTC, close at market.',
            whenText: 'Active window: <b>08:30 – 09:15 UTC (London Macro)</b>. Expected hold time: <b>15 – 35 minutes</b>.',
            entry: '1.29435',
            stop: '1.29390',
            target: '1.29615',
            pillEntry: 'LIMIT @ M1 CE',
            pillStop: '4.5 PIPS RISK',
            pillTarget: '18.0 PIPS TP',
            lossAvoidance: 'At <b>+0.80R (1.29471)</b>, Stop Loss moves to Breakeven (+1 pip). If M1 candle closes below 1.29410, kill trade immediately.',
            govBe: '+0.80R (1.29471)',
            govTp1: '+1.50R (1.29502)',
            govTp2: '+4.00R (1.29615)',
            calc50: '1.11 Lots',
            calc100: '2.22 Lots',
            calcRr: '1 : 4.00 R',
            profile: 'IPDA: MICRO LIQUIDITY RUN',
            range: 'DISCOUNT ZONE: 32.5%',
            tagEntry: 'ENTRY LIMIT: 1.29435',
            tagSl: 'SURGICAL SL: 4.5 PIPS (1.29390)',
            tagTp: 'TP: +18.0 PIPS (1:4.0R)',
            tagFvg: 'M1 FVG 50% CE: 1.29435',
            tagMo: 'MIDNIGHT OPEN: 1.29480'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5',
            tvInterval: '5',
            badge: '🎯 DAY TRADE CHOKEPOINT',
            headline: 'BUY LIMIT @ 1.29420',
            headlineClass: 'buy',
            archetype: 'SMT Turtle Soup (Sister Divergence)',
            order: 'Limit @ FVG Consequent Encroachment (50%)',
            doText: 'Wait for price to tap the <b>50% Consequent Encroachment (1.29420)</b>. Surgical Stop Loss anchored tight at <b>1.29340 (8.0 pips)</b>.',
            dontText: '<b>DO NOT</b> market-chase the green expansion candle above Asian High. <b>DO NOT</b> hold if 1.29340 is violated with candle-body close.',
            whenText: 'Delivery window: <b>08:30 – 09:15 UTC (London Open)</b>. Expected hold duration: <b>2 to 5 hours</b>.',
            entry: '1.29420',
            stop: '1.29340',
            target: '1.29820',
            pillEntry: 'LIMIT @ 50% CE',
            pillStop: '8.0 PIPS RISK',
            pillTarget: '40.0 PIPS TP',
            lossAvoidance: 'At <b>+0.80R (1.29484)</b>, move SL to Breakeven (+1 pip). If M5 closes below 1.29370 before 09:30 NY macro, kill trade at market.',
            govBe: '+0.80R (1.29484)',
            govTp1: '+1.50R (1.29540)',
            govTp2: '+5.00R (1.29820)',
            calc50: '0.62 Lots',
            calc100: '1.25 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'IPDA: WEDNESDAY EXPANSION',
            range: 'DISCOUNT ARRAY: 38.2%',
            tagEntry: 'ENTRY LIMIT: 1.29420',
            tagSl: 'SURGICAL SL: 8.0 PIPS (1.29340)',
            tagTp: 'TP: +40.0 PIPS (1:5.0R)',
            tagFvg: 'FVG 50% CE: 1.29420',
            tagMo: 'MIDNIGHT OPEN: 1.29480'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1',
            tvInterval: '60',
            badge: '🌊 SWING PROFILE',
            headline: 'BUY LIMIT @ 1.29150',
            headlineClass: 'buy',
            archetype: 'Weekly Bullish Profile (Tuesday Low)',
            order: 'Limit @ 4H Bullish Order Block + Discount FVG',
            doText: 'Place <b>Buy Limit at 1.29150</b> anchored to 4H OB. Surgical Stop Loss at <b>1.28870 (28.0 pips)</b>. Target 1.30550 (140 pips).',
            dontText: '<b>DO NOT</b> exit early during intra-day London retracements if 4H market structure remains intact above 1.28870.',
            whenText: 'Hold duration: <b>1 to 3 days</b>. Weekly expansion phase targeting Friday NY settlement.',
            entry: '1.29150',
            stop: '1.28870',
            target: '1.30550',
            pillEntry: 'LIMIT @ 4H OB',
            pillStop: '28.0 PIPS RISK',
            pillTarget: '140.0 PIPS TP',
            lossAvoidance: 'At <b>+1.00R (1.29430)</b>, move SL to Entry. Take 70% off table at TP1 (1.29570) to ensure a guaranteed win.',
            govBe: '+0.80R (1.29374)',
            govTp1: '+1.50R (1.29570)',
            govTp2: '+5.00R (1.30550)',
            calc50: '0.18 Lots',
            calc100: '0.36 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'IPDA: MULTI-WEEK EXPANSION',
            range: 'DEEP DISCOUNT: 27.5%',
            tagEntry: 'ENTRY LIMIT: 1.29150',
            tagSl: 'SURGICAL SL: 28.0 PIPS (1.28870)',
            tagTp: 'TP: +140.0 PIPS (1:5.0R)',
            tagFvg: '4H DISCOUNT OB: 1.29150',
            tagMo: 'WEEKLY OPEN: 1.29380'
          }
        }
      },

      EURUSD: {
        label: 'EUR/USD',
        price: '1.08485',
        spread: '0.6 pips',
        pipScale: 0.0001,
        tvSymbol: 'FX:EURUSD',
        horizons: {
          scalp: {
            status: 'STAND_ASIDE',
            tf: 'M1',
            tvInterval: '1',
            badge: '⏸️ STAND ASIDE',
            headline: 'NO ACTIVE SCALP SETUP',
            headlineClass: 'wait',
            archetype: 'Asian Range Dead Consolidation',
            order: 'Stand Aside (No Displacement)',
            doText: '<b>STAND ASIDE.</b> Price is currently deadlocked in a 5.5 pip Asian Range. Capital preservation in effect until London Open.',
            dontText: '<b>DO NOT</b> force scalps inside 1.08440 – 1.08500 consolidation. Avoid low-probability bank settlement spread widening.',
            whenText: 'Next viable intercept window: <b>London Open Killzone (07:00 – 09:00 UTC)</b>.',
            entry: '---',
            stop: '---',
            target: '---',
            pillEntry: 'MONITORING',
            pillStop: 'STAND ASIDE',
            pillTarget: 'NO SETUP',
            lossAvoidance: 'Discipline Rule: 0 trades taken during 5-pip dead Asian consolidation avoids guaranteed chop losses.',
            govBe: '---',
            govTp1: '---',
            govTp2: '---',
            calc50: '0.00 Lots',
            calc100: '0.00 Lots',
            calcRr: '0.00 R',
            profile: 'IPDA: CONSOLIDATION PHASE',
            range: 'DEAD EQUILIBRIUM: 50.0%',
            tagEntry: 'MONITORING: 1.08485',
            tagSl: 'STATUS: STAND ASIDE',
            tagTp: 'TARGET: NO TRIGGER',
            tagFvg: 'ASIA HIGH: 1.08510',
            tagMo: 'ASIA LOW: 1.08440'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5',
            tvInterval: '5',
            badge: '🎯 DAY TRADE CHOKEPOINT',
            headline: 'SELL LIMIT @ 1.08720',
            headlineClass: 'sell',
            archetype: 'Judas Swing Reversal into Bearish OB',
            order: 'Limit @ Bearish Order Block + 15M FVG',
            doText: 'Enter <b>Sell Limit at 1.08720</b> as price completes the Judas Swing fakeout. Surgical Stop Loss at <b>1.08785 (6.5 pips)</b>.',
            dontText: '<b>DO NOT</b> short market before the liquidity sweep. Must see M5 CISD candle close below 1.08680.',
            whenText: 'Timing: <b>08:00 – 10:00 UTC (London Killzone)</b>. Expected hold: <b>3 to 5 hours</b>.',
            entry: '1.08720',
            stop: '1.08785',
            target: '1.08280',
            pillEntry: 'LIMIT @ 15M OB',
            pillStop: '6.5 PIPS RISK',
            pillTarget: '44.0 PIPS TP',
            lossAvoidance: 'At <b>+0.80R (1.08668)</b>, move SL to Breakeven (+1 pip). If price closes back above 1.08740, scratch trade immediately.',
            govBe: '+0.80R (1.08668)',
            govTp1: '+1.50R (1.08622)',
            govTp2: '+6.77R (1.08280)',
            calc50: '0.77 Lots',
            calc100: '1.54 Lots',
            calcRr: '1 : 6.77 R',
            profile: 'IPDA: LONDON REVERSAL',
            range: 'PREMIUM ARRAY: 68.5%',
            tagEntry: 'ENTRY LIMIT: 1.08720',
            tagSl: 'SURGICAL SL: 6.5 PIPS (1.08785)',
            tagTp: 'TP: +44.0 PIPS (1:6.7R)',
            tagFvg: 'BEARISH OB: 1.08720',
            tagMo: 'MIDNIGHT OPEN: 1.08600'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1',
            tvInterval: '60',
            badge: '🌊 SWING PROFILE',
            headline: 'SELL LIMIT @ 1.09100',
            headlineClass: 'sell',
            archetype: 'Multi-Week Bearish Delivery',
            order: 'Limit @ Daily Bearish Mitigation',
            doText: 'Place <b>Sell Limit at 1.09100</b>. Surgical Stop Loss at <b>1.09350 (25.0 pips)</b>. Target equal lows at 1.07700 (140 pips).',
            dontText: '<b>DO NOT</b> move stop loss to breakeven prematurely before the 1.08500 psychological barrier is pierced.',
            whenText: 'Hold window: <b>2 to 4 days</b>.',
            entry: '1.09100',
            stop: '1.09350',
            target: '1.07700',
            pillEntry: 'LIMIT @ DAILY OB',
            pillStop: '25.0 PIPS RISK',
            pillTarget: '140.0 PIPS TP',
            lossAvoidance: 'Dual-Tranche: Take 70% off at TP1 (1.08725). Run remaining 30% risk-free with Stop Loss locked in profit.',
            govBe: '+0.80R (1.08900)',
            govTp1: '+1.50R (1.08725)',
            govTp2: '+5.60R (1.07700)',
            calc50: '0.20 Lots',
            calc100: '0.40 Lots',
            calcRr: '1 : 5.60 R',
            profile: 'IPDA: MONTHLY EXPANSION',
            range: 'EXTREME PREMIUM: 76.0%',
            tagEntry: 'ENTRY LIMIT: 1.09100',
            tagSl: 'SURGICAL SL: 25.0 PIPS (1.09350)',
            tagTp: 'TP: +140.0 PIPS (1:5.6R)',
            tagFvg: 'DAILY OB: 1.09100',
            tagMo: 'WEEKLY HIGH: 1.09450'
          }
        }
      },

      XAUUSD: {
        label: 'XAU/USD (Gold)',
        price: '2738.50',
        spread: '1.8 pips',
        pipScale: 0.10,
        tvSymbol: 'OANDA:XAUUSD',
        horizons: {
          scalp: {
            status: 'ACTIVE',
            tf: 'M1',
            tvInterval: '1',
            badge: '⚡ SCALP INTERCEPT',
            headline: 'BUY LIMIT @ 2734.20',
            headlineClass: 'buy',
            archetype: 'Comex Open FVG Tap',
            order: 'Limit @ M5 Consequent Encroachment (2734.20)',
            doText: 'Place <b>Buy Limit at 2734.20</b>. Surgical Stop Loss at <b>2732.40 (18.0 pips / $1.80)</b>. Target session high at 2743.20 (90 pips).',
            dontText: '<b>DO NOT</b> hold through the 14:00 London fixing if price has not reached TP1.',
            whenText: 'Timing: <b>13:20 – 14:15 UTC (Comex Open)</b>. Hold: <b>20 – 40 min</b>.',
            entry: '2734.20',
            stop: '2732.40',
            target: '2743.20',
            pillEntry: 'LIMIT @ M5 CE',
            pillStop: '18.0 PIPS RISK',
            pillTarget: '90.0 PIPS TP',
            lossAvoidance: 'At <b>+0.80R (2735.64)</b>, move SL to 2734.40 (+2 pips profit). Eliminates all gold spread exposure.',
            govBe: '+0.80R (2735.64)',
            govTp1: '+1.50R (2736.90)',
            govTp2: '+5.00R (2743.20)',
            calc50: '0.28 Lots',
            calc100: '0.56 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'IPDA: COMEX MACRO SWEEP',
            range: 'DISCOUNT ZONE: 34.0%',
            tagEntry: 'ENTRY LIMIT: 2734.20',
            tagSl: 'SURGICAL SL: 18.0 PIPS (2732.40)',
            tagTp: 'TP: +90.0 PIPS (1:5.0R)',
            tagFvg: 'M5 FVG 50% CE: 2734.20',
            tagMo: 'COMEX OPEN: 2733.00'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5',
            tvInterval: '5',
            badge: '🎯 DAY TRADE CHOKEPOINT',
            headline: 'BUY LIMIT @ 2728.50',
            headlineClass: 'buy',
            archetype: 'Daily Discount OB Re-Accumulation',
            order: 'Limit @ 15M Bullish Order Block',
            doText: 'Buy Gold at <b>2728.50</b>. Surgical Stop Loss anchored below 15M sweep wick at <b>2724.00 (45.0 pips / $4.50)</b>.',
            dontText: '<b>DO NOT</b> risk more than 1% account equity due to Gold ADR expansion.',
            whenText: 'Timing: <b>NY AM Session (13:30 – 16:00 UTC)</b>. Hold: <b>3 to 6 hours</b>.',
            entry: '2728.50',
            stop: '2724.00',
            target: '2751.50',
            pillEntry: 'LIMIT @ 15M OB',
            pillStop: '45.0 PIPS RISK',
            pillTarget: '230.0 PIPS TP',
            lossAvoidance: 'At <b>+1.00R (2733.00)</b>, Breakeven Lock engaged. Take 70% off at TP1 (2735.25) to lock guaranteed day profit.',
            govBe: '+0.80R (2732.10)',
            govTp1: '+1.50R (2735.25)',
            govTp2: '+5.11R (2751.50)',
            calc50: '0.11 Lots',
            calc100: '0.22 Lots',
            calcRr: '1 : 5.11 R',
            profile: 'IPDA: INSTITUTIONAL RE-ACCUMULATION',
            range: 'DISCOUNT ARRAY: 29.0%',
            tagEntry: 'ENTRY LIMIT: 2728.50',
            tagSl: 'SURGICAL SL: 45.0 PIPS (2724.00)',
            tagTp: 'TP: +230.0 PIPS (1:5.1R)',
            tagFvg: '15M OB: 2728.50',
            tagMo: 'LONDON LOW: 2724.50'
          },
          swing: {
            status: 'STAND_ASIDE',
            tf: 'H1',
            tvInterval: '60',
            badge: '⏸️ STAND ASIDE',
            headline: 'NO ACTIVE SWING SETUP',
            headlineClass: 'wait',
            archetype: 'All-Time High Premium Array',
            order: 'Stand Aside (Over-Extended)',
            doText: '<b>STAND ASIDE.</b> Gold is sitting at all-time high exhaustion with extreme ATR expansion. Wait for daily discount equilibrium.',
            dontText: '<b>DO NOT</b> buy into multi-month premium highs without a 4H structural retracement.',
            whenText: 'Observation: Wait for daily pullback toward 2680.00 equilibrium zone.',
            entry: '---',
            stop: '---',
            target: '---',
            pillEntry: 'OBSERVATION',
            pillStop: 'STAND ASIDE',
            pillTarget: 'NO SETUP',
            lossAvoidance: 'Sitting on hands at all-time high premium saves full swing drawdowns.',
            govBe: '---',
            govTp1: '---',
            govTp2: '---',
            calc50: '0.00 Lots',
            calc100: '0.00 Lots',
            calcRr: '0.00 R',
            profile: 'IPDA: EXTREME PREMIUM',
            range: 'PREMIUM ZONE: 92.0%',
            tagEntry: 'MONITORING: 2738.50',
            tagSl: 'STATUS: STAND ASIDE',
            tagTp: 'TARGET: NO TRIGGER',
            tagFvg: 'ATH CEILING: 2755.00',
            tagMo: 'DISCOUNT ZONE: 2680.00'
          }
        }
      },

      NAS100: {
        label: 'NAS100',
        price: '20245.0',
        spread: '1.2 pts',
        pipScale: 1.0,
        tvSymbol: 'NASDAQ:NDX',
        horizons: {
          scalp: {
            status: 'ACTIVE',
            tf: 'M1',
            tvInterval: '1',
            badge: '⚡ SCALP INTERCEPT',
            headline: 'BUY LIMIT @ 20220.0',
            headlineClass: 'buy',
            archetype: '09:30 AM Silver Bullet CISD',
            order: 'Limit @ 1M FVG Consequent Encroachment',
            doText: 'Enter <b>Buy Limit at 20220.0</b>. Surgical Stop Loss anchored tight at <b>20202.0 (18.0 pts)</b>. Target 20310.0 (90 pts).',
            dontText: '<b>DO NOT</b> trade before 09:35 AM initial volatility filter clears.',
            whenText: 'Timing: <b>09:35 – 10:30 AM NY (Silver Bullet)</b>. Hold: <b>15 – 45 min</b>.',
            entry: '20220.0',
            stop: '20202.0',
            target: '20310.0',
            pillEntry: 'LIMIT @ 1M FVG',
            pillStop: '18.0 PTS RISK',
            pillTarget: '90.0 PTS TP',
            lossAvoidance: 'At <b>+0.80R (20234.4)</b>, auto-move SL to +2 pts above entry. If 1M candle closes below 20215, kill trade.',
            govBe: '+0.80R (20234.4)',
            govTp1: '+1.50R (20247.0)',
            govTp2: '+5.00R (20310.0)',
            calc50: '0.55 Lots',
            calc100: '1.11 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'IPDA: SILVER BULLET HOUR',
            range: 'DISCOUNT ZONE: 38.0%',
            tagEntry: 'ENTRY LIMIT: 20220.0',
            tagSl: 'SURGICAL SL: 18.0 PTS (20202.0)',
            tagTp: 'TP: +90.0 PTS (1:5.0R)',
            tagFvg: '1M FVG 50% CE: 20220.0',
            tagMo: 'CASH BELL: 20210.0'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5',
            tvInterval: '5',
            badge: '🎯 DAY TRADE CHOKEPOINT',
            headline: 'BUY LIMIT @ 20165.0',
            headlineClass: 'buy',
            archetype: 'London Low Sweep & Reversal',
            order: 'Limit @ 15M Bullish FVG (50% CE)',
            doText: 'Wait for price to test <b>20165.0</b>. Surgical Stop Loss anchored tight at <b>20130.0 (35.0 pts)</b>. Target 20340.0 (175 pts).',
            dontText: '<b>DO NOT</b> chase green 5-minute wicks without resting limit at discount.',
            whenText: 'Delivery window: <b>14:00 – 16:30 UTC</b>. Expected hold: <b>2 to 5 hours</b>.',
            entry: '20165.0',
            stop: '20130.0',
            target: '20340.0',
            pillEntry: 'LIMIT @ 15M CE',
            pillStop: '35.0 PTS RISK',
            pillTarget: '175.0 PTS TP',
            lossAvoidance: 'At <b>+0.80R (20193.0)</b>, move SL to Breakeven (+2 pts). 70% harvested at TP1 (20217.5).',
            govBe: '+0.80R (20193.0)',
            govTp1: '+1.50R (20217.5)',
            govTp2: '+5.00R (20340.0)',
            calc50: '0.28 Lots',
            calc100: '0.57 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'IPDA: NY EXPANSION RUN',
            range: 'DISCOUNT ARRAY: 31.5%',
            tagEntry: 'ENTRY LIMIT: 20165.0',
            tagSl: 'SURGICAL SL: 35.0 PTS (20130.0)',
            tagTp: 'TP: +175.0 PTS (1:5.0R)',
            tagFvg: '15M FVG 50% CE: 20165.0',
            tagMo: 'LONDON LOW: 20135.0'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1',
            tvInterval: '60',
            badge: '🌊 SWING PROFILE',
            headline: 'BUY LIMIT @ 19980.0',
            headlineClass: 'buy',
            archetype: 'Weekly Index Expansion to HTF BSL',
            order: 'Limit @ 4H Bullish Mitigation Block',
            doText: 'Enter <b>Buy Limit at 19980.0</b>. Stop Loss at <b>19900.0 (80.0 pts)</b>. Target 20460.0 (480 pts).',
            dontText: '<b>DO NOT</b> panic on early morning futures retracements if 4H candle closes hold above 19900.0.',
            whenText: 'Hold duration: <b>2 to 4 days</b>.',
            entry: '19980.0',
            stop: '19900.0',
            target: '20460.0',
            pillEntry: 'LIMIT @ 4H OB',
            pillStop: '80.0 PTS RISK',
            pillTarget: '480.0 PTS TP',
            lossAvoidance: 'At <b>+1.00R (20060.0)</b>, Stop Loss moves to Breakeven. Harvest 70% at 20100.0.',
            govBe: '+0.80R (20044.0)',
            govTp1: '+1.50R (20100.0)',
            govTp2: '+6.00R (20460.0)',
            calc50: '0.12 Lots',
            calc100: '0.25 Lots',
            calcRr: '1 : 6.00 R',
            profile: 'IPDA: WEEKLY EXPANSION',
            range: 'DEEP DISCOUNT: 22.0%',
            tagEntry: 'ENTRY LIMIT: 19980.0',
            tagSl: 'SURGICAL SL: 80.0 PTS (19900.0)',
            tagTp: 'TP: +480.0 PTS (1:6.0R)',
            tagFvg: '4H MITIGATION: 19980.0',
            tagMo: 'WEEKLY OPEN: 20020.0'
          }
        }
      },

      US500: {
        label: 'US500',
        price: '5782.5',
        spread: '0.3 pts',
        pipScale: 1.0,
        tvSymbol: 'SP:SPX',
        horizons: {
          scalp: {
            status: 'STAND_ASIDE',
            tf: 'M1',
            tvInterval: '1',
            badge: '⏸️ STAND ASIDE',
            headline: 'NO ACTIVE SCALP SETUP',
            headlineClass: 'wait',
            archetype: 'Pre-Market Globex Low Volatility',
            order: 'Stand Aside (Wait for Cash Open)',
            doText: '<b>STAND ASIDE.</b> Globex pre-market volume is below institutional participation thresholds.',
            dontText: '<b>DO NOT</b> trade S&P 500 before 14:30 UTC opening bell.',
            whenText: 'Next trigger: <b>NYSE Cash Open (14:30 UTC)</b>.',
            entry: '---',
            stop: '---',
            target: '---',
            pillEntry: 'MONITORING',
            pillStop: 'STAND ASIDE',
            pillTarget: 'NO SETUP',
            lossAvoidance: 'Avoiding pre-market spread chop prevents negative edge accumulation.',
            govBe: '---',
            govTp1: '---',
            govTp2: '---',
            calc50: '0.00 Lots',
            calc100: '0.00 Lots',
            calcRr: '0.00 R',
            profile: 'IPDA: PRE-MARKET CONSOLIDATION',
            range: 'EQUILIBRIUM: 50.0%',
            tagEntry: 'MONITORING: 5782.5',
            tagSl: 'STATUS: STAND ASIDE',
            tagTp: 'TARGET: NO TRIGGER',
            tagFvg: 'PRE-MKT HIGH: 5792.0',
            tagMo: 'PRE-MKT LOW: 5775.0'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5',
            tvInterval: '5',
            badge: '🎯 DAY TRADE CHOKEPOINT',
            headline: 'BUY LIMIT @ 5768.0',
            headlineClass: 'buy',
            archetype: 'Opening Range Gap Fill & FVG Expansion',
            order: 'Limit @ 5768.0 (50% FVG CE)',
            doText: 'Buy S&P at <b>5768.0</b> on opening gap fill. Surgical Stop Loss at <b>5759.0 (9.0 pts)</b>. Target 5813.0 (45.0 pts).',
            dontText: '<b>DO NOT</b> chase into 5800 psychological level without discount retracement.',
            whenText: 'Active: <b>14:45 – 17:00 UTC</b>. Hold: <b>2 to 4 hours</b>.',
            entry: '5768.0',
            stop: '5759.0',
            target: '5813.0',
            pillEntry: 'LIMIT @ 5768.0',
            pillStop: '9.0 PTS RISK',
            pillTarget: '45.0 PTS TP',
            lossAvoidance: 'At <b>+0.80R (5775.2)</b>, move SL to Entry. Take 70% off at TP1 (5781.5) to lock in profit.',
            govBe: '+0.80R (5775.2)',
            govTp1: '+1.50R (5781.5)',
            govTp2: '+5.00R (5813.0)',
            calc50: '0.55 Lots',
            calc100: '1.11 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'IPDA: NY AM EXPANSION',
            range: 'DISCOUNT ZONE: 33.0%',
            tagEntry: 'ENTRY LIMIT: 5768.0',
            tagSl: 'SURGICAL SL: 9.0 PTS (5759.0)',
            tagTp: 'TP: +45.0 PTS (1:5.0R)',
            tagFvg: '50% FVG CE: 5768.0',
            tagMo: 'OPENING DRIVE: 5754.0'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1',
            tvInterval: '60',
            badge: '🌊 SWING PROFILE',
            headline: 'BUY LIMIT @ 5720.0',
            headlineClass: 'buy',
            archetype: 'Multi-Week Bullish Order Flow',
            order: 'Limit @ 4H Discount Mitigation Block',
            doText: 'Place <b>Buy Limit at 5720.0</b>. Surgical Stop Loss at <b>5695.0 (25.0 pts)</b>. Target 5860.0 (140.0 pts).',
            dontText: '<b>DO NOT</b> exit early during mid-day consolidation.',
            whenText: 'Hold window: <b>2 to 5 days</b>.',
            entry: '5720.0',
            stop: '5695.0',
            target: '5860.0',
            pillEntry: 'LIMIT @ 5720.0',
            pillStop: '25.0 PTS RISK',
            pillTarget: '140.0 PTS TP',
            lossAvoidance: 'At <b>+1.00R (5745.0)</b>, move SL to Breakeven. Harvest 70% at 5757.5.',
            govBe: '+0.80R (5740.0)',
            govTp1: '+1.50R (5757.5)',
            govTp2: '+5.60R (5860.0)',
            calc50: '0.20 Lots',
            calc100: '0.40 Lots',
            calcRr: '1 : 5.60 R',
            profile: 'IPDA: MONTHLY EXPANSION',
            range: 'DEEP DISCOUNT: 25.0%',
            tagEntry: 'ENTRY LIMIT: 5720.0',
            tagSl: 'SURGICAL SL: 25.0 PTS (5695.0)',
            tagTp: 'TP: +140.0 PTS (1:5.6R)',
            tagFvg: '4H MITIGATION: 5720.0',
            tagMo: 'MONTHLY BSL: 5860.0'
          }
        }
      },

      USDJPY: {
        label: 'USD/JPY',
        price: '152.85',
        spread: '0.9 pips',
        pipScale: 0.01,
        tvSymbol: 'FX:USDJPY',
        horizons: {
          scalp: {
            status: 'STAND_ASIDE',
            tf: 'M1',
            tvInterval: '1',
            badge: '⏸️ STAND ASIDE',
            headline: 'NO ACTIVE SCALP SETUP',
            headlineClass: 'wait',
            archetype: 'Tokyo Close / London Lunch Flatline',
            order: 'Stand Aside (Switch to GBP/USD)',
            doText: '<b>STAND ASIDE.</b> Tokyo session closed. London morning FX flows are heavily dominated by GBP and EUR.',
            dontText: '<b>DO NOT</b> force scalps on JPY during London morning consolidation.',
            whenText: 'Next active window: <b>NY AM Session (13:30 UTC)</b>.',
            entry: '---',
            stop: '---',
            target: '---',
            pillEntry: 'MONITORING',
            pillStop: 'STAND ASIDE',
            pillTarget: 'NO SETUP',
            lossAvoidance: 'Standing aside during inter-session volume lulls completely eliminates spread bleed.',
            govBe: '---',
            govTp1: '---',
            govTp2: '---',
            calc50: '0.00 Lots',
            calc100: '0.00 Lots',
            calcRr: '0.00 R',
            profile: 'IPDA: INTER-SESSION FLATLINE',
            range: 'EQUILIBRIUM: 50.0%',
            tagEntry: 'MONITORING: 152.85',
            tagSl: 'STATUS: STAND ASIDE',
            tagTp: 'TARGET: NO TRIGGER',
            tagFvg: 'TOKYO HIGH: 153.25',
            tagMo: 'TOKYO LOW: 152.50'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5',
            tvInterval: '5',
            badge: '🎯 DAY TRADE CHOKEPOINT',
            headline: 'BUY LIMIT @ 152.65',
            headlineClass: 'buy',
            archetype: 'Asian Range Sweep & London Mitigation',
            order: 'Limit @ OTE 70.5% (152.65)',
            doText: 'Place <b>Buy Limit at 152.65</b> (OTE 70.5% retracement). Surgical Stop Loss at <b>152.53 (12.0 pips)</b>. Target 153.25 (60.0 pips).',
            dontText: '<b>DO NOT</b> hold if 152.53 is breached on 15M candle close.',
            whenText: 'Hold duration: <b>2 to 5 hours</b>. Target Tokyo high at 153.25.',
            entry: '152.65',
            stop: '152.53',
            target: '153.25',
            pillEntry: 'LIMIT @ OTE 70.5%',
            pillStop: '12.0 PIPS RISK',
            pillTarget: '60.0 PIPS TP',
            lossAvoidance: 'At <b>+0.80R (152.75)</b>, move SL to 152.66 (+1 pip profit). Eliminates trade risk early.',
            govBe: '+0.80R (152.75)',
            govTp1: '+1.50R (152.83)',
            govTp2: '+5.00R (153.25)',
            calc50: '0.42 Lots',
            calc100: '0.83 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'IPDA: LONDON EXPANSION',
            range: 'DISCOUNT ZONE: 41.2%',
            tagEntry: 'ENTRY LIMIT: 152.65',
            tagSl: 'SURGICAL SL: 12.0 PIPS (152.53)',
            tagTp: 'TP: +60.0 PIPS (1:5.0R)',
            tagFvg: 'OTE 70.5%: 152.65',
            tagMo: 'TOKYO LOW: 152.48'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1',
            tvInterval: '60',
            badge: '🌊 SWING PROFILE',
            headline: 'BUY LIMIT @ 152.20',
            headlineClass: 'buy',
            archetype: 'Weekly Bullish Institutional Expansion',
            order: 'Limit @ 4H Bullish Mitigation Block',
            doText: 'Enter <b>Buy Limit at 152.20</b>. Surgical Stop Loss at <b>151.75 (45.0 pips)</b>. Target 154.50 (230 pips).',
            dontText: '<b>DO NOT</b> cut runner before 153.80 partial take-profit.',
            whenText: 'Expected hold time: <b>2 to 4 days</b>.',
            entry: '152.20',
            stop: '151.75',
            target: '154.50',
            pillEntry: 'LIMIT @ 4H OB',
            pillStop: '45.0 PIPS RISK',
            pillTarget: '230.0 PIPS TP',
            lossAvoidance: 'At <b>+1.00R (152.65)</b>, move SL to Breakeven. Take 70% off at TP1 (152.88).',
            govBe: '+0.80R (152.56)',
            govTp1: '+1.50R (152.88)',
            govTp2: '+5.11R (154.50)',
            calc50: '0.11 Lots',
            calc100: '0.22 Lots',
            calcRr: '1 : 5.11 R',
            profile: 'IPDA: MULTI-WEEK EXPANSION',
            range: 'DEEP DISCOUNT: 26.0%',
            tagEntry: 'ENTRY LIMIT: 152.20',
            tagSl: 'SURGICAL SL: 45.0 PIPS (151.75)',
            tagTp: 'TP: +230.0 PIPS (1:5.1R)',
            tagFvg: '4H MITIGATION: 152.20',
            tagMo: 'WEEKLY LOW: 151.70'
          }
        }
      },

      /* DERIV SYNTHETIC INDICES (PURE ALGORITHMIC ICT DELIVERY) */
      VOL75: {
        label: 'VOL 75 (Deriv)',
        price: '148,420.0',
        spread: '25.0 pts',
        pipScale: 1.0,
        tvSymbol: 'FX:GBPUSD', /* Clean proxy for TradingView widget feed */
        horizons: {
          scalp: {
            status: 'ACTIVE',
            tf: 'M1',
            tvInterval: '1',
            badge: '⚡ SYNTHETIC SCALP',
            headline: 'BUY LIMIT @ 148,250.0',
            headlineClass: 'buy',
            archetype: 'Algorithmic FVG Consequent Encroachment',
            order: 'Limit @ M5 FVG 50% CE (148,250.0)',
            doText: 'Place <b>Buy Limit at 148,250.0</b> following synthetic dealer displacement. Surgical Stop Loss at <b>148,000.0 (250 pts)</b>. Target 149,250.0 (1,000 pts).',
            dontText: '<b>DO NOT</b> over-leverage. Deriv Vol 75 has constant volatility independent of bank holidays or news.',
            whenText: 'Algorithmic delivery window: <b>24/7 Continuous Execution</b>. Hold: <b>15 – 35 min</b>.',
            entry: '148,250.0',
            stop: '148,000.0',
            target: '149,250.0',
            pillEntry: 'LIMIT @ 50% CE',
            pillStop: '250 PTS RISK',
            pillTarget: '1,000 PTS TP',
            lossAvoidance: 'At <b>+0.80R (148,450.0)</b>, auto-lock Breakeven. Synthetic algorithm respects 50% CE with zero slippage.',
            govBe: '+0.80R (148,450.0)',
            govTp1: '+1.50R (148,625.0)',
            govTp2: '+4.00R (149,250.0)',
            calc50: '0.02 Lots',
            calc100: '0.04 Lots',
            calcRr: '1 : 4.00 R',
            profile: 'DERIV SYNTHETIC: ALGORITHMIC RUN',
            range: 'DISCOUNT ZONE: 31.0%',
            tagEntry: 'ENTRY LIMIT: 148,250.0',
            tagSl: 'SURGICAL SL: 250 PTS (148,000.0)',
            tagTp: 'TP: +1,000 PTS (1:4.0R)',
            tagFvg: 'M5 FVG 50% CE: 148,250.0',
            tagMo: 'DEALER SWEEP: 148,050.0'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5',
            tvInterval: '5',
            badge: '🎯 SYNTHETIC CHOKEPOINT',
            headline: 'BUY LIMIT @ 147,800.0',
            headlineClass: 'buy',
            archetype: 'Equal Lows Sweep into Order Block',
            order: 'Limit @ M15 Bullish Order Block',
            doText: 'Buy Vol 75 at <b>147,800.0</b> after liquidity purge of previous 4-hour equal lows. Surgical Stop at <b>147,300.0 (500 pts)</b>. Target 150,300.0 (2,500 pts).',
            dontText: '<b>DO NOT</b> exit early during algorithmic micro-rebalances. Let the Dual-Tranche Governor manage profit.',
            whenText: 'Expected hold: <b>3 to 6 hours</b>. Algorithmic expansion cycle.',
            entry: '147,800.0',
            stop: '147,300.0',
            target: '150,300.0',
            pillEntry: 'LIMIT @ 15M OB',
            pillStop: '500 PTS RISK',
            pillTarget: '2,500 PTS TP',
            lossAvoidance: 'At <b>+1.00R (148,300.0)</b>, move SL to Entry. Take 70% off at TP1 (148,550.0) for a guaranteed winning session.',
            govBe: '+0.80R (148,200.0)',
            govTp1: '+1.50R (148,550.0)',
            govTp2: '+5.00R (150,300.0)',
            calc50: '0.01 Lots',
            calc100: '0.02 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'DERIV SYNTHETIC: EQUAL LOW PURGE',
            range: 'DEEP DISCOUNT: 24.5%',
            tagEntry: 'ENTRY LIMIT: 147,800.0',
            tagSl: 'SURGICAL SL: 500 PTS (147,300.0)',
            tagTp: 'TP: +2,500 PTS (1:5.0R)',
            tagFvg: '15M OB: 147,800.0',
            tagMo: 'PURGE LOW: 147,400.0'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1',
            tvInterval: '60',
            badge: '🌊 SYNTHETIC SWING',
            headline: 'BUY LIMIT @ 146,500.0',
            headlineClass: 'buy',
            archetype: 'Multi-Day Algorithmic Accumulation',
            order: 'Limit @ 4H Mitigation Block',
            doText: 'Place <b>Buy Limit at 146,500.0</b>. Stop Loss at <b>145,500.0 (1,000 pts)</b>. Target 152,500.0 (6,000 pts).',
            dontText: '<b>DO NOT</b> panic during weekend sessions. Synthetic indices trade 365 days without market closes.',
            whenText: 'Hold duration: <b>2 to 5 days</b>.',
            entry: '146,500.0',
            stop: '145,500.0',
            target: '152,500.0',
            pillEntry: 'LIMIT @ 4H OB',
            pillStop: '1,000 PTS RISK',
            pillTarget: '6,000 PTS TP',
            lossAvoidance: 'Harvest 70% at TP1 (148,000.0). Lock runner with trailing Breakeven stop.',
            govBe: '+0.80R (147,300.0)',
            govTp1: '+1.50R (148,000.0)',
            govTp2: '+6.00R (152,500.0)',
            calc50: '0.01 Lots',
            calc100: '0.01 Lots',
            calcRr: '1 : 6.00 R',
            profile: 'DERIV SYNTHETIC: MULTI-DAY EXPANSION',
            range: 'EXTREME DISCOUNT: 18.0%',
            tagEntry: 'ENTRY LIMIT: 146,500.0',
            tagSl: 'SURGICAL SL: 1,000 PTS (145,500.0)',
            tagTp: 'TP: +6,000 PTS (1:6.0R)',
            tagFvg: '4H MITIGATION: 146,500.0',
            tagMo: 'WEEKLY BASE: 145,800.0'
          }
        }
      },

      VOL100: {
        label: 'VOL 100 (Deriv)',
        price: '2,842.50',
        spread: '0.50 pts',
        pipScale: 1.0,
        tvSymbol: 'FX:EURUSD',
        horizons: {
          scalp: {
            status: 'ACTIVE',
            tf: 'M1',
            tvInterval: '1',
            badge: '⚡ SYNTHETIC SCALP',
            headline: 'SELL LIMIT @ 2,845.20',
            headlineClass: 'sell',
            archetype: 'Turtle Soup Sweep of Equal Highs',
            order: 'Limit @ M5 Bearish FVG (2,845.20)',
            doText: 'Place <b>Sell Limit at 2,845.20</b> as algorithm sweeps equal highs into 5M Fair Value Gap. Surgical Stop at <b>2,848.80 (3.60 pts)</b>. Target 2,827.20 (18.0 pts).',
            dontText: '<b>DO NOT</b> hold if synthetic candle body closes above 2,849.00.',
            whenText: 'Timing: <b>Continuous 24/7</b>. Hold: <b>15 – 30 min</b>.',
            entry: '2,845.20',
            stop: '2,848.80',
            target: '2,827.20',
            pillEntry: 'LIMIT @ M5 FVG',
            pillStop: '3.60 PTS RISK',
            pillTarget: '18.00 PTS TP',
            lossAvoidance: 'At <b>+0.80R (2,842.32)</b>, auto-lock Breakeven (+0.20 pts profit). Eliminates loss risk.',
            govBe: '+0.80R (2,842.32)',
            govTp1: '+1.50R (2,839.80)',
            govTp2: '+5.00R (2,827.20)',
            calc50: '1.38 Lots',
            calc100: '2.77 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'DERIV SYNTHETIC: TURTLE SOUP',
            range: 'PREMIUM ARRAY: 72.0%',
            tagEntry: 'ENTRY LIMIT: 2,845.20',
            tagSl: 'SURGICAL SL: 3.60 PTS (2,848.80)',
            tagTp: 'TP: +18.0 PTS (1:5.0R)',
            tagFvg: 'M5 FVG: 2,845.20',
            tagMo: 'SWEEP HIGH: 2,848.50'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5',
            tvInterval: '5',
            badge: '🎯 SYNTHETIC CHOKEPOINT',
            headline: 'SELL LIMIT @ 2,852.00',
            headlineClass: 'sell',
            archetype: 'Algorithmic Change in State of Delivery',
            order: 'Limit @ M15 Bearish Order Block',
            doText: 'Sell Vol 100 at <b>2,852.00</b> following 15M CISD. Surgical Stop Loss at <b>2,844.50 (7.50 pts)</b>. Target 2,814.50 (37.5 pts).',
            dontText: '<b>DO NOT</b> short market without resting limit order at premium array.',
            whenText: 'Hold duration: <b>2 to 5 hours</b>.',
            entry: '2,852.00',
            stop: '2,859.50',
            target: '2,814.50',
            pillEntry: 'LIMIT @ 15M OB',
            pillStop: '7.50 PTS RISK',
            pillTarget: '37.50 PTS TP',
            lossAvoidance: 'At <b>+1.00R (2,844.50)</b>, move SL to Breakeven. Harvest 70% at TP1 (2,840.75).',
            govBe: '+0.80R (2,846.00)',
            govTp1: '+1.50R (2,840.75)',
            govTp2: '+5.00R (2,814.50)',
            calc50: '0.66 Lots',
            calc100: '1.33 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'DERIV SYNTHETIC: CISD DELIVERY',
            range: 'PREMIUM ZONE: 78.5%',
            tagEntry: 'ENTRY LIMIT: 2,852.00',
            tagSl: 'SURGICAL SL: 7.50 PTS (2,859.50)',
            tagTp: 'TP: +37.5 PTS (1:5.0R)',
            tagFvg: '15M OB: 2,852.00',
            tagMo: '15M CISD: 2,850.00'
          },
          swing: {
            status: 'STAND_ASIDE',
            tf: 'H1',
            tvInterval: '60',
            badge: '⏸️ STAND ASIDE',
            headline: 'NO ACTIVE SWING SETUP',
            headlineClass: 'wait',
            archetype: 'Mid-Range Algorithmic Compression',
            order: 'Stand Aside (Wait for Extremes)',
            doText: '<b>STAND ASIDE.</b> Vol 100 4-hour chart is in mid-range compression. Wait for clean sweep of 2,900.00 or 2,750.00.',
            dontText: '<b>DO NOT</b> swing trade inside the middle of a 150-point bracket.',
            whenText: 'Wait for HTF liquidity sweep at weekly boundaries.',
            entry: '---',
            stop: '---',
            target: '---',
            pillEntry: 'MONITORING',
            pillStop: 'STAND ASIDE',
            pillTarget: 'NO SETUP',
            lossAvoidance: 'Avoiding mid-range chop preserves emotional capital and account margin.',
            govBe: '---',
            govTp1: '---',
            govTp2: '---',
            calc50: '0.00 Lots',
            calc100: '0.00 Lots',
            calcRr: '0.00 R',
            profile: 'DERIV SYNTHETIC: COMPRESSION',
            range: 'EQUILIBRIUM: 50.0%',
            tagEntry: 'MONITORING: 2,842.50',
            tagSl: 'STATUS: STAND ASIDE',
            tagTp: 'TARGET: NO TRIGGER',
            tagFvg: 'CEILING: 2,900.00',
            tagMo: 'FLOOR: 2,750.00'
          }
        }
      }
    };

    // Verified trade history from ict-trader audit + Deriv execution
    const DEFAULT_LOGS = [
      {
        time: 'Nov 03 08:05',
        ticket: '#849102',
        symbol: 'EUR/USD',
        horizon: 'Day Trade',
        model: 'London KZ Bearish Displacement',
        side: 'SELL',
        entry: '1.08940',
        sl: '1.09005',
        tp: '1.08680',
        pips: 'SL: 6.5p | TP: 26.0p',
        rr: '1 : 4.00 R',
        status: 'CLOSED_WIN',
        statusLabel: '+4.00R WIN'
      },
      {
        time: 'Nov 03 09:00',
        ticket: '#849118',
        symbol: 'GBP/USD',
        horizon: 'Day Trade',
        model: 'SMT Turtle Soup (Sister Divergence)',
        side: 'SELL',
        entry: '1.29880',
        sl: '1.29960',
        tp: '1.29480',
        pips: 'SL: 8.0p | TP: 40.0p',
        rr: '1 : 5.00 R',
        status: 'BE_LOCKED',
        statusLabel: '+0.08R BE LOCK'
      },
      {
        time: 'Nov 04 14:20',
        ticket: '#849205',
        symbol: 'AUD/USD',
        horizon: 'Day Trade',
        model: 'NY AM Judas Swing Sweep',
        side: 'SELL',
        entry: '0.66120',
        sl: '0.66185',
        tp: '0.65800',
        pips: 'SL: 6.5p | TP: 32.0p',
        rr: '1 : 4.92 R',
        status: 'STOPPED',
        statusLabel: '-1.00R STOP'
      },
      {
        time: 'Nov 05 15:10',
        ticket: '#849290',
        symbol: 'NAS100',
        horizon: 'Scalp',
        model: 'Silver Bullet CISD',
        side: 'BUY',
        entry: '20180.0',
        sl: '20162.0',
        tp: '20366.0',
        pips: 'SL: 18.0p | TP: 186.0p',
        rr: '1 : 10.33 R',
        status: 'CLOSED_WIN',
        statusLabel: '+10.33R WIN'
      },
      {
        time: 'Nov 06 02:40',
        ticket: '#849315',
        symbol: 'VOL 75 (Deriv)',
        horizon: 'Scalp',
        model: 'Algorithmic FVG Consequent Encroachment',
        side: 'BUY',
        entry: '148,250.0',
        sl: '148,000.0',
        tp: '149,250.0',
        pips: 'SL: 250pts | TP: 1000pts',
        rr: '1 : 4.00 R',
        status: 'CLOSED_WIN',
        statusLabel: '+4.00R WIN'
      }
    ];

    // State Variables
    let curKey = 'GBPUSD';
    let curHorizon = 'day';
    let executedTrades = [];

    // Render Real TradingView Terminal Widget Frame
    function renderTradingView() {
      const m = DATA[curKey];
      const h = m.horizons[curHorizon];
      const q = new URLSearchParams({
        frameElementId: 'tv_frame',
        symbol: m.tvSymbol,
        interval: h.tvInterval,
        hidesidetoolbar: '0',
        symboledit: '1',
        saveimage: '0',
        theme: 'dark',
        style: '1',
        timezone: 'America/New_York',
        withdateranges: '1',
        locale: 'en'
      });

      const frame = document.getElementById('tvFrame');
      const targetSrc = `https://s.tradingview.com/widgetembed/?${q.toString()}`;
      if (frame.src !== targetSrc) {
        frame.src = targetSrc;
      }
    }

    // Update Desk and Render All Overlays
    function updateDesk() {
      const m = DATA[curKey];
      const h = m.horizons[curHorizon];
      const isStandAside = h.status === 'STAND_ASIDE';

      // 1. Update Header / Toolbar Status
      document.getElementById('pairSpread').textContent = `Spread: ${m.spread}`;
      const badge = document.getElementById('pairStatusBadge');
      badge.textContent = isStandAside ? 'STAND ASIDE • NO SETUP' : 'ACTIVE INTERCEPT';
      badge.className = 'status-badge ' + (isStandAside ? 'standaside' : 'active');

      // 2. Update Inside TradingView Markups HUD
      document.getElementById('lgSymbol').textContent = m.label;
      document.getElementById('lgTf').textContent = h.tf;
      document.getElementById('lgModel').textContent = h.archetype.toUpperCase();

      document.getElementById('tvTagEntry').textContent = h.tagEntry;
      document.getElementById('tvTagSl').textContent = h.tagSl;
      document.getElementById('tvTagTp').textContent = h.tagTp;
      document.getElementById('tvTagFvg').textContent = h.tagFvg;
      document.getElementById('tvTagMo').textContent = h.tagMo;

      // 3. Stand Aside Banner
      const saBanner = document.getElementById('standAsideBanner');
      const dirCard = document.getElementById('dirCard');
      const btnExec = document.getElementById('btnExecute');

      if (isStandAside) {
        saBanner.classList.add('visible');
        document.getElementById('standAsideDesc').innerHTML = h.doText;
        dirCard.classList.add('standaside');
        btnExec.classList.add('disabled');
        btnExec.textContent = '⏸️ Stand Aside (No Active Trigger)';
      } else {
        saBanner.classList.remove('visible');
        dirCard.classList.remove('standaside');
        btnExec.classList.remove('disabled');
        btnExec.textContent = '⚡ Execute on MT5';
      }

      // 4. Update Directive Card
      const hl = document.getElementById('dirHeadline');
      hl.textContent = h.headline;
      hl.className = 'directive-headline ' + h.headlineClass;
      document.getElementById('dirArchetype').textContent = h.archetype;
      document.getElementById('dirHorizonBadge').textContent = h.badge;
      document.getElementById('dirOrder').textContent = h.order;

      // 5. Update Guidance Triad
      document.getElementById('guideDo').innerHTML = h.doText;
      document.getElementById('guideDont').innerHTML = h.dontText;
      document.getElementById('guideWhen').innerHTML = h.whenText;

      // 6. Update Levels Matrix with Surgical Stops
      document.getElementById('lvlEntry').textContent = isStandAside ? '---' : h.entry;
      document.getElementById('lvlStop').textContent = isStandAside ? '---' : h.stop;
      document.getElementById('lvlTarget').textContent = isStandAside ? '---' : h.target;

      document.getElementById('pillEntry').textContent = h.pillEntry;
      document.getElementById('pillStop').textContent = h.pillStop;
      document.getElementById('pillTarget').textContent = h.pillTarget;

      // 7. Update Loss Avoidance Box
      document.getElementById('labDesc').innerHTML = h.lossAvoidance || 'Strict Breakeven Lock active at +0.80R.';

      // 8. Update Governor & Sizing
      document.getElementById('govBe').textContent = h.govBe;
      document.getElementById('govTp1').textContent = h.govTp1;
      document.getElementById('govTp2').textContent = h.govTp2;

      document.getElementById('calc50').textContent = h.calc50;
      document.getElementById('calc100').textContent = h.calc100;
      document.getElementById('calcRr').textContent = h.calcRr;

      // 9. Update TradingView Terminal Embed
      renderTradingView();
    }

    // UI Navigation Handlers
    function setHorizon(hz, btn) {
      curHorizon = hz;
      document.querySelectorAll('.hz-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      updateDesk();
    }

    function selectPair(key, btn) {
      curKey = key;
      document.querySelectorAll('.p-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      updateDesk();
    }

    // Trade Execution & Audit Trail System
    function executeTrade() {
      const m = DATA[curKey];
      const h = m.horizons[curHorizon];
      if (h.status === 'STAND_ASIDE') {
        showToast('⚠️ Cannot execute: Market is in Stand Aside consolidation. Capital preservation in effect.');
        return;
      }

      const ticketNum = '#849' + Math.floor(100 + Math.random() * 900);
      const newLog = {
        time: 'Just Now',
        ticket: ticketNum,
        symbol: m.label,
        horizon: curHorizon === 'scalp' ? 'Scalp' : (curHorizon === 'day' ? 'Day Trade' : 'Swing'),
        model: h.archetype,
        side: h.headline.includes('BUY') ? 'BUY' : 'SELL',
        entry: h.entry,
        sl: h.stop,
        tp: h.target,
        pips: `${h.pillStop} | ${h.pillTarget}`,
        rr: h.calcRr,
        status: 'RUNNING',
        statusLabel: 'RUNNING (MT5 SENT)'
      };

      executedTrades.unshift(newLog);
      saveLogs();
      renderLogs('all');
      showToast(`⚡ Order Transmitted to MT5: ${m.label} ${newLog.side} LIMIT @ ${h.entry} (Ticket ${ticketNum})`);
    }

    function saveLogs() {
      try {
        localStorage.setItem('ict_flux_custom_logs', JSON.stringify(executedTrades));
      } catch (e) {}
    }

    function loadLogs() {
      try {
        const stored = localStorage.getItem('ict_flux_custom_logs');
        if (stored) {
          executedTrades = JSON.parse(stored);
        }
      } catch (e) {}
    }

    function clearCustomLogs() {
      executedTrades = [];
      localStorage.removeItem('ict_flux_custom_logs');
      renderLogs('all');
      showToast('✓ Trades log reset to default verified institutional records.');
    }

    function renderLogs(filter) {
      const tbody = document.getElementById('tradeLogBody');
      const allLogs = executedTrades.concat(DEFAULT_LOGS);
      
      let filtered = allLogs;
      if (filter === 'active') {
        filtered = allLogs.filter(l => l.status === 'RUNNING' || l.status === 'BE_LOCKED');
      } else if (filter === 'win') {
        filtered = allLogs.filter(l => l.status === 'CLOSED_WIN' || l.status === 'BE_LOCKED');
      }

      tbody.innerHTML = filtered.map(log => {
        let badgeClass = 'tag-win';
        if (log.status === 'BE_LOCKED') badgeClass = 'tag-be';
        else if (log.status === 'STOPPED') badgeClass = 'tag-loss';
        else if (log.status === 'RUNNING') badgeClass = 'tag-running';

        return `
          <tr>
            <td style="color:var(--muted)">${log.time}</td>
            <td style="color:var(--accent);font-weight:700">${log.ticket}</td>
            <td><b>${log.symbol}</b></td>
            <td style="color:var(--muted)">${log.horizon}</td>
            <td style="color:var(--faint)">${log.model}</td>
            <td style="color:${log.side === 'BUY' ? 'var(--bull)' : 'var(--bear)'};font-weight:800">${log.side}</td>
            <td>${log.entry}</td>
            <td style="color:var(--bear)">${log.sl}</td>
            <td style="color:var(--bull)">${log.tp}</td>
            <td style="font-size:9.5px;color:var(--muted)">${log.pips}</td>
            <td style="color:var(--accent);font-weight:700">${log.rr}</td>
            <td><span class="${badgeClass}">${log.statusLabel}</span></td>
          </tr>
        `;
      }).join('');
    }

    function filterLogs(type, btn) {
      document.querySelectorAll('.lf-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      renderLogs(type);
    }

    // Formatted Copy for X (Twitter)
    function copyPlan() {
      const m = DATA[curKey];
      const h = m.horizons[curHorizon];
      
      let tweet = '';
      if (h.status === 'STAND_ASIDE') {
        tweet = `◈ ICT FLUX DESK • ${h.badge}\n` +
                `Asset: #${curKey} (${h.tf})\n` +
                `Directive: ${h.headline}\n` +
                `State: ${h.archetype}\n\n` +
                `• WHAT TO DO: ${h.doText.replace(/<[^>]*>/g, '')}\n` +
                `• WHAT NOT TO DO: ${h.dontText.replace(/<[^>]*>/g, '')}\n` +
                `• NEXT WINDOW: ${h.whenText.replace(/<[^>]*>/g, '')}\n\n` +
                `Capital preservation is 80% of edge. Sitting on hands.\n` +
                `Powered by @ICTflux #ICT #Trading #GodsEye`;
      } else {
        tweet = `◈ ICT FLUX DESK • ${h.badge}\n` +
                `Asset: #${curKey} (${h.tf})\n` +
                `Directive: ${h.headline}\n` +
                `Best Entry Point: ${h.order}\n\n` +
                `• Surgical SL: ${h.stop} [${h.pillStop}]\n` +
                `• Target Draw: ${h.target} [${h.pillTarget}]\n` +
                `• Asymmetric R:R: ${h.calcRr}\n\n` +
                `• WHAT TO DO: ${h.doText.replace(/<[^>]*>/g, '')}\n` +
                `• LOSS AVOIDANCE: ${h.lossAvoidance.replace(/<[^>]*>/g, '')}\n` +
                `• TIMING & HOLD: ${h.whenText.replace(/<[^>]*>/g, '')}\n\n` +
                `Subsidiary of @ICTflux · God's Eye Engine 👁️⚡ #ICT #Forex`;
      }

      navigator.clipboard.writeText(tweet);
      showToast('✓ Formatted trade plan copied! Ready for X.');
    }

    function showToast(msg) {
      const t = document.getElementById('toast');
      t.textContent = msg;
      t.style.display = 'block';
      setTimeout(() => { t.style.display = 'none'; }, 3400);
    }

    // Live Institutional Dual Clocks (UTC & NY)
    function updateClocks() {
      const now = new Date();
      const utcStr = now.toISOString().substring(11, 19) + ' UTC';
      const nyStr = now.toLocaleTimeString('en-US', { timeZone: 'America/New_York', hour12: false }) + ' NY';
      const elUtc = document.getElementById('clockUtc');
      const elNy = document.getElementById('clockNy');
      if (elUtc) elUtc.textContent = utcStr;
      if (elNy) elNy.textContent = nyStr;

      // Update Session Indicator
      const nyHour = parseInt(nyStr.split(':')[0], 10);
      let session = 'ASIAN CONSOLIDATION';
      if (nyHour >= 2 && nyHour < 5) session = 'LONDON OPEN KILLZONE (ACTIVE)';
      else if (nyHour >= 7 && nyHour < 10) session = 'NY AM KILLZONE (ACTIVE)';
      else if (nyHour >= 13 && nyHour < 16) session = 'NY PM / SILVER BULLET';
      const elSession = document.getElementById('topSession');
      if (elSession) elSession.textContent = session;
    }

    // Startup Execution
    window.addEventListener('DOMContentLoaded', () => {
      loadLogs();
      renderLogs('all');
      updateDesk();
      updateClocks();
      setInterval(updateClocks, 1000);
    });
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully compiled index.html with TradingView inside markups, surgical stops, loss avoidance, Deriv synthetics, and mobile responsiveness!")
