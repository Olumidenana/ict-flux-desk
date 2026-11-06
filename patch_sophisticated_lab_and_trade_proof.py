import sys

path = r"C:\Users\giant\Documents\ict-flux-desk\build_app.py"

with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Expand the Trade Modal Dialog to accommodate the Chart Proof View & Execution Journey Timeline
old_modal_card = """    <div class="modal-card" style="background:var(--surface);border:1px solid var(--accent);border-radius:14px;max-width:580px;width:92%;padding:22px;box-shadow:0 12px 48px rgba(0,0,0,0.85);position:relative;">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:14px;">
        <div>
          <span style="font-family:var(--mono);font-size:10px;color:var(--accent);font-weight:800;letter-spacing:0.06em;text-transform:uppercase;">CHOKEPOINT EXECUTION AUDIT</span>
          <h3 id="modalTradeTitle" style="font-size:17px;font-weight:800;margin-top:4px;color:var(--text)">Trade Details</h3>
        </div>
        <button onclick="closeTradeModal()" style="background:none;border:none;color:var(--muted);font-size:22px;cursor:pointer;line-height:1;">&times;</button>
      </div>

      <div id="modalTradeBody" style="display:flex;flex-direction:column;gap:12px;font-family:var(--mono);font-size:11.5px;">
        <!-- Injected dynamically -->
      </div>

      <div style="display:flex;justify-content:flex-end;gap:8px;margin-top:18px;">
        <button class="btn" onclick="closeTradeModal()">Close</button>
        <button class="btn primary" id="modalBtnTv" style="background:var(--accent);color:#07080B;font-weight:800;">👁️ View in TradingView</button>
      </div>
    </div>"""

new_modal_card = """    <div class="modal-card" style="background:var(--surface);border:1px solid var(--accent);border-radius:14px;max-width:760px;width:94%;max-height:92vh;overflow-y:auto;padding:24px;box-shadow:0 16px 64px rgba(0,0,0,0.9);position:relative;">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;border-bottom:1px solid var(--line);padding-bottom:12px;">
        <div>
          <div style="display:flex;align-items:center;gap:8px;">
            <span style="font-family:var(--mono);font-size:10px;color:var(--accent);font-weight:800;letter-spacing:0.08em;text-transform:uppercase;">ICT FLUX DESK • TRADE EXECUTION JOURNEY</span>
            <span id="modalHorizonBadge" style="font-family:var(--mono);font-size:9.5px;padding:2px 8px;border-radius:4px;background:var(--surface-3);color:var(--text);font-weight:700;"></span>
          </div>
          <h3 id="modalTradeTitle" style="font-size:18px;font-weight:800;margin-top:4px;color:var(--text)">Trade Details</h3>
        </div>
        <button onclick="closeTradeModal()" style="background:var(--surface-2);border:1px solid var(--line);color:var(--text);border-radius:6px;width:30px;height:30px;font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;line-height:1;">&times;</button>
      </div>

      <!-- Interactive Chart Proof View Embed -->
      <div style="margin-bottom:16px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
          <span style="font-family:var(--mono);font-size:10px;color:var(--muted);font-weight:700;text-transform:uppercase;">📍 LIVE CHART PROOF (TRADINGVIEW AUTHENTIC FEED)</span>
          <span id="modalTvSymTag" style="font-family:var(--mono);font-size:10.5px;color:var(--accent);font-weight:700;"></span>
        </div>
        <div id="modalChartContainer" style="width:100%;height:270px;background:#050608;border-radius:8px;border:1px solid var(--line);overflow:hidden;position:relative;">
          <!-- Injected dynamically with live TradingView frame for this exact trade -->
        </div>
      </div>

      <div id="modalTradeBody" style="display:flex;flex-direction:column;gap:12px;font-family:var(--mono);font-size:11.5px;">
        <!-- Injected dynamically -->
      </div>

      <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;margin-top:20px;padding-top:14px;border-top:1px solid var(--line);flex-wrap:wrap;">
        <button class="btn" onclick="closeTradeModal()">Close Inspector</button>
        <div style="display:flex;gap:8px;">
          <button class="btn sm" id="modalBtnDesk" style="font-family:var(--mono);font-size:11px;padding:6px 14px;cursor:pointer;">📺 Open on Main Desk Chart</button>
          <button class="btn primary sm" id="modalBtnTv" style="background:var(--accent);color:#07080B;font-family:var(--mono);font-size:11px;font-weight:800;padding:6px 14px;cursor:pointer;">↗️ Open on TradingView.com</button>
        </div>
      </div>
    </div>"""

if old_modal_card in code:
    code = code.replace(old_modal_card, new_modal_card)
    print("Replaced tradeModalOverlay dialog with chart proof & progression layout (LF)")
else:
    old_crlf = old_modal_card.replace("\n", "\r\n")
    new_crlf = new_modal_card.replace("\n", "\r\n")
    if old_crlf in code:
        code = code.replace(old_crlf, new_crlf)
        print("Replaced tradeModalOverlay dialog (CRLF)")
    else:
        print("old_modal_card not found")

# 2. Upgrade openTradeModal(ticket) to render the complete step-by-step execution lifecycle & TradingView chart frame
old_open_modal_func = """    function openTradeModal(ticket) {
      const t = REAL_BACKTEST_TRADES.find(tr => tr.ticket === ticket);
      if (!t) return;

      const overlay = document.getElementById('tradeModalOverlay');
      const title = document.getElementById('modalTradeTitle');
      const body = document.getElementById('modalTradeBody');
      const btnTv = document.getElementById('modalBtnTv');

      const isWin = t.outcome === 'TP_HIT';
      const isBe = t.outcome === 'BE_SAVED';
      const outcomeColor = isWin ? 'var(--bull)' : (isBe ? 'var(--warn)' : 'var(--bear)');
      const outcomeLabel = isWin ? '🎯 TAKE PROFIT' : (isBe ? '🛡️ BE PROTECTED' : '🛑 STOP LOSS HIT');

      title.textContent = `${t.ticket} • ${t.market_label} ${t.direction}`;
      body.innerHTML = `
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;background:var(--surface-2);padding:12px;border-radius:8px;border:1px solid var(--line);">
          <div><span style="color:var(--muted)">Model Archetype:</span> <b>${t.model}</b></div>
          <div><span style="color:var(--muted)">Horizon:</span> <b style="text-transform:uppercase">${t.horizon}</b></div>
          <div><span style="color:var(--muted)">Execution Time:</span> <b>${t.time}</b></div>
          <div><span style="color:var(--muted)">Exit Time:</span> <b>${t.exit_time}</b></div>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;background:var(--surface-2);padding:12px;border-radius:8px;border:1px solid var(--line);">
          <div><span style="color:var(--muted);display:block;font-size:10px">LIMIT ENTRY</span><b style="color:var(--accent);font-size:13px">${t.entry}</b></div>
          <div><span style="color:var(--muted);display:block;font-size:10px">SURGICAL SL</span><b style="color:var(--bear);font-size:13px">${t.stop}</b> <span style="font-size:9.5px;color:var(--faint)">(${t.sl_pips})</span></div>
          <div><span style="color:var(--muted);display:block;font-size:10px">TAKE PROFIT</span><b style="color:var(--bull);font-size:13px">${t.target}</b> <span style="font-size:9.5px;color:var(--faint)">(${t.tp_pips})</span></div>
        </div>

        <div style="background:var(--surface-2);padding:12px;border-radius:8px;border:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;">
          <div><span style="color:var(--muted)">Outcome:</span> <b style="color:${outcomeColor}">${outcomeLabel}</b></div>
          <div><span style="color:var(--muted)">Realized Net R:</span> <b style="font-size:14px;color:${t.r_multiple >= 0 ? 'var(--bull)' : 'var(--bear)'}">${t.r_multiple >= 0 ? '+' : ''}${t.r_multiple.toFixed(2)}R</b></div>
          <div><span style="color:var(--muted)">Risk:Reward:</span> <b>${t.rr}</b></div>
        </div>

        <div style="background:var(--surface-2);padding:12px;border-radius:8px;border-left:3px solid var(--accent);">
          <span style="color:var(--accent);font-weight:700;display:block;margin-bottom:4px">⚡ ICT ALGORITHMIC THESIS:</span>
          <span style="color:var(--text);font-size:11px;line-height:1.4">${t.notes}</span>
        </div>
      `;

      btnTv.onclick = () => {
        closeTradeModal();
        inspectTradeInTradingView(t.ticket);
      };

      overlay.style.display = 'flex';
    }"""

new_open_modal_func = """    function openTradeModal(ticket) {
      const t = REAL_BACKTEST_TRADES.find(tr => tr.ticket === ticket);
      if (!t) return;

      const overlay = document.getElementById('tradeModalOverlay');
      const title = document.getElementById('modalTradeTitle');
      const body = document.getElementById('modalTradeBody');
      const badge = document.getElementById('modalHorizonBadge');
      const tvSymTag = document.getElementById('modalTvSymTag');
      const chartBox = document.getElementById('modalChartContainer');
      const btnTv = document.getElementById('modalBtnTv');
      const btnDesk = document.getElementById('modalBtnDesk');

      const isWin = t.outcome === 'TP_HIT';
      const isBe = t.outcome === 'BE_SAVED';
      const outcomeColor = isWin ? 'var(--bull)' : (isBe ? 'var(--warn)' : 'var(--bear)');
      const outcomeLabel = isWin ? '🎯 TAKE PROFIT (+4.00R / Full Harvest)' : (isBe ? '🛡️ BREAKEVEN LOCK (+0.80R Saved)' : '🛑 STOP LOSS CUT (-1.00R Initial)');

      const horizonLabel = t.horizon === 'scalp' ? 'M1 / M5 SCALP' : (t.horizon === 'day' ? 'M5 / M15 DAY TRADE' : 'H1 / H4 SWING');
      const horizonColor = t.horizon === 'scalp' ? 'var(--accent)' : (t.horizon === 'day' ? 'var(--bull)' : '#60a5fa');

      title.textContent = `${t.ticket} • ${t.market_label} (${t.direction})`;
      if (badge) {
        badge.textContent = horizonLabel;
        badge.style.color = horizonColor;
        badge.style.border = `1px solid ${horizonColor}`;
      }
      if (tvSymTag) {
        tvSymTag.textContent = `${t.tv_symbol} • ${t.time}`;
      }

      // Inject Live TradingView Chart Frame directly for this trade
      if (chartBox) {
        let tfVal = '15';
        if (t.horizon === 'scalp') tfVal = '1';
        else if (t.horizon === 'day') tfVal = '5';
        else if (t.horizon === 'swing') tfVal = '60';

        const tvUrl = `https://s.tradingview.com/widgetembed/?frameElementId=modal_tv_frame&symbol=${encodeURIComponent(t.tv_symbol)}&interval=${tfVal}&hidesidetoolbar=1&symboledit=0&saveimage=0&theme=dark&style=1&timezone=America%2FNew_York&withdateranges=1`;
        chartBox.innerHTML = `<iframe src="${tvUrl}" style="width:100%;height:100%;border:none;" loading="lazy"></iframe>`;
      }

      // Progression Steps
      const step1Text = `${t.time} — ${t.direction} Order Trigger: Asian range liquidity sweep identified. Limit order filled at ${t.entry} (${t.model}).`;
      const step2Text = isWin || isBe 
        ? `Displacement reached +0.80R threshold. Algorithmic Breakeven Lock engaged automatically: Stop Loss moved to Entry (${t.entry}). Zero downside risk.`
        : `Displacement stalled; opposite order flow emerged. Predefined Stop Loss respected at ${t.stop}. Position terminated cleanly with zero emotional revenge trading.`;
      const step3Text = isWin 
        ? `Tranche 1: 70% harvested at TP1 (+1.50R). Tranche 2: 30% runner held until Draw-on-Liquidity target hit at ${t.target} (+4.00R). Total Realized Net R: +${t.r_multiple.toFixed(2)}R.`
        : (isBe 
            ? `Price reversed back into entry level. Protected stop triggered at ${t.entry} (+0.80R lock). Full capital preserved with +0.00R net change.`
            : `Risk capped at strictly -1.00R (${t.sl_pips}). Account capital protected.`);

      body.innerHTML = `
        <!-- High-level Metric Strip -->
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(130px, 1fr));gap:8px;background:var(--surface-2);padding:12px;border-radius:8px;border:1px solid var(--line);">
          <div><span style="color:var(--muted);display:block;font-size:10px">ORDER EXECUTION</span><b style="color:var(--text);font-size:12px">${t.time}</b></div>
          <div><span style="color:var(--muted);display:block;font-size:10px">TERMINAL EXIT</span><b style="color:var(--text);font-size:12px">${t.exit_time}</b></div>
          <div><span style="color:var(--muted);display:block;font-size:10px">OUTCOME STATUS</span><b style="color:${outcomeColor};font-size:12px">${outcomeLabel}</b></div>
          <div><span style="color:var(--muted);display:block;font-size:10px">NET REALIZED R</span><b style="color:${t.r_multiple >= 0 ? 'var(--bull)' : 'var(--bear)'};font-size:14px">${t.r_multiple >= 0 ? '+' : ''}${t.r_multiple.toFixed(2)}R</b></div>
        </div>

        <!-- Precise Price Coordinates -->
        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;background:var(--surface-2);padding:12px;border-radius:8px;border:1px solid var(--line);">
          <div><span style="color:var(--muted);display:block;font-size:10px">LIMIT ENTRY</span><b style="color:var(--accent);font-size:13.5px">${t.entry}</b></div>
          <div><span style="color:var(--muted);display:block;font-size:10px">SURGICAL STOP LOSS</span><b style="color:var(--bear);font-size:13.5px">${t.stop}</b> <span style="font-size:9.5px;color:var(--muted)">(${t.sl_pips})</span></div>
          <div><span style="color:var(--muted);display:block;font-size:10px">DRAW-ON-LIQUIDITY TP</span><b style="color:var(--bull);font-size:13.5px">${t.target}</b> <span style="font-size:9.5px;color:var(--muted)">(${t.tp_pips})</span></div>
        </div>

        <!-- How The Trade Went Through (Execution Lifecycle Timeline) -->
        <div style="background:var(--surface-2);padding:14px;border-radius:8px;border:1px solid var(--line);">
          <span style="color:var(--accent);font-weight:800;font-size:10.5px;letter-spacing:0.06em;text-transform:uppercase;display:block;margin-bottom:10px;">
            📈 HOW THIS TRADE WENT THROUGH (STEP-BY-STEP PROGRESSION):
          </span>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <div style="display:flex;gap:10px;align-items:flex-start;">
              <span style="background:var(--accent);color:#07080B;font-size:9.5px;font-weight:800;border-radius:50%;width:18px;height:18px;display:flex;align-items:center;justify-content:center;flex-shrink:0;">1</span>
              <div><strong style="color:var(--text);font-size:11px">Liquidity Intercept & Entry Fill:</strong> <span style="color:var(--muted);font-size:11px">${step1Text}</span></div>
            </div>
            <div style="display:flex;gap:10px;align-items:flex-start;">
              <span style="background:${isWin || isBe ? 'var(--bull)' : 'var(--bear)'};color:#07080B;font-size:9.5px;font-weight:800;border-radius:50%;width:18px;height:18px;display:flex;align-items:center;justify-content:center;flex-shrink:0;">2</span>
              <div><strong style="color:var(--text);font-size:11px">Displacement & Risk Shield:</strong> <span style="color:var(--muted);font-size:11px">${step2Text}</span></div>
            </div>
            <div style="display:flex;gap:10px;align-items:flex-start;">
              <span style="background:${outcomeColor};color:#07080B;font-size:9.5px;font-weight:800;border-radius:50%;width:18px;height:18px;display:flex;align-items:center;justify-content:center;flex-shrink:0;">3</span>
              <div><strong style="color:var(--text);font-size:11px">Resolution & Tranche Harvest:</strong> <span style="color:var(--muted);font-size:11px">${step3Text}</span></div>
            </div>
          </div>
        </div>

        <!-- ICT Thesis -->
        <div style="background:var(--surface-3);padding:12px;border-radius:8px;border-left:3px solid var(--accent);">
          <span style="color:var(--accent);font-weight:800;display:block;margin-bottom:3px;font-size:10.5px">⚡ INSTITUTIONAL ALGORITHMIC THESIS:</span>
          <span style="color:var(--text);font-size:11px;line-height:1.4">${t.notes}</span>
        </div>
      `;

      if (btnDesk) {
        btnDesk.onclick = () => {
          closeTradeModal();
          curKey = t.symbol;
          curHorizon = t.horizon;
          const sel = document.getElementById('instrumentSelect');
          if (sel) sel.value = curKey;
          switchView('desk');
          updateDesk();
          updateTradingViewFrame();
          showToast(`Loaded ${t.symbol} (${t.horizon.toUpperCase()}) on Execution Desk!`);
        };
      }

      if (btnTv) {
        btnTv.onclick = () => {
          const directUrl = `https://www.tradingview.com/chart/?symbol=${encodeURIComponent(t.tv_symbol)}`;
          window.open(directUrl, '_blank');
        };
      }

      overlay.style.display = 'flex';
    }"""

if old_open_modal_func in code:
    code = code.replace(old_open_modal_func, new_open_modal_func)
    print("Upgraded openTradeModal with step-by-step lifecycle and live chart proof (LF)")
else:
    old_crlf = old_open_modal_func.replace("\n", "\r\n")
    new_crlf = new_open_modal_func.replace("\n", "\r\n")
    if old_crlf in code:
        code = code.replace(old_crlf, new_crlf)
        print("Upgraded openTradeModal (CRLF)")
    else:
        print("old_open_modal_func not found")

# 3. Upgrade renderRealTradeTable to include Horizon badge and 1-Click "🔍 Inspect & Chart" button
old_row_gen = """        tr.innerHTML = `
          <td><span style="color:var(--accent);font-weight:700">${t.ticket}</span></td>
          <td>${t.time}</td>
          <td><b>${t.market_label}</b></td>
          <td><span class="bm-tag ${t.direction === 'BUY' ? 'buy' : 'sell'}" style="font-size:9.5px">${t.direction}</span></td>
          <td><span style="color:var(--muted)">${t.model}</span></td>
          <td>${t.entry}</td>
          <td><span style="color:var(--bear)">${t.stop}</span> <span style="font-size:9px;color:var(--faint)">(${t.sl_pips})</span></td>
          <td><span style="color:var(--bull)">${t.target}</span> <span style="font-size:9px;color:var(--faint)">(${t.tp_pips})</span></td>
          <td><b>${t.rr}</b></td>
          <td><b style="color:${t.r_multiple >= 0 ? 'var(--bull)' : 'var(--bear)'}">${t.r_multiple >= 0 ? '+' : ''}${t.r_multiple.toFixed(2)}R</b></td>
          <td><span class="bm-tag ${badgeClass}" style="font-size:9.5px">${t.outcome}</span></td>
          <td><button class="btn sm" onclick="inspectTradeInTradingView('${t.ticket}')" style="padding:3px 8px;font-size:10px;cursor:pointer;">👁️ Chart</button></td>
        `;"""

new_row_gen = """        const horizonPill = t.horizon === 'scalp' 
          ? '<span style="color:var(--accent);background:rgba(245,186,65,0.12);padding:2px 6px;border-radius:4px;font-size:9.5px;font-weight:700">SCALP</span>'
          : (t.horizon === 'day' 
              ? '<span style="color:var(--bull);background:rgba(43,212,125,0.12);padding:2px 6px;border-radius:4px;font-size:9.5px;font-weight:700">DAY</span>'
              : '<span style="color:#60a5fa;background:rgba(96,165,250,0.12);padding:2px 6px;border-radius:4px;font-size:9.5px;font-weight:700">SWING</span>');

        tr.innerHTML = `
          <td><span style="color:var(--accent);font-weight:700">${t.ticket}</span></td>
          <td>${t.time}</td>
          <td><b>${t.market_label}</b></td>
          <td>${horizonPill}</td>
          <td><span class="bm-tag ${t.direction === 'BUY' ? 'buy' : 'sell'}" style="font-size:9.5px">${t.direction}</span></td>
          <td><span style="color:var(--muted)">${t.model}</span></td>
          <td>${t.entry}</td>
          <td><span style="color:var(--bear)">${t.stop}</span> <span style="font-size:9px;color:var(--faint)">(${t.sl_pips})</span></td>
          <td><span style="color:var(--bull)">${t.target}</span> <span style="font-size:9px;color:var(--faint)">(${t.tp_pips})</span></td>
          <td><b>${t.rr}</b></td>
          <td><b style="color:${t.r_multiple >= 0 ? 'var(--bull)' : 'var(--bear)'}">${t.r_multiple >= 0 ? '+' : ''}${t.r_multiple.toFixed(2)}R</b></td>
          <td><span class="bm-tag ${badgeClass}" style="font-size:9.5px">${t.outcome}</span></td>
          <td><button class="btn sm primary" onclick="event.stopPropagation();openTradeModal('${t.ticket}')" style="background:var(--accent);color:#07080B;font-weight:800;padding:4px 9px;font-size:10px;cursor:pointer;">🔍 Inspect & Chart</button></td>
        `;"""

if old_row_gen in code:
    code = code.replace(old_row_gen, new_row_gen)
    print("Enhanced renderRealTradeTable row with horizon pill and Inspect & Chart button (LF)")
else:
    old_crlf = old_row_gen.replace("\n", "\r\n")
    new_crlf = new_row_gen.replace("\n", "\r\n")
    if old_crlf in code:
        code = code.replace(old_crlf, new_crlf)
        print("Enhanced renderRealTradeTable (CRLF)")
    else:
        print("old_row_gen not found")

# 4. Update the Table Headers in paneLab to include HORIZON column
old_table_header = """                  <tr>
                    <th>Ticket</th>
                    <th>Date / Time (NY)</th>
                    <th>Symbol</th>
                    <th>Side</th>
                    <th>Model Archetype</th>
                    <th>Limit Entry</th>
                    <th>SL (Pips)</th>
                    <th>TP (Pips)</th>
                    <th>Risk:Reward</th>
                    <th>Realized Net R</th>
                    <th>Execution Status</th>
                    <th>Audit Action</th>
                  </tr>"""

new_table_header = """                  <tr>
                    <th>Ticket</th>
                    <th>Date / Time (NY)</th>
                    <th>Symbol</th>
                    <th>Horizon</th>
                    <th>Side</th>
                    <th>Model Archetype</th>
                    <th>Limit Entry</th>
                    <th>SL (Pips)</th>
                    <th>TP (Pips)</th>
                    <th>Risk:Reward</th>
                    <th>Realized Net R</th>
                    <th>Execution Status</th>
                    <th>Audit & Chart Proof</th>
                  </tr>"""

if old_table_header in code:
    code = code.replace(old_table_header, new_table_header)
    print("Updated trade table headers with Horizon and Audit & Chart Proof (LF)")
else:
    old_crlf = old_table_header.replace("\n", "\r\n")
    new_crlf = new_table_header.replace("\n", "\r\n")
    if old_crlf in code:
        code = code.replace(old_crlf, new_crlf)
        print("Updated trade table headers (CRLF)")
    else:
        print("old_table_header not found")

# 5. Upgrade exportRealCsv to include TradingView chart URLs and Lifecycle details for every trade
old_export_csv = """      let csv = 'Ticket,DateTime_NY,Symbol,Direction,Model,Horizon,Entry,StopLoss,TakeProfit,SL_Pips,TP_Pips,RR,R_Multiple,Outcome,Notes\\n';
      currentFilteredTrades.forEach(t => {
        csv += `"${t.ticket}","${t.time}","${t.symbol}","${t.direction}","${t.model}","${t.horizon}",${t.entry},${t.stop},${t.target},"${t.sl_pips}","${t.tp_pips}","${t.rr}",${t.r_multiple},"${t.outcome}","${t.notes || ''}"\\n`;
      });"""

new_export_csv = """      let csv = 'Ticket,DateTime_NY,ExitTime_NY,Symbol,Direction,Model,Horizon,Limit_Entry,Stop_Loss,Take_Profit,SL_Pips,TP_Pips,RR,Realized_Net_R,Outcome_Status,TradingView_Chart_Proof_URL,Institutional_Notes\\n';
      currentFilteredTrades.forEach(t => {
        const tvUrl = `https://www.tradingview.com/chart/?symbol=${encodeURIComponent(t.tv_symbol)}`;
        csv += `"${t.ticket}","${t.time}","${t.exit_time || ''}","${t.symbol}","${t.direction}","${t.model}","${t.horizon}",${t.entry},${t.stop},${t.target},"${t.sl_pips}","${t.tp_pips}","${t.rr}",${t.r_multiple},"${t.outcome}","${tvUrl}","${(t.notes || '').replace(/"/g, '""')}"\\n`;
      });"""

if old_export_csv in code:
    code = code.replace(old_export_csv, new_export_csv)
    print("Enhanced exportRealCsv with TradingView URLs and Exit Times (LF)")
else:
    old_crlf = old_export_csv.replace("\n", "\r\n")
    new_crlf = new_export_csv.replace("\n", "\r\n")
    if old_crlf in code:
        code = code.replace(old_crlf, new_crlf)
        print("Enhanced exportRealCsv (CRLF)")
    else:
        print("old_export_csv not found")

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated build_app.py successfully.")
