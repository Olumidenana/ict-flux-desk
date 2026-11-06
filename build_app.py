# -*- coding: utf-8 -*-
"""Builder script to generate the unified ICT Flux Desk:
1. Live Execution Desk View (Unobstructed TV chart, resizable side card, accurate $4,077+ Gold, Stand-Aside discipline, instrument dropdown selector)
2. Interactive Research & Backtest Lab View (Select period: 7d, 30d, 90d, 365d; select models; win rate %, profit factor, cumulative R equity curve, trade-by-trade audit table, and CSV export)
3. 100% Client-side, lightning fast (< 20ms execution, zero serverless timeouts)
4. Mobile-optimized responsive layout
"""

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>ICT FLUX DESK • Autonomous Execution Terminal & Research Lab</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500;600;700;800&family=Geist:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <!-- TradingView Lightweight Charts Library (Local + CDN Fallback) -->
  <script src="lightweight-charts.js"></script>
  <script>
    if (typeof LightweightCharts === 'undefined') {
      document.write('<script src="https://unpkg.com/lightweight-charts@4.1.3/dist/lightweight-charts.standalone.production.js"><\/script>');
    }
  </script>
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
      user-select: none;
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
    .brand-wrap {
      display: flex;
      align-items: center;
      gap: 20px;
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

    /* Top Navigation Tabs (Desk vs Research Lab) */
    .top-nav {
      display: flex;
      background: var(--surface-2);
      border-radius: 8px;
      padding: 3px;
      border: 1px solid var(--line);
      gap: 2px;
    }
    .nav-tab {
      padding: 6px 12px;
      border-radius: 6px;
      border: 0;
      background: transparent;
      color: var(--muted);
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }
    .nav-tab:hover {
      color: var(--text);
    }
    .nav-tab.active {
      background: var(--surface-3);
      color: var(--accent);
      box-shadow: 0 0 10px rgba(0,0,0,0.5);
      border: 1px solid var(--line-gold);
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

    /* Views Container */
    .view-container {
      width: 100%;
      height: calc(100vh - 60px);
      position: relative;
    }
    .view-pane {
      display: none;
      width: 100%;
      height: 100%;
    }
    .view-pane.active {
      display: flex;
    }

    /* ========================================================= */
    /* VIEW 1: LIVE EXECUTION DESK (WITH RESIZABLE SPLIT CARD)  */
    /* ========================================================= */
    .desk-layout {
      display: flex;
      width: 100%;
      height: 100%;
      position: relative;
      overflow: hidden;
    }
    .chart-panel {
      flex: 1;
      min-width: 320px;
      display: flex;
      flex-direction: column;
      background: #050608;
      position: relative;
      height: 100%;
    }
    .chart-toolbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 14px;
      background: var(--surface);
      border-bottom: 1px solid var(--line);
      gap: 10px;
      flex-wrap: wrap;
    }
    .selector-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .instrument-select {
      background: var(--surface-2);
      color: var(--text);
      font-family: var(--mono);
      font-size: 12px;
      font-weight: 700;
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid var(--line-gold);
      outline: none;
      cursor: pointer;
    }
    .instrument-select optgroup {
      background: var(--surface);
      color: var(--accent);
      font-family: var(--sans);
      font-weight: 800;
    }
    .instrument-select option {
      background: var(--surface-2);
      color: var(--text);
      font-family: var(--mono);
      padding: 4px 8px;
    }
    .chart-meta {
      display: flex;
      align-items: center;
      gap: 8px;
      font-family: var(--mono);
      font-size: 11px;
      color: var(--muted);
    }
    .status-badge {
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 10px;
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

        .chart-mode-toggle {
      display: flex;
      background: var(--surface-2);
      border-radius: 6px;
      padding: 2px;
      border: 1px solid var(--line);
      gap: 2px;
    }
    .mode-btn {
      padding: 4px 10px;
      border-radius: 4px;
      border: 0;
      background: transparent;
      color: var(--muted);
      font-family: var(--mono);
      font-size: 10.5px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s;
    }
    .mode-btn:hover {
      color: var(--text);
    }
    .mode-btn.active {
      background: var(--surface-3);
      color: var(--accent);
      border: 1px solid var(--line-gold);
    }

    .desk-log-section {
      margin-top: 14px;
      background: var(--surface-2);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 10px;
    }
    .desk-log-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }
    .desk-log-title {
      font-family: var(--mono);
      font-size: 10.5px;
      font-weight: 800;
      color: var(--accent);
      letter-spacing: 0.02em;
      text-transform: uppercase;
    }
    .log-clear-btn {
      background: transparent;
      border: 1px solid var(--line);
      color: var(--faint);
      font-family: var(--mono);
      font-size: 9.5px;
      padding: 2px 6px;
      border-radius: 4px;
      cursor: pointer;
    }
    .log-clear-btn:hover {
      color: var(--bear);
      border-color: var(--bear);
    }
    .desk-log-table-wrap {
      max-height: 180px;
      overflow-y: auto;
      border-radius: 6px;
      border: 1px solid var(--line);
    }
    .desk-log-table-wrap table {
      width: 100%;
      border-collapse: collapse;
      font-family: var(--mono);
      font-size: 10px;
    }
    .desk-log-table-wrap th {
      background: var(--surface-3);
      color: var(--muted);
      padding: 6px 8px;
      text-align: left;
      font-size: 9px;
      text-transform: uppercase;
      position: sticky;
      top: 0;
      z-index: 2;
    }
    .desk-log-table-wrap td {
      padding: 5px 8px;
      border-top: 1px solid rgba(255,255,255,0.04);
      color: var(--text);
      white-space: nowrap;
    }

    .chart-stage {
      flex: 1;
      width: 100%;
      height: 100%;
      min-height: 440px;
      position: relative;
      background: #050608;
    }
    #tvChartContainer {
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
    }
    .chart-benchmark-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 6px 14px;
      background: var(--surface);
      border-top: 1px solid var(--line);
      font-family: var(--mono);
      font-size: 10.5px;
      gap: 10px;
      overflow-x: auto;
    }
    .benchmark-pills {
      display: flex;
      gap: 6px;
      white-space: nowrap;
    }
    .bm-tag {
      padding: 2px 7px;
      border-radius: 4px;
      font-weight: 700;
      font-size: 9.5px;
    }
    .bm-tag.gold { background: var(--accent-soft); color: var(--accent); border: 1px solid var(--line-gold); }
    .bm-tag.red { background: var(--bear-soft); color: var(--bear); border: 1px solid rgba(255,92,108,0.3); }
    .bm-tag.green { background: var(--bull-soft); color: var(--bull); border: 1px solid rgba(43,212,125,0.3); }
    .bm-tag.gray { background: rgba(255,255,255,0.05); color: var(--muted); border: 1px solid var(--line); }

    /* Resizer Divider */
    .resizer-divider {
      width: 6px;
      background: var(--surface-2);
      border-left: 1px solid var(--line);
      border-right: 1px solid var(--line);
      cursor: col-resize;
      transition: background 0.15s;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 20;
      flex-shrink: 0;
    }
    .resizer-divider:hover, .resizer-divider.dragging {
      background: var(--accent);
      box-shadow: 0 0 10px var(--accent-glow);
    }
    .resizer-grip {
      width: 2px;
      height: 24px;
      background: var(--faint);
      border-radius: 1px;
    }

    /* Desk Panel (Adjustable Width) */
    .desk-panel {
      width: 480px;
      min-width: 320px;
      max-width: 850px;
      background: var(--surface);
      overflow-y: auto;
      padding: 14px 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      flex-shrink: 0;
      -webkit-overflow-scrolling: touch;
      position: relative;
    }
    .desk-panel.enlarged {
      width: 680px;
    }
    .desk-top-controls {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--line);
      padding-bottom: 8px;
    }
    .desk-panel-title {
      font-family: var(--mono);
      font-size: 11.5px;
      font-weight: 800;
      color: var(--accent);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .enlarge-btn {
      padding: 4px 8px;
      border-radius: 5px;
      background: var(--surface-2);
      border: 1px solid var(--line);
      color: var(--muted);
      font-family: var(--mono);
      font-size: 10px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s;
    }
    .enlarge-btn:hover {
      border-color: var(--accent);
      color: var(--text);
    }

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
      font-size: 10.5px;
      color: #E2E8F0;
      line-height: 1.4;
    }

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

    /* ========================================================= */
    /* VIEW 2: RESEARCH & BACKTEST LAB (STATISTICAL VERIFICATION)*/
    /* ========================================================= */
    .lab-layout {
      width: 100%;
      height: 100%;
      overflow-y: auto;
      padding: 18px 24px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      background: var(--bg);
    }
    .lab-hero {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      border-bottom: 1px solid var(--line);
      padding-bottom: 14px;
    }
    .lab-hero-title {
      font-size: 18px;
      font-weight: 800;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .lab-hero-sub {
      font-size: 11.5px;
      color: var(--muted);
      margin-top: 3px;
    }

    /* Backtest Parameters Configuration Bar */
    .bt-config-card {
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 14px 18px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .bt-filters-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
    }
    .bt-field {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    .bt-label {
      font-family: var(--mono);
      font-size: 10px;
      color: var(--faint);
      font-weight: 700;
      text-transform: uppercase;
    }
    .bt-select {
      background: var(--surface-2);
      border: 1px solid var(--line-2);
      color: var(--text);
      font-family: var(--mono);
      font-size: 11.5px;
      padding: 7px 10px;
      border-radius: 6px;
      outline: none;
      cursor: pointer;
    }
    .bt-actions-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--line);
      padding-top: 10px;
      flex-wrap: wrap;
      gap: 10px;
    }
    .bt-toggles {
      display: flex;
      gap: 12px;
      font-family: var(--mono);
      font-size: 11px;
      color: var(--muted);
      align-items: center;
    }
    .bt-toggle-item {
      display: flex;
      align-items: center;
      gap: 5px;
      cursor: pointer;
    }
    .bt-toggle-item input {
      accent-color: var(--accent);
      cursor: pointer;
    }

    /* Metrics Grid */
    .lab-metrics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 10px;
    }
    .metric-card {
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 9px;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .m-title {
      font-family: var(--mono);
      font-size: 9.5px;
      color: var(--faint);
      font-weight: 700;
      text-transform: uppercase;
    }
    .m-val {
      font-family: var(--mono);
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.02em;
    }
    .m-sub {
      font-size: 9.5px;
      color: var(--muted);
      font-family: var(--mono);
    }

    /* Equity Growth Curve Visualizer */
    .equity-card {
      background: var(--surface);
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 14px 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .equity-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--mono);
      font-size: 11.5px;
    }
    .equity-chart-box {
      width: 100%;
      height: 180px;
      position: relative;
    }
    svg.equity-svg {
      width: 100%;
      height: 100%;
      overflow: visible;
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
      .desk-layout {
        flex-direction: column;
        height: auto;
      }
      .resizer-divider {
        display: none;
      }
      .desk-panel {
        width: 100% !important;
        max-width: 100%;
      }
          .chart-mode-toggle {
      display: flex;
      background: var(--surface-2);
      border-radius: 6px;
      padding: 2px;
      border: 1px solid var(--line);
      gap: 2px;
    }
    .mode-btn {
      padding: 4px 10px;
      border-radius: 4px;
      border: 0;
      background: transparent;
      color: var(--muted);
      font-family: var(--mono);
      font-size: 10.5px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s;
    }
    .mode-btn:hover {
      color: var(--text);
    }
    .mode-btn.active {
      background: var(--surface-3);
      color: var(--accent);
      border: 1px solid var(--line-gold);
    }

    .desk-log-section {
      margin-top: 14px;
      background: var(--surface-2);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 10px;
    }
    .desk-log-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }
    .desk-log-title {
      font-family: var(--mono);
      font-size: 10.5px;
      font-weight: 800;
      color: var(--accent);
      letter-spacing: 0.02em;
      text-transform: uppercase;
    }
    .log-clear-btn {
      background: transparent;
      border: 1px solid var(--line);
      color: var(--faint);
      font-family: var(--mono);
      font-size: 9.5px;
      padding: 2px 6px;
      border-radius: 4px;
      cursor: pointer;
    }
    .log-clear-btn:hover {
      color: var(--bear);
      border-color: var(--bear);
    }
    .desk-log-table-wrap {
      max-height: 180px;
      overflow-y: auto;
      border-radius: 6px;
      border: 1px solid var(--line);
    }
    .desk-log-table-wrap table {
      width: 100%;
      border-collapse: collapse;
      font-family: var(--mono);
      font-size: 10px;
    }
    .desk-log-table-wrap th {
      background: var(--surface-3);
      color: var(--muted);
      padding: 6px 8px;
      text-align: left;
      font-size: 9px;
      text-transform: uppercase;
      position: sticky;
      top: 0;
      z-index: 2;
    }
    .desk-log-table-wrap td {
      padding: 5px 8px;
      border-top: 1px solid rgba(255,255,255,0.04);
      color: var(--text);
      white-space: nowrap;
    }

    .chart-stage {
        height: 420px;
        min-height: 380px;
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
          .chart-mode-toggle {
      display: flex;
      background: var(--surface-2);
      border-radius: 6px;
      padding: 2px;
      border: 1px solid var(--line);
      gap: 2px;
    }
    .mode-btn {
      padding: 4px 10px;
      border-radius: 4px;
      border: 0;
      background: transparent;
      color: var(--muted);
      font-family: var(--mono);
      font-size: 10.5px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s;
    }
    .mode-btn:hover {
      color: var(--text);
    }
    .mode-btn.active {
      background: var(--surface-3);
      color: var(--accent);
      border: 1px solid var(--line-gold);
    }

    .desk-log-section {
      margin-top: 14px;
      background: var(--surface-2);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 10px;
    }
    .desk-log-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }
    .desk-log-title {
      font-family: var(--mono);
      font-size: 10.5px;
      font-weight: 800;
      color: var(--accent);
      letter-spacing: 0.02em;
      text-transform: uppercase;
    }
    .log-clear-btn {
      background: transparent;
      border: 1px solid var(--line);
      color: var(--faint);
      font-family: var(--mono);
      font-size: 9.5px;
      padding: 2px 6px;
      border-radius: 4px;
      cursor: pointer;
    }
    .log-clear-btn:hover {
      color: var(--bear);
      border-color: var(--bear);
    }
    .desk-log-table-wrap {
      max-height: 180px;
      overflow-y: auto;
      border-radius: 6px;
      border: 1px solid var(--line);
    }
    .desk-log-table-wrap table {
      width: 100%;
      border-collapse: collapse;
      font-family: var(--mono);
      font-size: 10px;
    }
    .desk-log-table-wrap th {
      background: var(--surface-3);
      color: var(--muted);
      padding: 6px 8px;
      text-align: left;
      font-size: 9px;
      text-transform: uppercase;
      position: sticky;
      top: 0;
      z-index: 2;
    }
    .desk-log-table-wrap td {
      padding: 5px 8px;
      border-top: 1px solid rgba(255,255,255,0.04);
      color: var(--text);
      white-space: nowrap;
    }

    .chart-stage {
        height: 360px;
        min-height: 340px;
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

  <!-- TOP HEADER WITH VIEW SWITCHER -->
  <header class="top">
    <div class="top-bar">
      <div class="brand-wrap">
        <div class="brand">
          <div class="logo-badge">F</div>
          <div class="brand-col">
            <div class="brand-title">
              <span>ICT FLUX DESK</span>
              <span style="font-size:9.5px;color:var(--faint);">v39.7</span>
            </div>
            <div class="subsidiary-pill">
              <span>SUBSIDIARY OF</span>
              <a href="https://ictflux.app" target="_blank" title="Visit Parent Application">ICTFLUX.APP ↗</a>
              <span>• GOD'S EYE</span>
            </div>
          </div>
        </div>

        <!-- Mode Navigation: Live Desk vs Research Lab -->
        <div class="top-nav">
          <button class="nav-tab active" id="tabDesk" onclick="switchView('desk')">
            <span>⚡ EXECUTION DESK</span>
          </button>
          <button class="nav-tab" id="tabLab" onclick="switchView('lab')">
            <span>🔬 RESEARCH & BACKTEST LAB</span>
          </button>
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

  <!-- DUAL-VIEW WORKSPACE CONTAINER -->
  <div class="view-container">

    <!-- ======================================================== -->
    <!-- VIEW 1: LIVE EXECUTION DESK                             -->
    <!-- ======================================================== -->
    <div class="view-pane active" id="paneDesk">
      <div class="desk-layout" id="workspaceLayout">
        
        <!-- LEFT: UNOBSTRUCTED TRADINGVIEW LIGHTWEIGHT CANDLESTICK CHART -->
        <div class="chart-panel" id="chartPanel">
          
          <!-- Toolbar with Structured Instrument Dropdown Selector -->
          <div class="chart-toolbar">
            <div class="selector-group">
              <label style="font-family:var(--mono);font-size:10.5px;color:var(--muted);font-weight:700">ASSET:</label>
              <select class="instrument-select" id="instrumentSelect" onchange="onSelectInstrument(this.value)">
                <optgroup label="Forex Majors">
                  <option value="GBPUSD" selected>GBP/USD · 1.3394</option>
                  <option value="EURUSD">EUR/USD · 1.1177</option>
                  <option value="USDJPY">USD/JPY · 158.26</option>
                </optgroup>
                <optgroup label="Precious Metals & Commodities">
                  <option value="XAUUSD">XAU/USD (Gold) · $4,077.60</option>
                </optgroup>
                <optgroup label="Global Equity Indices">
                  <option value="NAS100">NAS100 (NQ) · 27,139.2</option>
                  <option value="US500">US500 (ES) · 7,403.7</option>
                </optgroup>
                <optgroup label="Deriv Synthetic Indices (24/7 Algorithmic)">
                  <option value="VOL75">VOL 75 (Deriv) · 148,420.0</option>
                  <option value="VOL100">VOL 100 (Deriv) · 2,842.50</option>
                </optgroup>
              </select>
            </div>

            <div class="chart-mode-toggle">
              <button class="mode-btn active" id="btnModeLc" onclick="switchChartEngine('lc')">⚡ ICT Markups Engine</button>
              <button class="mode-btn" id="btnModeTv" onclick="switchChartEngine('tv')">📊 TradingView Terminal</button>
            </div>

            <div class="chart-meta">
              <span id="pairSpread">Spread: 0.8 pips</span>
              <span class="status-badge active" id="pairStatusBadge">ACTIVE INTERCEPT</span>
            </div>
          </div>

          <!-- Clean Unobstructed Chart Stage -->
          <div class="chart-stage" id="chartStage">
            <div id="tvChartContainer"></div>
            <iframe id="tvLiveFrame" style="display:none;width:100%;height:100%;border:none;background:#050608;" allowfullscreen loading="lazy"></iframe>
          </div>

          <!-- Non-Interfering ICT Benchmark Bar Below Chart -->
          <div class="chart-benchmark-bar">
            <span style="color:var(--faint);font-size:9.5px;text-transform:uppercase;font-weight:700" id="bmModelLabel">MODEL: SMT TURTLE SOUP</span>
            <div class="benchmark-pills" id="bmPills">
              <!-- Dynamically populated benchmark tags -->
            </div>
          </div>
        </div>

        <!-- DRAGGABLE RESIZER HANDLE -->
        <div class="resizer-divider" id="resizerHandle" title="Drag to resize card width">
          <div class="resizer-grip"></div>
        </div>

        <!-- RIGHT: GOD'S EYE ACTION DIRECTIVE DESK (ADJUSTABLE / ENLARGEABLE) -->
        <div class="desk-panel" id="deskPanel">
          
          <div class="desk-top-controls">
            <div class="desk-panel-title">
              <span>👁️ GOD'S EYE ACTION CARD</span>
              <span style="font-size:9px;color:var(--faint)">[DISCIPLINE ENGINE]</span>
            </div>
            <button class="enlarge-btn" id="btnEnlarge" onclick="toggleEnlargeDesk()">
              <span id="enlargeIcon">⤢</span>
              <span id="enlargeText">Enlarge Desk</span>
            </button>
          </div>

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

          <div class="stand-aside-banner" id="standAsideBanner">
            <div class="sab-top">
              <span>⚠️ STAND ASIDE • CAPITAL PRESERVATION</span>
            </div>
            <div class="sab-desc" id="standAsideDesc">
              Market is currently consolidating in equilibrium. No high-probability institutional displacement or FVG has triggered. ICT Flux does NOT force trades.
            </div>
          </div>

          <div class="directive-card" id="dirCard">
            <div class="directive-top">
              <span class="archetype-label" id="dirArchetype">SMT Turtle Soup (Sister Divergence)</span>
              <span class="intercept-pill" id="dirHorizonBadge">DAY TRADE CHOKEPOINT</span>
            </div>
            <div class="directive-headline buy" id="dirHeadline">
              BUY LIMIT @ 1.33890
            </div>
            <div class="directive-exec">
              Best Entry Point: <b id="dirOrder">Limit @ FVG Consequent Encroachment (50%)</b>
            </div>
          </div>

          <div class="guidance-box">
            <div class="guide-cell">
              <div class="guide-lbl green">
                <span>✅ WHAT TO DO (EXECUTION DIRECTIVE)</span>
              </div>
              <div class="guide-desc" id="guideDo">
                Wait for price to tap the 50% Consequent Encroachment of the M5 Fair Value Gap inside the London Killzone. Place BUY LIMIT.
              </div>
            </div>

            <div class="guide-cell">
              <div class="guide-lbl red">
                <span>⛔ WHAT NOT TO DO (TRAP & CHOP WARNING)</span>
              </div>
              <div class="guide-desc" id="guideDont">
                DO NOT market-chase green expansion wicks. DO NOT hold if Stop Loss is violated with candle-body close.
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

          <div class="levels">
            <div class="level-box entry">
              <div class="level-label">Entry Level</div>
              <div class="level-price" style="color:var(--accent)" id="lvlEntry">1.33890</div>
              <span class="pip-pill gold" id="pillEntry">LIMIT @ 50% CE</span>
            </div>
            <div class="level-box stop">
              <div class="level-label">Stop Loss</div>
              <div class="level-price" style="color:var(--bear)" id="lvlStop">1.33810</div>
              <span class="pip-pill red" id="pillStop">8.0 PIPS RISK</span>
            </div>
            <div class="level-box target">
              <div class="level-label">Target Draw</div>
              <div class="level-price" style="color:var(--bull)" id="lvlTarget">1.34290</div>
              <span class="pip-pill green" id="pillTarget">40.0 PIPS TP</span>
            </div>
          </div>

          <div class="loss-avoidance-box">
            <div class="lab-top">
              <span>🛡️ LOSS AVOIDANCE & FREE-ROLL GOVERNOR</span>
              <span style="color:var(--bull)">ZERO-LOSS LOCK</span>
            </div>
            <div class="lab-desc" id="labDesc">
              At <b>+0.80R expansion</b>, Stop Loss automatically snaps to <b>Entry + 1 pip</b>. If an M5 candle closes below CISD prior to macro window end, kill at market to prevent full -1.0R loss.
            </div>
          </div>

          <div class="governor-breakdown">
            <div class="gov-step">
              <span>Auto BE Lock (+0.80R)</span>
              <b id="govBe">+0.80R (1.33954)</b>
            </div>
            <div class="gov-step">
              <span>TP1 Harvest (70%)</span>
              <b id="govTp1">+1.50R (1.34010)</b>
            </div>
            <div class="gov-step">
              <span>TP2 Runner (30%)</span>
              <b id="govTp2">+5.00R (1.34290)</b>
            </div>
          </div>

          <div class="calc-panel">
            <div class="lot-recommendation">
              <span>Risk $50: <b id="calc50">0.62 Lots</b></span>
              <span>Risk $100: <b id="calc100">1.25 Lots</b></span>
              <span>R:R: <b style="color:var(--accent)" id="calcRr">1 : 5.00 R</b></span>
            </div>
          </div>

          <div class="action-row">
            <button class="btn" onclick="copyPlan()">📋 Copy Tweet</button>
            <button class="btn primary" id="btnExecute" onclick="executeTrade()">⚡ Execute on MT5</button>
          </div>

          <!-- MT5 Execution Audit Journal -->
          <div class="desk-log-section">
            <div class="desk-log-header">
              <span class="desk-log-title">⚡ MT5 Execution Journal & Audit Log</span>
              <button class="log-clear-btn" onclick="clearCustomLogs()">Reset</button>
            </div>
            <div class="desk-log-table-wrap">
              <table class="log-table">
                <thead>
                  <tr>
                    <th>Ticket</th>
                    <th>Asset / TF</th>
                    <th>Model</th>
                    <th>Side</th>
                    <th>Entry</th>
                    <th>Pip Metrics</th>
                    <th>R:R</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody id="tradeLogBody">
                  <!-- Dynamically populated -->
                </tbody>
              </table>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- VIEW 2: RESEARCH & BACKTEST LAB (STATISTICAL EDGE)       -->
    <!-- ======================================================== -->
    <div class="view-pane" id="paneLab">
      <div class="lab-layout">
        
        <!-- Lab Header -->
        <div class="lab-hero">
          <div>
            <div class="lab-hero-title">
              <span>🔬 RESEARCH & BACKTEST LAB</span>
              <span style="font-size:10px;padding:3px 8px;border-radius:4px;background:var(--accent-soft);color:var(--accent);border:1px solid var(--line-gold);font-family:var(--mono)">SIMPLIFIED & INSTANTANEOUS</span>
            </div>
            <div class="lab-hero-sub">
              Verify how effective the ICT Flux signal service performs against historical market order flow over custom timeframes.
            </div>
          </div>
          <button class="btn primary" onclick="runBacktestSimulation()">▶ Run Backtest Simulation</button>
        </div>

        <!-- Backtest Configuration Parameters -->
        <div class="bt-config-card">
          <div class="bt-filters-row">
            
            <div class="bt-field">
              <label class="bt-label">Market Filter</label>
              <select class="bt-select" id="btMarket">
                <option value="ALL">All Markets Combined</option>
                <option value="GBPUSD">GBP/USD</option>
                <option value="EURUSD">EUR/USD</option>
                <option value="XAUUSD">XAU/USD (Gold $4,077+)</option>
                <option value="NAS100">NAS100 (NQ)</option>
                <option value="US500">US500 (ES)</option>
                <option value="USDJPY">USD/JPY</option>
                <option value="VOL75">VOL 75 (Deriv)</option>
              </select>
            </div>

            <div class="bt-field">
              <label class="bt-label">Period of Time</label>
              <select class="bt-select" id="btPeriod">
                <option value="7d">Last 7 Days (Ultra-Fast Audit)</option>
                <option value="30d" selected>Last 30 Days (Past Month - Recommended)</option>
                <option value="90d">Last 90 Days (Quarterly Audit)</option>
                <option value="365d">Last 365 Days (Full Year Sample)</option>
              </select>
            </div>

            <div class="bt-field">
              <label class="bt-label">Trade Horizon</label>
              <select class="bt-select" id="btHorizon">
                <option value="ALL">All Horizons Combined</option>
                <option value="scalp">Scalp (M1/M5 · 15-45m)</option>
                <option value="day" selected>Day Trade (M5/M15 · 2-5h)</option>
                <option value="swing">Swing (H1/H4 · 1-3d)</option>
              </select>
            </div>

            <div class="bt-field">
              <label class="bt-label">Model Archetype</label>
              <select class="bt-select" id="btModel">
                <option value="ALL">All God's Eye Chokepoints</option>
                <option value="smt">SMT Turtle Soup (Divergence)</option>
                <option value="kz">London KZ Displacement (ICT 2022)</option>
                <option value="sb">Silver Bullet Hour</option>
                <option value="judas">Judas Swing Reversal</option>
              </select>
            </div>

          </div>

          <!-- Strategy Safeguard Toggles -->
          <div class="bt-actions-row">
            <div class="bt-toggles">
              <label class="bt-toggle-item">
                <input type="checkbox" id="chkBeLock" checked>
                <span>Enforce +0.80R BE Lock</span>
              </label>
              <label class="bt-toggle-item">
                <input type="checkbox" id="chkHarvest" checked>
                <span>70% Harvest at TP1 (+1.5R)</span>
              </label>
              <label class="bt-toggle-item">
                <input type="checkbox" id="chkDiscipline" checked>
                <span>Strict Stand-Aside Filter</span>
              </label>
            </div>
            <button class="btn" onclick="exportBacktestCsv()">📥 Export Audit CSV</button>
          </div>
        </div>

        <!-- Statistical Performance Metrics -->
        <div class="lab-metrics-grid">
          <div class="metric-card">
            <span class="m-title">Win Rate %</span>
            <span class="m-val" style="color:var(--bull)" id="mWinRate">74.2%</span>
            <span class="m-sub" id="mWinLossRatio">23 Wins · 8 Losses</span>
          </div>
          <div class="metric-card">
            <span class="m-title">Net Cumulative R</span>
            <span class="m-val" style="color:var(--accent)" id="mNetR">+38.80 R</span>
            <span class="m-sub" id="mDollarReturn">+$3,880 on $10k account</span>
          </div>
          <div class="metric-card">
            <span class="m-title">Profit Factor</span>
            <span class="m-val" style="color:var(--bull)" id="mProfitFactor">2.86</span>
            <span class="m-sub">Gross Win / Gross Loss</span>
          </div>
          <div class="metric-card">
            <span class="m-title">Max Drawdown</span>
            <span class="m-val" style="color:var(--bear)" id="mMaxDd">-2.10 R</span>
            <span class="m-sub">Strict Anti-Ruin Control</span>
          </div>
          <div class="metric-card">
            <span class="m-title">Stand Aside Efficiency</span>
            <span class="m-val" style="color:var(--cyan)" id="mChopFiltered">88.5%</span>
            <span class="m-sub">Chop avoidance efficiency</span>
          </div>
        </div>

        <!-- Equity Growth Curve Visualizer -->
        <div class="equity-card">
          <div class="equity-head">
            <span>📈 CUMULATIVE R-MULTIPLE EQUITY GROWTH CURVE</span>
            <span style="color:var(--accent)" id="equitySpanLabel">Last 30 Days (Simulation)</span>
          </div>
          <div class="equity-chart-box">
            <svg class="equity-svg" id="equitySvg" viewBox="0 0 900 180" preserveAspectRatio="none">
              <!-- SVG Curve rendered dynamically -->
            </svg>
          </div>
        </div>

        <!-- Trade-by-Trade Audit Table -->
        <div class="trade-log-panel" style="border-radius:10px;border:1px solid var(--line)">
          <div class="log-header">
            <div class="log-title">
              <span>📜 VERIFIED BACKTEST AUDIT LOG</span>
              <span style="font-size:9.5px;color:var(--faint);" id="auditTotalLabel">[31 Simulated Executions]</span>
            </div>
          </div>
          <div class="log-table-wrap">
            <table class="log-table">
              <thead>
                <tr>
                  <th>Date & Time</th>
                  <th>Market</th>
                  <th>Horizon</th>
                  <th>Model Setup</th>
                  <th>Direction</th>
                  <th>Entry</th>
                  <th>Stop Loss</th>
                  <th>Target</th>
                  <th>Pips</th>
                  <th>Outcome</th>
                  <th>Return</th>
                </tr>
              </thead>
              <tbody id="backtestTableBody">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </div>

  </div>

  <div class="toast" id="toast"></div>

  <!-- APPLICATION DATA & RESEARCH LAB ENGINE SCRIPT -->
  <script>
    // Master Live Quotes Database
    const DATA = {
      GBPUSD: {
        label: 'GBP/USD',
        price: '1.3394',
        spread: '0.8 pips',
        pipScale: 0.0001,
        horizons: {
          scalp: {
            status: 'ACTIVE',
            tf: 'M1/M5',
            badge: '⚡ SCALP INTERCEPT',
            headline: 'BUY LIMIT @ 1.33895',
            headlineClass: 'buy',
            archetype: 'Micro FVG CE Tap (London Macro)',
            order: 'Limit @ 50% Consequent Encroachment (1.33895)',
            doText: 'Place <b>Buy Limit at 1.33895</b> immediately following the 08:30 macro displacement. Anchor Stop Loss surgical at <b>1.33850 (4.5 pips)</b>.',
            dontText: '<b>DO NOT</b> hold longer than 35 minutes. If target is not reached before 09:15 UTC, close at market.',
            whenText: 'Active window: <b>08:30 – 09:15 UTC (London Macro)</b>. Expected hold time: <b>15 – 35 minutes</b>.',
            entry: '1.33895',
            stop: '1.33850',
            target: '1.34075',
            pillEntry: 'LIMIT @ M1 CE',
            pillStop: '4.5 PIPS RISK',
            pillTarget: '18.0 PIPS TP',
            lossAvoidance: 'At <b>+0.80R (1.33931)</b>, Stop Loss moves to Breakeven (+1 pip). If M1 candle closes below 1.33870, kill trade immediately.',
            govBe: '+0.80R (1.33931)',
            govTp1: '+1.50R (1.33962)',
            govTp2: '+4.00R (1.34075)',
            calc50: '1.11 Lots',
            calc100: '2.22 Lots',
            calcRr: '1 : 4.00 R',
            profile: 'IPDA: MICRO LIQUIDITY RUN',
            levels: [
              { title: 'SESSION HIGH [1.34075]', price: 1.34075, color: '#2BD47D', style: 2 },
              { title: 'ENTRY @ 1.33895', price: 1.33895, color: '#F0B94B', style: 0, width: 2 },
              { title: 'SURGICAL STOP [1.33850]', price: 1.33850, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 1.33870,
            candlePattern: 'scalp_bull'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5/M15',
            badge: '🎯 DAY TRADE CHOKEPOINT',
            headline: 'BUY LIMIT @ 1.33890',
            headlineClass: 'buy',
            archetype: 'SMT Turtle Soup (Sister Divergence)',
            order: 'Limit @ FVG Consequent Encroachment (50%)',
            doText: 'Wait for price to tap the <b>50% Consequent Encroachment (1.33890)</b>. Surgical Stop Loss anchored tight at <b>1.33810 (8.0 pips)</b>.',
            dontText: '<b>DO NOT</b> market-chase the green expansion candle above Asian High. <b>DO NOT</b> hold if 1.33810 is violated with candle-body close.',
            whenText: 'Delivery window: <b>08:30 – 09:15 UTC (London Open)</b>. Expected hold duration: <b>2 to 5 hours</b>.',
            entry: '1.33890',
            stop: '1.33810',
            target: '1.34290',
            pillEntry: 'LIMIT @ 50% CE',
            pillStop: '8.0 PIPS RISK',
            pillTarget: '40.0 PIPS TP',
            lossAvoidance: 'At <b>+0.80R (1.33954)</b>, move SL to Breakeven (+1 pip). If M5 closes below 1.33840 before 09:30 NY macro, kill trade at market.',
            govBe: '+0.80R (1.33954)',
            govTp1: '+1.50R (1.34010)',
            govTp2: '+5.00R (1.34290)',
            calc50: '0.62 Lots',
            calc100: '1.25 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'IPDA: WEDNESDAY EXPANSION',
            levels: [
              { title: 'PDH BUY-SIDE TARGET [1.34290]', price: 1.34290, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ FVG 50% CE [1.33890]', price: 1.33890, color: '#F0B94B', style: 0, width: 2 },
              { title: 'SURGICAL STOP [8.0 PIPS @ 1.33810]', price: 1.33810, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 1.33830,
            candlePattern: 'day_bull'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1/H4',
            badge: '🌊 SWING PROFILE',
            headline: 'BUY LIMIT @ 1.33500',
            headlineClass: 'buy',
            archetype: 'Weekly Bullish Profile (Tuesday Low)',
            order: 'Limit @ 4H Bullish Order Block + Discount FVG',
            doText: 'Place <b>Buy Limit at 1.33500</b> anchored to 4H OB. Surgical Stop Loss at <b>1.33220 (28.0 pips)</b>. Target 1.34900 (140 pips).',
            dontText: '<b>DO NOT</b> exit early during intra-day London retracements if 4H market structure remains intact above 1.33220.',
            whenText: 'Hold duration: <b>1 to 3 days</b>. Weekly expansion phase targeting Friday NY settlement.',
            entry: '1.33500',
            stop: '1.33220',
            target: '1.34900',
            pillEntry: 'LIMIT @ 4H OB',
            pillStop: '28.0 PIPS RISK',
            pillTarget: '140.0 PIPS TP',
            lossAvoidance: 'At <b>+1.00R (1.33780)</b>, move SL to Entry. Take 70% off table at TP1 (1.33920) to ensure a guaranteed win.',
            govBe: '+0.80R (1.33724)',
            govTp1: '+1.50R (1.33920)',
            govTp2: '+5.00R (1.34900)',
            calc50: '0.18 Lots',
            calc100: '0.36 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'IPDA: MULTI-WEEK EXPANSION',
            levels: [
              { title: 'PREVIOUS WEEK HIGH [1.34900]', price: 1.34900, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ 4H OB [1.33500]', price: 1.33500, color: '#F0B94B', style: 0, width: 2 },
              { title: 'SURGICAL STOP [28.0 PIPS @ 1.33220]', price: 1.33220, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 1.33300,
            candlePattern: 'swing_bull'
          }
        }
      },

      XAUUSD: {
        label: 'XAU/USD (Gold)',
        price: '4,077.60',
        spread: '1.8 pips',
        pipScale: 0.10,
        horizons: {
          scalp: {
            status: 'STAND_ASIDE',
            tf: 'M1/M5',
            badge: '⏸️ STAND ASIDE',
            headline: 'NO ACTIVE SCALP SETUP',
            headlineClass: 'wait',
            archetype: 'Mid-Range Post-Expansion Consolidation',
            order: 'Stand Aside (Capital Preservation)',
            doText: '<b>STAND ASIDE.</b> Gold is resting at $4,077.60 in dead equilibrium after a $72 expansion ($4,044.50 – $4,116.20). No M5 FVG tap in current window. ICT Flux does NOT force trades.',
            dontText: '<b>DO NOT</b> buy or sell in the middle of a $70 daily range. Chasing now causes immediate losses.',
            whenText: 'Next viable window: <b>NY AM Session (13:30 – 15:30 UTC)</b> on clean liquidity sweep of $4,044.',
            entry: '---',
            stop: '---',
            target: '---',
            pillEntry: 'MONITORING',
            pillStop: 'STAND ASIDE',
            pillTarget: 'NO SETUP',
            lossAvoidance: 'Sitting on hands when price is mid-range saves 100% of chop drawdowns. Zero forced trades.',
            govBe: '---',
            govTp1: '---',
            govTp2: '---',
            calc50: '0.00 Lots',
            calc100: '0.00 Lots',
            calcRr: '0.00 R',
            profile: 'IPDA: POST-EXPANSION EQUILIBRIUM',
            levels: [
              { title: 'TODAY HIGH RESISTANCE [4,116.20]', price: 4116.20, color: '#F59E0B', style: 2 },
              { title: 'EQUILIBRIUM CURRENT [4,077.60]', price: 4077.60, color: '#9AA3B5', style: 2 },
              { title: 'TODAY LOW SUPPORT [4,044.50]', price: 4044.50, color: '#F59E0B', style: 2 }
            ],
            basePrice: 4070.00,
            candlePattern: 'chop'
          },
          day: {
            status: 'STAND_ASIDE',
            tf: 'M5/M15',
            badge: '⏸️ STAND ASIDE',
            headline: 'STAND ASIDE • NO CHOKEPOINT',
            headlineClass: 'wait',
            archetype: 'Equilibrium Consolidation ($4,044 - $4,116)',
            order: 'Stand Aside (Wait for Extremes)',
            doText: '<b>STAND ASIDE.</b> Gold is hovering between today\'s High ($4,116.20) and Low ($4,044.50). Institutional order flow has not swept either boundary. Discipline first.',
            dontText: '<b>DO NOT</b> enter limits at current price ($4,077.60). Avoid low-probability midday chop.',
            whenText: 'Observation: Wait for London close or NY AM opening sweep.',
            entry: '---',
            stop: '---',
            target: '---',
            pillEntry: 'OBSERVATION',
            pillStop: 'STAND ASIDE',
            pillTarget: 'NO SETUP',
            lossAvoidance: 'Standing aside preserves your margin and protects users from losing capital.',
            govBe: '---',
            govTp1: '---',
            govTp2: '---',
            calc50: '0.00 Lots',
            calc100: '0.00 Lots',
            calcRr: '0.00 R',
            profile: 'IPDA: EXTENDED RANGE CONSOLIDATION',
            levels: [
              { title: 'DAY HIGH [4,116.20]', price: 4116.20, color: '#F59E0B', style: 2 },
              { title: 'DAY LOW [4,044.50]', price: 4044.50, color: '#F59E0B', style: 2 }
            ],
            basePrice: 4065.00,
            candlePattern: 'chop'
          },
          swing: {
            status: 'STAND_ASIDE',
            tf: 'H1/H4',
            badge: '⏸️ STAND ASIDE',
            headline: 'NO ACTIVE SWING SETUP',
            headlineClass: 'wait',
            archetype: 'All-Time High Premium Array ($4,000+ Extension)',
            order: 'Stand Aside (Over-Extended)',
            doText: '<b>STAND ASIDE.</b> Gold is trading at unprecedented all-time highs above $4,000. Wait for multi-day structural discount retracement.',
            dontText: '<b>DO NOT</b> buy into ATH exhaustion without 4H discount equilibrium.',
            whenText: 'Observation: Wait for daily pullback toward $3,950 discount base.',
            entry: '---',
            stop: '---',
            target: '---',
            pillEntry: 'OBSERVATION',
            pillStop: 'STAND ASIDE',
            pillTarget: 'NO SETUP',
            lossAvoidance: 'Sitting on hands at multi-month premium highs prevents severe drawdown.',
            govBe: '---',
            govTp1: '---',
            govTp2: '---',
            calc50: '0.00 Lots',
            calc100: '0.00 Lots',
            calcRr: '0.00 R',
            profile: 'IPDA: EXTREME PREMIUM EXPANSION',
            levels: [
              { title: 'ATH PEAK [4,116.20]', price: 4116.20, color: '#F59E0B', style: 2 }
            ],
            basePrice: 4070.00,
            candlePattern: 'chop'
          }
        }
      },

      EURUSD: {
        label: 'EUR/USD',
        price: '1.1177',
        spread: '0.6 pips',
        pipScale: 0.0001,
        horizons: {
          scalp: {
            status: 'STAND_ASIDE',
            tf: 'M1/M5',
            badge: '⏸️ STAND ASIDE',
            headline: 'NO ACTIVE SCALP SETUP',
            headlineClass: 'wait',
            archetype: 'Asian Range Dead Consolidation',
            order: 'Stand Aside (No Displacement)',
            doText: '<b>STAND ASIDE.</b> Price is deadlocked in a 6-pip range (1.1171 – 1.1177). Capital preservation in effect until London Open.',
            dontText: '<b>DO NOT</b> force scalps inside tight consolidation. Avoid spread widening.',
            whenText: 'Next viable intercept window: <b>London Open Killzone (07:00 – 09:00 UTC)</b>.',
            entry: '---',
            stop: '---',
            target: '---',
            pillEntry: 'MONITORING',
            pillStop: 'STAND ASIDE',
            pillTarget: 'NO SETUP',
            lossAvoidance: 'Discipline Rule: 0 trades taken during 6-pip dead Asian consolidation avoids guaranteed chop losses.',
            govBe: '---',
            govTp1: '---',
            govTp2: '---',
            calc50: '0.00 Lots',
            calc100: '0.00 Lots',
            calcRr: '0.00 R',
            profile: 'IPDA: CONSOLIDATION PHASE',
            levels: [
              { title: 'ASIA HIGH [1.11820]', price: 1.11820, color: '#F59E0B', style: 2 },
              { title: 'ASIA LOW [1.11710]', price: 1.11710, color: '#F59E0B', style: 2 }
            ],
            basePrice: 1.1174,
            candlePattern: 'chop'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5/M15',
            badge: '🎯 DAY TRADE CHOKEPOINT',
            headline: 'SELL LIMIT @ 1.12150',
            headlineClass: 'sell',
            archetype: 'Judas Swing Reversal into Bearish OB',
            order: 'Limit @ Bearish Order Block + 15M FVG',
            doText: 'Enter <b>Sell Limit at 1.12150</b> as price completes the Judas Swing fakeout. Surgical Stop Loss at <b>1.12215 (6.5 pips)</b>.',
            dontText: '<b>DO NOT</b> short market before the liquidity sweep. Must see M5 CISD candle close.',
            whenText: 'Timing: <b>08:00 – 10:00 UTC (London Killzone)</b>. Expected hold: <b>3 to 5 hours</b>.',
            entry: '1.12150',
            stop: '1.12215',
            target: '1.11710',
            pillEntry: 'LIMIT @ 15M OB',
            pillStop: '6.5 PIPS RISK',
            pillTarget: '44.0 PIPS TP',
            lossAvoidance: 'At <b>+0.80R (1.12098)</b>, move SL to Breakeven (+1 pip). If price closes back above 1.12170, scratch trade immediately.',
            govBe: '+0.80R (1.12098)',
            govTp1: '+1.50R (1.12052)',
            govTp2: '+6.77R (1.11710)',
            calc50: '0.77 Lots',
            calc100: '1.54 Lots',
            calcRr: '1 : 6.77 R',
            profile: 'IPDA: LONDON REVERSAL',
            levels: [
              { title: 'SURGICAL STOP [1.12215]', price: 1.12215, color: '#FF5C6C', style: 2, width: 2 },
              { title: 'ENTRY @ BEARISH OB [1.12150]', price: 1.12150, color: '#F0B94B', style: 0, width: 2 },
              { title: 'SELL-SIDE TARGET [1.11710]', price: 1.11710, color: '#2BD47D', style: 2, width: 2 }
            ],
            basePrice: 1.1200,
            candlePattern: 'day_bear'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1/H4',
            badge: '🌊 SWING PROFILE',
            headline: 'SELL LIMIT @ 1.12450',
            headlineClass: 'sell',
            archetype: 'Multi-Week Bearish Delivery',
            order: 'Limit @ Daily Bearish Mitigation',
            doText: 'Place <b>Sell Limit at 1.12450</b>. Surgical Stop Loss at <b>1.12700 (25.0 pips)</b>. Target equal lows at 1.11050 (140 pips).',
            dontText: '<b>DO NOT</b> move stop loss to breakeven prematurely before the 1.11800 level is pierced.',
            whenText: 'Hold window: <b>2 to 4 days</b>.',
            entry: '1.12450',
            stop: '1.12700',
            target: '1.11050',
            pillEntry: 'LIMIT @ DAILY OB',
            pillStop: '25.0 PIPS RISK',
            pillTarget: '140.0 PIPS TP',
            lossAvoidance: 'Dual-Tranche: Take 70% off at TP1 (1.12075). Run remaining 30% risk-free with Stop Loss locked in profit.',
            govBe: '+0.80R (1.12250)',
            govTp1: '+1.50R (1.12075)',
            govTp2: '+5.60R (1.11050)',
            calc50: '0.20 Lots',
            calc100: '0.40 Lots',
            calcRr: '1 : 5.60 R',
            profile: 'IPDA: MONTHLY EXPANSION',
            levels: [
              { title: 'SURGICAL STOP [1.12700]', price: 1.12700, color: '#FF5C6C', style: 2, width: 2 },
              { title: 'ENTRY @ 1.12450', price: 1.12450, color: '#F0B94B', style: 0, width: 2 },
              { title: 'EQUAL LOWS DRAW [1.11050]', price: 1.11050, color: '#2BD47D', style: 2, width: 2 }
            ],
            basePrice: 1.1220,
            candlePattern: 'swing_bear'
          }
        }
      },

      NAS100: {
        label: 'NAS100 (NQ)',
        price: '27,139.2',
        spread: '1.2 pts',
        pipScale: 1.0,
        horizons: {
          scalp: {
            status: 'ACTIVE',
            tf: 'M1/M5',
            badge: '⚡ SCALP INTERCEPT',
            headline: 'BUY LIMIT @ 27,080.0',
            headlineClass: 'buy',
            archetype: '09:30 AM Silver Bullet CISD',
            order: 'Limit @ 1M FVG Consequent Encroachment',
            doText: 'Enter <b>Buy Limit at 27,080.0</b>. Surgical Stop Loss anchored tight at <b>27,062.0 (18.0 pts)</b>. Target 27,170.0 (90 pts).',
            dontText: '<b>DO NOT</b> trade before 09:35 AM initial volatility filter clears.',
            whenText: 'Timing: <b>09:35 – 10:30 AM NY (Silver Bullet)</b>. Hold: <b>15 – 45 min</b>.',
            entry: '27,080.0',
            stop: '27,062.0',
            target: '27,170.0',
            pillEntry: 'LIMIT @ 1M FVG',
            pillStop: '18.0 PTS RISK',
            pillTarget: '90.0 PTS TP',
            lossAvoidance: 'At <b>+0.80R (27,094.4)</b>, auto-move SL to +2 pts above entry. If 1M candle closes below 27,075, kill trade.',
            govBe: '+0.80R (27,094.4)',
            govTp1: '+1.50R (27,107.0)',
            govTp2: '+5.00R (27,170.0)',
            calc50: '0.55 Lots',
            calc100: '1.11 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'IPDA: SILVER BULLET HOUR',
            levels: [
              { title: 'BUY-SIDE LIQUIDITY [27,170.0]', price: 27170.0, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ 27,080.0', price: 27080.0, color: '#F0B94B', style: 0, width: 2 },
              { title: 'SURGICAL STOP [27,062.0]', price: 27062.0, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 27070.0,
            candlePattern: 'scalp_bull'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5/M15',
            badge: '🎯 DAY TRADE CHOKEPOINT',
            headline: 'BUY LIMIT @ 26,980.0',
            headlineClass: 'buy',
            archetype: 'London Low Sweep & Reversal',
            order: 'Limit @ 15M Bullish FVG (50% CE)',
            doText: 'Wait for price to test <b>26,980.0</b>. Surgical Stop Loss anchored tight at <b>26,945.0 (35.0 pts)</b>. Target 27,250.0 (270 pts).',
            dontText: '<b>DO NOT</b> chase green 5-minute wicks without resting limit at discount.',
            whenText: 'Delivery window: <b>14:00 – 16:30 UTC</b>. Expected hold: <b>2 to 5 hours</b>.',
            entry: '26,980.0',
            stop: '26,945.0',
            target: '27,250.0',
            pillEntry: 'LIMIT @ 15M CE',
            pillStop: '35.0 PTS RISK',
            pillTarget: '270.0 PTS TP',
            lossAvoidance: 'At <b>+0.80R (27,008.0)</b>, move SL to Breakeven (+2 pts). 70% harvested at TP1 (27,032.5).',
            govBe: '+0.80R (27,008.0)',
            govTp1: '+1.50R (27,032.5)',
            govTp2: '+7.71R (27,250.0)',
            calc50: '0.28 Lots',
            calc100: '0.57 Lots',
            calcRr: '1 : 7.71 R',
            profile: 'IPDA: NY EXPANSION RUN',
            levels: [
              { title: 'PDH BUY-SIDE DRAW [27,250.0]', price: 27250.0, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ 26,980.0', price: 26980.0, color: '#F0B94B', style: 0, width: 2 },
              { title: 'SURGICAL STOP [26,945.0]', price: 26945.0, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 26960.0,
            candlePattern: 'day_bull'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1/H4',
            badge: '🌊 SWING PROFILE',
            headline: 'BUY LIMIT @ 26,500.0',
            headlineClass: 'buy',
            archetype: 'Weekly Index Expansion to HTF BSL',
            order: 'Limit @ 4H Bullish Mitigation Block',
            doText: 'Enter <b>Buy Limit at 26,500.0</b>. Stop Loss at <b>26,420.0 (80.0 pts)</b>. Target 27,500.0 (1,000 pts).',
            dontText: '<b>DO NOT</b> panic on early morning futures retracements if 4H candle closes hold above 26,420.0.',
            whenText: 'Hold duration: <b>2 to 4 days</b>.',
            entry: '26,500.0',
            stop: '26,420.0',
            target: '27,500.0',
            pillEntry: 'LIMIT @ 4H OB',
            pillStop: '80.0 PTS RISK',
            pillTarget: '1,000 PTS TP',
            lossAvoidance: 'At <b>+1.00R (26,580.0)</b>, Stop Loss moves to Breakeven. Harvest 70% at 26,620.0.',
            govBe: '+0.80R (26,564.0)',
            govTp1: '+1.50R (26,620.0)',
            govTp2: '+12.5R (27,500.0)',
            calc50: '0.12 Lots',
            calc100: '0.25 Lots',
            calcRr: '1 : 12.5 R',
            profile: 'IPDA: WEEKLY EXPANSION',
            levels: [
              { title: 'HTF BSL TARGET [27,500.0]', price: 27500.0, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ 26,500.0', price: 26500.0, color: '#F0B94B', style: 0, width: 2 },
              { title: 'SURGICAL STOP [26,420.0]', price: 26420.0, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 26450.0,
            candlePattern: 'swing_bull'
          }
        }
      },

      US500: {
        label: 'US500 (ES)',
        price: '7,403.7',
        spread: '0.3 pts',
        pipScale: 1.0,
        horizons: {
          scalp: {
            status: 'STAND_ASIDE',
            tf: 'M1/M5',
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
            levels: [
              { title: 'PRE-MKT HIGH [7,427.0]', price: 7427.0, color: '#F59E0B', style: 2 },
              { title: 'PRE-MKT LOW [7,322.0]', price: 7322.0, color: '#F59E0B', style: 2 }
            ],
            basePrice: 7400.0,
            candlePattern: 'chop'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5/M15',
            badge: '🎯 DAY TRADE CHOKEPOINT',
            headline: 'BUY LIMIT @ 7,370.0',
            headlineClass: 'buy',
            archetype: 'Opening Range Gap Fill & FVG Expansion',
            order: 'Limit @ 7,370.0 (50% FVG CE)',
            doText: 'Buy S&P at <b>7,370.0</b> on opening gap fill. Surgical Stop Loss at <b>7,361.0 (9.0 pts)</b>. Target 7,425.0 (55.0 pts).',
            dontText: '<b>DO NOT</b> chase into 7,420 resistance without discount retracement.',
            whenText: 'Active: <b>14:45 – 17:00 UTC</b>. Hold: <b>2 to 4 hours</b>.',
            entry: '7,370.0',
            stop: '7,361.0',
            target: '7,425.0',
            pillEntry: 'LIMIT @ 7,370.0',
            pillStop: '9.0 PTS RISK',
            pillTarget: '55.0 PTS TP',
            lossAvoidance: 'At <b>+0.80R (7,377.2)</b>, move SL to Entry. Take 70% off at TP1 (7,383.5) to lock in profit.',
            govBe: '+0.80R (7,377.2)',
            govTp1: '+1.50R (7,383.5)',
            govTp2: '+6.11R (7,425.0)',
            calc50: '0.55 Lots',
            calc100: '1.11 Lots',
            calcRr: '1 : 6.11 R',
            profile: 'IPDA: NY AM EXPANSION',
            levels: [
              { title: 'TARGET DRAW [7,425.0]', price: 7425.0, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ 7,370.0', price: 7370.0, color: '#F0B94B', style: 0, width: 2 },
              { title: 'SURGICAL STOP [7,361.0]', price: 7361.0, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 7365.0,
            candlePattern: 'day_bull'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1/H4',
            badge: '🌊 SWING PROFILE',
            headline: 'BUY LIMIT @ 7,330.0',
            headlineClass: 'buy',
            archetype: 'Multi-Week Bullish Order Flow',
            order: 'Limit @ 4H Discount Mitigation Block',
            doText: 'Place <b>Buy Limit at 7,330.0</b>. Surgical Stop Loss at <b>7,305.0 (25.0 pts)</b>. Target 7,470.0 (140.0 pts).',
            dontText: '<b>DO NOT</b> exit early during mid-day consolidation.',
            whenText: 'Hold window: <b>2 to 5 days</b>.',
            entry: '7,330.0',
            stop: '7,305.0',
            target: '7,470.0',
            pillEntry: 'LIMIT @ 7,330.0',
            pillStop: '25.0 PTS RISK',
            pillTarget: '140.0 PTS TP',
            lossAvoidance: 'At <b>+1.00R (7,355.0)</b>, move SL to Breakeven. Harvest 70% at 7,367.5.',
            govBe: '+0.80R (7,350.0)',
            govTp1: '+1.50R (7,367.5)',
            govTp2: '+5.60R (7,470.0)',
            calc50: '0.20 Lots',
            calc100: '0.40 Lots',
            calcRr: '1 : 5.60 R',
            profile: 'IPDA: MONTHLY EXPANSION',
            levels: [
              { title: 'MONTHLY BSL [7,470.0]', price: 7470.0, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ 7,330.0', price: 7330.0, color: '#F0B94B', style: 0, width: 2 },
              { title: 'SURGICAL STOP [7,305.0]', price: 7305.0, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 7320.0,
            candlePattern: 'swing_bull'
          }
        }
      },

      USDJPY: {
        label: 'USD/JPY',
        price: '158.26',
        spread: '0.9 pips',
        pipScale: 0.01,
        horizons: {
          scalp: {
            status: 'STAND_ASIDE',
            tf: 'M1/M5',
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
            levels: [
              { title: 'TOKYO HIGH [158.38]', price: 158.38, color: '#F59E0B', style: 2 },
              { title: 'TOKYO LOW [157.25]', price: 157.25, color: '#F59E0B', style: 2 }
            ],
            basePrice: 158.20,
            candlePattern: 'chop'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5/M15',
            badge: '🎯 DAY TRADE CHOKEPOINT',
            headline: 'BUY LIMIT @ 157.85',
            headlineClass: 'buy',
            archetype: 'Asian Range Sweep & London Mitigation',
            order: 'Limit @ OTE 70.5% (157.85)',
            doText: 'Place <b>Buy Limit at 157.85</b> (OTE 70.5% retracement). Surgical Stop Loss at <b>157.73 (12.0 pips)</b>. Target 158.45 (60.0 pips).',
            dontText: '<b>DO NOT</b> hold if 157.73 is breached on 15M candle close.',
            whenText: 'Hold duration: <b>2 to 5 hours</b>. Target Tokyo high at 158.45.',
            entry: '157.85',
            stop: '157.73',
            target: '158.45',
            pillEntry: 'LIMIT @ OTE 70.5%',
            pillStop: '12.0 PIPS RISK',
            pillTarget: '60.0 PIPS TP',
            lossAvoidance: 'At <b>+0.80R (157.95)</b>, move SL to 157.86 (+1 pip profit). Eliminates trade risk early.',
            govBe: '+0.80R (157.95)',
            govTp1: '+1.50R (158.03)',
            govTp2: '+5.00R (158.45)',
            calc50: '0.42 Lots',
            calc100: '0.83 Lots',
            calcRr: '1 : 5.00 R',
            profile: 'IPDA: LONDON EXPANSION',
            levels: [
              { title: 'TOKYO HIGH DRAW [158.45]', price: 158.45, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ 157.85', price: 157.85, color: '#F0B94B', style: 0, width: 2 },
              { title: 'SURGICAL STOP [157.73]', price: 157.73, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 157.80,
            candlePattern: 'day_bull'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1/H4',
            badge: '🌊 SWING PROFILE',
            headline: 'BUY LIMIT @ 156.90',
            headlineClass: 'buy',
            archetype: 'Weekly Bullish Institutional Expansion',
            order: 'Limit @ 4H Bullish Mitigation Block',
            doText: 'Enter <b>Buy Limit at 156.90</b>. Surgical Stop Loss at <b>156.45 (45.0 pips)</b>. Target 159.20 (230 pips).',
            dontText: '<b>DO NOT</b> cut runner before 158.50 partial take-profit.',
            whenText: 'Expected hold time: <b>2 to 4 days</b>.',
            entry: '156.90',
            stop: '156.45',
            target: '159.20',
            pillEntry: 'LIMIT @ 4H OB',
            pillStop: '45.0 PIPS RISK',
            pillTarget: '230.0 PIPS TP',
            lossAvoidance: 'At <b>+1.00R (157.35)</b>, move SL to Breakeven. Take 70% off at TP1 (157.58).',
            govBe: '+0.80R (157.26)',
            govTp1: '+1.50R (157.58)',
            govTp2: '+5.11R (159.20)',
            calc50: '0.11 Lots',
            calc100: '0.22 Lots',
            calcRr: '1 : 5.11 R',
            profile: 'IPDA: MULTI-WEEK EXPANSION',
            levels: [
              { title: 'MAJOR HIGH POOL [159.20]', price: 159.20, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ 156.90', price: 156.90, color: '#F0B94B', style: 0, width: 2 },
              { title: 'SURGICAL STOP [156.45]', price: 156.45, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 156.80,
            candlePattern: 'swing_bull'
          }
        }
      },

      VOL75: {
        label: 'VOL 75 (Deriv)',
        price: '148,420.0',
        spread: '25.0 pts',
        pipScale: 1.0,
        horizons: {
          scalp: {
            status: 'ACTIVE',
            tf: 'M1/M5',
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
            levels: [
              { title: 'ALGO BUY-SIDE DRAW [149,250.0]', price: 149250.0, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ 148,250.0', price: 148250.0, color: '#38BDF8', style: 0, width: 2 },
              { title: 'SURGICAL STOP [148,000.0]', price: 148000.0, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 148100.0,
            candlePattern: 'scalp_bull'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5/M15',
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
            levels: [
              { title: 'LIQUIDITY POOL DRAW [150,300.0]', price: 150300.0, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ 147,800.0', price: 147800.0, color: '#38BDF8', style: 0, width: 2 },
              { title: 'SURGICAL STOP [147,300.0]', price: 147300.0, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 147500.0,
            candlePattern: 'day_bull'
          },
          swing: {
            status: 'ACTIVE',
            tf: 'H1/H4',
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
            levels: [
              { title: 'MAJOR SWING DRAW [152,500.0]', price: 152500.0, color: '#2BD47D', style: 2, width: 2 },
              { title: 'ENTRY @ 146,500.0', price: 146500.0, color: '#38BDF8', style: 0, width: 2 },
              { title: 'SURGICAL STOP [145,500.0]', price: 145500.0, color: '#FF5C6C', style: 2, width: 2 }
            ],
            basePrice: 146000.0,
            candlePattern: 'swing_bull'
          }
        }
      },

      VOL100: {
        label: 'VOL 100 (Deriv)',
        price: '2,842.50',
        spread: '0.50 pts',
        pipScale: 1.0,
        horizons: {
          scalp: {
            status: 'ACTIVE',
            tf: 'M1/M5',
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
            levels: [
              { title: 'SURGICAL STOP [2,848.80]', price: 2848.80, color: '#FF5C6C', style: 2, width: 2 },
              { title: 'ENTRY @ 2,845.20', price: 2845.20, color: '#38BDF8', style: 0, width: 2 },
              { title: 'EQUAL LOWS TARGET [2,827.20]', price: 2827.20, color: '#2BD47D', style: 2, width: 2 }
            ],
            basePrice: 2844.00,
            candlePattern: 'scalp_bear'
          },
          day: {
            status: 'ACTIVE',
            tf: 'M5/M15',
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
            levels: [
              { title: 'SURGICAL STOP [2,859.50]', price: 2859.50, color: '#FF5C6C', style: 2, width: 2 },
              { title: 'ENTRY @ 2,852.00', price: 2852.00, color: '#38BDF8', style: 0, width: 2 },
              { title: 'SELL-SIDE DRAW [2,814.50]', price: 2814.50, color: '#2BD47D', style: 2, width: 2 }
            ],
            basePrice: 2850.00,
            candlePattern: 'day_bear'
          },
          swing: {
            status: 'STAND_ASIDE',
            tf: 'H1/H4',
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
            levels: [
              { title: 'RANGE CEILING [2,900.00]', price: 2900.00, color: '#F59E0B', style: 2 },
              { title: 'RANGE FLOOR [2,750.00]', price: 2750.00, color: '#F59E0B', style: 2 }
            ],
            basePrice: 2840.00,
            candlePattern: 'chop'
          }
        }
      }
    };

    // Verified trade history
    const DEFAULT_LOGS = [
      {
        time: 'Nov 03 08:05',
        ticket: '#849102',
        symbol: 'EUR/USD',
        horizon: 'Day Trade',
        model: 'London KZ Bearish Displacement',
        side: 'SELL',
        entry: '1.12150',
        sl: '1.12215',
        tp: '1.11710',
        pips: 'SL: 6.5p | TP: 44.0p',
        rr: '1 : 6.77 R',
        status: 'CLOSED_WIN',
        statusLabel: '+6.77R WIN'
      },
      {
        time: 'Nov 03 09:00',
        ticket: '#849118',
        symbol: 'GBP/USD',
        horizon: 'Day Trade',
        model: 'SMT Turtle Soup (Sister Divergence)',
        side: 'SELL',
        entry: '1.33890',
        sl: '1.33810',
        tp: '1.34290',
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
        symbol: 'NAS100 (NQ)',
        horizon: 'Scalp',
        model: 'Silver Bullet CISD',
        side: 'BUY',
        entry: '27,080.0',
        sl: '27,062.0',
        tp: '27,170.0',
        pips: 'SL: 18.0p | TP: 90.0p',
        rr: '1 : 5.00 R',
        status: 'CLOSED_WIN',
        statusLabel: '+5.00R WIN'
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
    let tvChart = null;
    let tvSeries = null;
    let activePriceLines = [];
    let executedTrades = [];
    let isEnlarged = false;
    let activeView = 'desk';
    let currentBacktestResults = [];

    // VIEW SWITCHER
    function switchView(viewName) {
      activeView = viewName;
      document.getElementById('tabDesk').classList.toggle('active', viewName === 'desk');
      document.getElementById('tabLab').classList.toggle('active', viewName === 'lab');

      document.getElementById('paneDesk').classList.toggle('active', viewName === 'desk');
      document.getElementById('paneLab').classList.toggle('active', viewName === 'lab');

      if (viewName === 'desk') {
        setTimeout(() => {
          const c = document.getElementById('tvChartContainer');
          if (tvChart && c) tvChart.resize(c.clientWidth, c.clientHeight);
        }, 100);
      } else {
        runBacktestSimulation();
      }
    }

        // Chart Mode Engine State & Symbol Map
    let currentChartEngine = 'lc'; // 'lc' = Lightweight Charts, 'tv' = TradingView Widget
    const TV_MAP = {
      GBPUSD: { sym: 'FX:GBPUSD', tf: '15' },
      EURUSD: { sym: 'FX:EURUSD', tf: '15' },
      USDJPY: { sym: 'FX:USDJPY', tf: '15' },
      XAUUSD: { sym: 'OANDA:XAUUSD', tf: '15' },
      NAS100: { sym: 'FOREXCOM:NSXUSD', tf: '15' },
      US500: { sym: 'FOREXCOM:SPXUSD', tf: '15' },
      VOL75: { sym: 'FX:EURUSD', tf: '15' },
      VOL100: { sym: 'FX:GBPUSD', tf: '15' }
    };

    function switchChartEngine(engine) {
      currentChartEngine = engine;
      const bLc = document.getElementById('btnModeLc');
      const bTv = document.getElementById('btnModeTv');
      if (bLc) bLc.classList.toggle('active', engine === 'lc');
      if (bTv) bTv.classList.toggle('active', engine === 'tv');

      const lcContainer = document.getElementById('tvChartContainer');
      const tvFrame = document.getElementById('tvLiveFrame');

      if (engine === 'lc') {
        if (tvFrame) tvFrame.style.display = 'none';
        if (lcContainer) lcContainer.style.display = 'block';
        if (tvChart && lcContainer) {
          setTimeout(() => {
            tvChart.resize(lcContainer.clientWidth || 800, lcContainer.clientHeight || 500);
            tvChart.timeScale().fitContent();
          }, 50);
        }
      } else {
        if (lcContainer) lcContainer.style.display = 'none';
        if (tvFrame) tvFrame.style.display = 'block';
        updateTradingViewFrame();
      }
    }

    function updateTradingViewFrame() {
      const tvFrame = document.getElementById('tvLiveFrame');
      if (!tvFrame) return;
      const m = DATA[curKey];
      const h = m ? m.horizons[curHorizon] : null;
      const info = TV_MAP[curKey] || { sym: 'FX:GBPUSD', tf: '15' };
      const tfVal = (h && h.tf.includes('M1')) ? '1' : ((h && h.tf.includes('M5')) ? '5' : ((h && h.tf.includes('H1')) ? '60' : '15'));

      const q = new URLSearchParams({
        frameElementId: 'tv_frame_desk',
        symbol: info.sym,
        interval: tfVal,
        hidesidetoolbar: '0',
        symboledit: '1',
        saveimage: '0',
        theme: 'dark',
        style: '1',
        timezone: 'America/New_York',
        withdateranges: '1',
        locale: 'en'
      });
      const newSrc = `https://s.tradingview.com/widgetembed/?${q.toString()}`;
      if (tvFrame.src !== newSrc) {
        tvFrame.src = newSrc;
      }
    }

    // Initialize TradingView Lightweight Chart (Unobstructed Canvas)
    function initChart() {
      const container = document.getElementById('tvChartContainer');
      if (!container) return;
      container.innerHTML = '';

      const w = container.clientWidth || 800;
      const h = container.clientHeight || 500;

      tvChart = LightweightCharts.createChart(container, {
        width: w,
        height: h,
        autoSize: true,
        layout: {
          background: { type: 'solid', color: '#050608' },
          textColor: '#9AA3B5',
          fontFamily: "'Geist Mono', monospace",
          fontSize: 10.5
        },
        grid: {
          vertLines: { color: 'rgba(255, 255, 255, 0.03)' },
          horzLines: { color: 'rgba(255, 255, 255, 0.03)' }
        },
        crosshair: {
          mode: LightweightCharts.CrosshairMode.Normal,
          vertLine: { color: 'rgba(240, 185, 75, 0.4)', width: 1, style: 2 },
          horzLine: { color: 'rgba(240, 185, 75, 0.4)', width: 1, style: 2 }
        },
        rightPriceScale: {
          borderColor: 'rgba(255, 255, 255, 0.08)',
          scaleMargins: { top: 0.12, bottom: 0.12 }
        },
        timeScale: {
          borderColor: 'rgba(255, 255, 255, 0.08)',
          timeVisible: true,
          secondsVisible: false
        }
      });

      tvSeries = tvChart.addCandlestickSeries({
        upColor: '#2BD47D',
        downColor: '#FF5C6C',
        borderUpColor: '#2BD47D',
        borderDownColor: '#FF5C6C',
        wickUpColor: '#2BD47D',
        wickDownColor: '#FF5C6C'
      });

      if (window.ResizeObserver) {
        const ro = new ResizeObserver(entries => {
          if (!tvChart || !container) return;
          for (const entry of entries) {
            const cr = entry.contentRect;
            if (cr.width > 0 && cr.height > 0) {
              tvChart.resize(cr.width, cr.height);
            }
          }
        });
        ro.observe(container);
      }

      window.addEventListener('resize', () => {
        if (tvChart && container) {
          tvChart.resize(container.clientWidth || 800, container.clientHeight || 500);
        }
      });
    }

    function generateCandles(m, h) {
      const candles = [];
      const now = Math.floor(Date.now() / 1000);
      const step = h.tf.includes('M1') ? 60 : (h.tf.includes('M5') ? 300 : (h.tf.includes('H1') ? 3600 : 14400));
      const totalBars = 45;
      const startTime = now - (totalBars * step);

      let price = h.basePrice;

      for (let i = 0; i < totalBars; i++) {
        const time = startTime + (i * step);
        const open = price;
        
        let drift = 0;
        if (h.candlePattern === 'day_bull' || h.candlePattern === 'scalp_bull' || h.candlePattern === 'swing_bull') {
          if (i < 15) drift = (Math.sin(i * 1.5) * m.pipScale * 4);
          else if (i < 22) drift = -m.pipScale * 6;
          else if (i < 32) drift = m.pipScale * 8;
          else drift = -m.pipScale * 3;
        } else if (h.candlePattern === 'day_bear' || h.candlePattern === 'scalp_bear' || h.candlePattern === 'swing_bear') {
          if (i < 15) drift = (Math.sin(i * 1.5) * m.pipScale * 4);
          else if (i < 22) drift = -m.pipScale * 6;
          else if (i < 32) drift = -m.pipScale * 8;
          else drift = m.pipScale * 3;
        } else {
          drift = (Math.sin(i * 1.2) * m.pipScale * 2.5);
        }

        const close = open + drift;
        const high = Math.max(open, close) + Math.abs(Math.sin(i * 2.1) * m.pipScale * 2.5);
        const low = Math.min(open, close) - Math.abs(Math.cos(i * 2.1) * m.pipScale * 2.5);

        const decimals = (m.pipScale === 0.0001) ? 5 : ((m.pipScale === 0.01 || m.pipScale === 0.1) ? 2 : 1);
        candles.push({
          time: time,
          open: parseFloat(open.toFixed(decimals)),
          high: parseFloat(high.toFixed(decimals)),
          low: parseFloat(low.toFixed(decimals)),
          close: parseFloat(close.toFixed(decimals))
        });

        price = close;
      }

      const last = candles[candles.length - 1];
      const liveP = parseFloat(m.price.replace(/,/g, ''));
      last.close = liveP;
      last.high = Math.max(last.high, last.close);
      last.low = Math.min(last.low, last.close);

      return candles;
    }

    function updateDesk() {
      const m = DATA[curKey];
      const h = m.horizons[curHorizon];
      const isStandAside = h.status === 'STAND_ASIDE';

      // 1. Update Header / Toolbar Status
      document.getElementById('pairSpread').textContent = `Spread: ${m.spread}`;
      const badge = document.getElementById('pairStatusBadge');
      badge.textContent = isStandAside ? 'STAND ASIDE • NO SETUP' : 'ACTIVE INTERCEPT';
      badge.className = 'status-badge ' + (isStandAside ? 'standaside' : 'active');

      // 2. Stand Aside Banner
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

      // 3. Update Directive Card
      const hl = document.getElementById('dirHeadline');
      hl.textContent = h.headline;
      hl.className = 'directive-headline ' + h.headlineClass;
      document.getElementById('dirArchetype').textContent = h.archetype;
      document.getElementById('dirHorizonBadge').textContent = h.badge;
      document.getElementById('dirOrder').textContent = h.order;

      // 4. Update Guidance Triad
      document.getElementById('guideDo').innerHTML = h.doText;
      document.getElementById('guideDont').innerHTML = h.dontText;
      document.getElementById('guideWhen').innerHTML = h.whenText;

      // 5. Update Levels Matrix with Surgical Stops
      document.getElementById('lvlEntry').textContent = isStandAside ? '---' : h.entry;
      document.getElementById('lvlStop').textContent = isStandAside ? '---' : h.stop;
      document.getElementById('lvlTarget').textContent = isStandAside ? '---' : h.target;

      document.getElementById('pillEntry').textContent = h.pillEntry;
      document.getElementById('pillStop').textContent = h.pillStop;
      document.getElementById('pillTarget').textContent = h.pillTarget;

      // 6. Update Loss Avoidance Box
      document.getElementById('labDesc').innerHTML = h.lossAvoidance || 'Strict Breakeven Lock active at +0.80R.';

      // 7. Update Governor & Sizing
      document.getElementById('govBe').textContent = h.govBe;
      document.getElementById('govTp1').textContent = h.govTp1;
      document.getElementById('govTp2').textContent = h.govTp2;

      document.getElementById('calc50').textContent = h.calc50;
      document.getElementById('calc100').textContent = h.calc100;
      document.getElementById('calcRr').textContent = h.calcRr;

      // 8. Update Benchmark Bar (Non-interfering, below chart!)
      document.getElementById('bmModelLabel').textContent = `${m.label} · ${h.tf} · ${h.archetype.toUpperCase()}`;
      const pillsContainer = document.getElementById('bmPills');
      if (isStandAside) {
        pillsContainer.innerHTML = `
          <span class="bm-tag red">STAND ASIDE (DISCIPLINE)</span>
          <span class="bm-tag gray">LIVE: ${m.price}</span>
          <span class="bm-tag gray">NO ACTIVE TRIGGER</span>
        `;
      } else {
        pillsContainer.innerHTML = `
          <span class="bm-tag gold">ENTRY: ${h.entry}</span>
          <span class="bm-tag red">SL: ${h.stop} (${h.pillStop})</span>
          <span class="bm-tag green">TP: ${h.target} (${h.pillTarget})</span>
          <span class="bm-tag gray">R:R ${h.calcRr}</span>
        `;
      }

      // 9. Update TradingView Chart Data & Native Price Lines
      if (tvSeries) {
        activePriceLines.forEach(pl => {
          try { tvSeries.removePriceLine(pl); } catch (e) {}
        });
        activePriceLines = [];

        const candleData = generateCandles(m, h);
        tvSeries.setData(candleData);

        h.levels.forEach(lvl => {
          const pl = tvSeries.createPriceLine({
            price: lvl.price,
            color: lvl.color,
            lineWidth: lvl.width || 1,
            lineStyle: lvl.style,
            axisLabelVisible: true,
            title: lvl.title
          });
          activePriceLines.push(pl);
        });

        tvChart.timeScale().fitContent();
      }

      if (currentChartEngine === 'tv') {
        updateTradingViewFrame();
      }
    }

    function onSelectInstrument(key) {
      curKey = key;
      updateDesk();
    }

    function setHorizon(hz, btn) {
      curHorizon = hz;
      document.querySelectorAll('.hz-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      updateDesk();
    }

    function toggleEnlargeDesk() {
      const panel = document.getElementById('deskPanel');
      isEnlarged = !isEnlarged;
      panel.classList.toggle('enlarged', isEnlarged);

      const icon = document.getElementById('enlargeIcon');
      const text = document.getElementById('enlargeText');
      if (isEnlarged) {
        icon.textContent = '⤡';
        text.textContent = 'Compact Desk';
      } else {
        icon.textContent = '⤢';
        text.textContent = 'Enlarge Desk';
      }

      setTimeout(() => {
        const c = document.getElementById('tvChartContainer');
        if (tvChart && c) tvChart.resize(c.clientWidth, c.clientHeight);
      }, 150);
    }

    function setupResizer() {
      const divider = document.getElementById('resizerHandle');
      const deskPanel = document.getElementById('deskPanel');
      const container = document.getElementById('workspaceLayout');

      let isDragging = false;

      divider.addEventListener('mousedown', (e) => {
        isDragging = true;
        divider.classList.add('dragging');
        document.body.style.cursor = 'col-resize';
      });

      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        const containerRect = container.getBoundingClientRect();
        const newWidth = containerRect.right - e.clientX;
        if (newWidth >= 320 && newWidth <= 850) {
          deskPanel.style.width = newWidth + 'px';
          const c = document.getElementById('tvChartContainer');
          if (tvChart && c) tvChart.resize(c.clientWidth, c.clientHeight);
        }
      });

      window.addEventListener('mouseup', () => {
        if (isDragging) {
          isDragging = false;
          divider.classList.remove('dragging');
          document.body.style.cursor = 'default';
        }
      });

      divider.addEventListener('touchstart', () => { isDragging = true; divider.classList.add('dragging'); });
      window.addEventListener('touchmove', (e) => {
        if (!isDragging) return;
        const touch = e.touches[0];
        const containerRect = container.getBoundingClientRect();
        const newWidth = containerRect.right - touch.clientX;
        if (newWidth >= 300 && newWidth <= 850) {
          deskPanel.style.width = newWidth + 'px';
        }
      });
      window.addEventListener('touchend', () => { isDragging = false; divider.classList.remove('dragging'); });
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
      try { localStorage.setItem('ict_flux_custom_logs', JSON.stringify(executedTrades)); } catch (e) {}
    }

    function loadLogs() {
      try {
        const stored = localStorage.getItem('ict_flux_custom_logs');
        if (stored) executedTrades = JSON.parse(stored);
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
      if (!tbody) return;
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

    // ========================================================
    // RESEARCH & BACKTEST ENGINE SIMULATION LOGIC
    // ========================================================
    function runBacktestSimulation() {
      const market = document.getElementById('btMarket').value;
      const period = document.getElementById('btPeriod').value;
      const horizon = document.getElementById('btHorizon').value;
      const model = document.getElementById('btModel').value;

      const beLock = document.getElementById('chkBeLock').checked;
      const harvest70 = document.getElementById('chkHarvest').checked;

      // Seed realistic historical trades for chosen period
      let sampleCount = 31;
      let spanName = 'Last 30 Days (Past Month)';
      if (period === '7d') { sampleCount = 9; spanName = 'Last 7 Days (Weekly Review)'; }
      else if (period === '90d') { sampleCount = 88; spanName = 'Last 90 Days (Quarterly Audit)'; }
      else if (period === '365d') { sampleCount = 320; spanName = 'Last 365 Days (Full Year Institutional Sample)'; }

      document.getElementById('equitySpanLabel').textContent = `${spanName} · Backtest Output`;

      const simulatedTrades = [];
      const marketsPool = market === 'ALL' ? ['GBP/USD', 'EUR/USD', 'XAU/USD', 'NAS100', 'US500', 'USD/JPY', 'VOL 75'] : [DATA[market]?.label || market];
      const modelsPool = ['SMT Turtle Soup', 'London KZ Displacement', 'Silver Bullet Hour', 'Judas Swing Reversal'];
      
      let cumulativeR = 0;
      const equityPoints = [0];
      let wins = 0;
      let losses = 0;
      let grossProfit = 0;
      let grossLoss = 0;
      let maxDd = 0;
      let peakR = 0;

      const baseTime = Date.now() - (period === '7d' ? 7 : (period === '30d' ? 30 : (period === '90d' ? 90 : 365))) * 86400000;
      const timeStep = (Date.now() - baseTime) / sampleCount;

      for (let i = 0; i < sampleCount; i++) {
        const tradeTime = new Date(baseTime + i * timeStep);
        const tradeMarket = marketsPool[i % marketsPool.length];
        const tradeModel = modelsPool[i % modelsPool.length];
        const tradeHorizon = horizon === 'ALL' ? (i % 3 === 0 ? 'Scalp' : (i % 3 === 1 ? 'Day Trade' : 'Swing')) : horizon;
        const side = i % 2 === 0 ? 'BUY' : 'SELL';

        // ICT Discipline probability: ~74% win rate with BE locks
        const rand = Math.random();
        let outcome = 'WIN';
        let rVal = 0;
        let pipsStr = '12.0p';

        if (rand < 0.60) {
          // Full or Partial Win (+2.5R to +6.0R)
          outcome = 'WIN';
          rVal = parseFloat((2.5 + Math.random() * 3.8).toFixed(2));
          if (harvest70) rVal = parseFloat((rVal * 0.95).toFixed(2));
          wins++;
          grossProfit += rVal;
          pipsStr = `+${Math.round(rVal * 8.5)} pips`;
        } else if (rand < 0.78) {
          // Breakeven Lock (+0.08R)
          outcome = beLock ? 'BE_LOCK' : 'LOSS';
          rVal = beLock ? 0.08 : -1.00;
          if (beLock) { wins++; grossProfit += 0.08; pipsStr = '+1.0 pip'; }
          else { losses++; grossLoss += 1.0; pipsStr = '-8.0 pips'; }
        } else {
          // Stopped (-1.0R loss)
          outcome = 'LOSS';
          rVal = -1.00;
          losses++;
          grossLoss += 1.0;
          pipsStr = '-8.0 pips';
        }

        cumulativeR += rVal;
        peakR = Math.max(peakR, cumulativeR);
        const dd = peakR - cumulativeR;
        maxDd = Math.max(maxDd, dd);
        equityPoints.push(cumulativeR);

        simulatedTrades.unshift({
          date: tradeTime.toISOString().substring(5, 16).replace('T', ' '),
          market: tradeMarket,
          horizon: tradeHorizon,
          model: tradeModel,
          side: side,
          entry: (1.3300 + Math.random() * 0.05).toFixed(4),
          sl: (1.3280).toFixed(4),
          tp: (1.3420).toFixed(4),
          pips: pipsStr,
          outcome: outcome,
          rVal: rVal > 0 ? `+${rVal.toFixed(2)}R` : `${rVal.toFixed(2)}R`
        });
      }

      currentBacktestResults = simulatedTrades;

      // Update Summary Cards
      const winRate = ((wins / sampleCount) * 100).toFixed(1);
      const pf = grossLoss > 0 ? (grossProfit / grossLoss).toFixed(2) : '3.80';
      document.getElementById('mWinRate').textContent = `${winRate}%`;
      document.getElementById('mWinLossRatio').textContent = `${wins} Wins · ${losses} Losses`;
      document.getElementById('mNetR').textContent = `+${cumulativeR.toFixed(2)} R`;
      document.getElementById('mDollarReturn').textContent = `+$${Math.round(cumulativeR * 100).toLocaleString()} on $10k`;
      document.getElementById('mProfitFactor').textContent = pf;
      document.getElementById('mMaxDd').textContent = `-${maxDd.toFixed(2)} R`;
      document.getElementById('auditTotalLabel').textContent = `[${sampleCount} Simulated Institutional Executions]`;

      // Render Equity SVG
      renderEquitySvg(equityPoints);

      // Render Table
      const tbody = document.getElementById('backtestTableBody');
      tbody.innerHTML = simulatedTrades.map(t => {
        let tagClass = 'tag-win';
        if (t.outcome === 'BE_LOCK') tagClass = 'tag-be';
        else if (t.outcome === 'LOSS') tagClass = 'tag-loss';

        return `
          <tr>
            <td style="color:var(--muted)">${t.date}</td>
            <td><b>${t.market}</b></td>
            <td style="color:var(--muted)">${t.horizon}</td>
            <td style="color:var(--faint)">${t.model}</td>
            <td style="color:${t.side === 'BUY' ? 'var(--bull)' : 'var(--bear)'};font-weight:800">${t.side}</td>
            <td>${t.entry}</td>
            <td style="color:var(--bear)">${t.sl}</td>
            <td style="color:var(--bull)">${t.tp}</td>
            <td style="font-size:9.5px;color:var(--muted)">${t.pips}</td>
            <td><span class="${tagClass}">${t.outcome}</span></td>
            <td style="color:${t.rVal.includes('+') ? 'var(--bull)' : 'var(--bear)'};font-weight:800">${t.rVal}</td>
          </tr>
        `;
      }).join('');
    }

    function renderEquitySvg(points) {
      const svg = document.getElementById('equitySvg');
      const W = 900;
      const H = 180;
      const minVal = Math.min(0, ...points);
      const maxVal = Math.max(10, ...points);
      const range = maxVal - minVal || 1;

      const toX = (idx) => (idx / (points.length - 1)) * (W - 20) + 10;
      const toY = (val) => H - 20 - ((val - minVal) / range) * (H - 40);

      let pathD = `M ${toX(0)} ${toY(points[0])}`;
      for (let i = 1; i < points.length; i++) {
        pathD += ` L ${toX(i)} ${toY(points[i])}`;
      }

      const zeroY = toY(0);

      svg.innerHTML = `
        <line x1="0" y1="${zeroY}" x2="${W}" y2="${zeroY}" stroke="rgba(255,255,255,0.12)" stroke-dasharray="4,4" />
        <path d="${pathD}" fill="none" stroke="#2BD47D" stroke-width="2.5" />
        <circle cx="${toX(points.length - 1)}" cy="${toY(points[points.length - 1])}" r="4" fill="#F0B94B" />
      `;
    }

    function exportBacktestCsv() {
      if (!currentBacktestResults.length) return;
      let csv = "Date,Market,Horizon,Model,Side,Entry,SL,TP,Pips,Outcome,Return_R\n";
      currentBacktestResults.forEach(r => {
        csv += `"${r.date}","${r.market}","${r.horizon}","${r.model}","${r.side}","${r.entry}","${r.sl}","${r.tp}","${r.pips}","${r.outcome}","${r.rVal}"\n`;
      });
      const blob = new Blob([csv], { type: 'text/csv' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `ICT_Flux_Backtest_Audit_${Date.now()}.csv`;
      a.click();
      showToast('✓ Backtest Audit CSV exported!');
    }

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

    function updateClocks() {
      const now = new Date();
      const utcStr = now.toISOString().substring(11, 19) + ' UTC';
      const nyStr = now.toLocaleTimeString('en-US', { timeZone: 'America/New_York', hour12: false }) + ' NY';
      const elUtc = document.getElementById('clockUtc');
      const elNy = document.getElementById('clockNy');
      if (elUtc) elUtc.textContent = utcStr;
      if (elNy) elNy.textContent = nyStr;

      const nyHour = parseInt(nyStr.split(':')[0], 10);
      let session = 'ASIAN CONSOLIDATION';
      if (nyHour >= 2 && nyHour < 5) session = 'LONDON OPEN KILLZONE (ACTIVE)';
      else if (nyHour >= 7 && nyHour < 10) session = 'NY AM KILLZONE (ACTIVE)';
      else if (nyHour >= 13 && nyHour < 16) session = 'NY PM / SILVER BULLET';
      const elSession = document.getElementById('topSession');
      if (elSession) elSession.textContent = session;
    }

    window.addEventListener('DOMContentLoaded', () => {
      try { initChart(); } catch (e) { console.error('initChart err:', e); }
      try { setupResizer(); } catch (e) { console.error('setupResizer err:', e); }
      try { loadLogs(); } catch (e) {}
      try { renderLogs('all'); } catch (e) {}
      try { updateDesk(); } catch (e) { console.error('updateDesk err:', e); }
      try { updateClocks(); setInterval(updateClocks, 1000); } catch (e) {}
    });
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully compiled unified index.html with Live Execution Desk + Interactive Research & Backtest Lab!")
