# seetoo-strategy-analysis 實作計畫

**Goal:** 在 `seetoo-strategy-core` 上，建一支把司徒達賢策略形態分析法施加到具體事業、產出有紀律分析報告的技能。

**Architecture:** SKILL.md（程序＋紀律＋消費 core）＋ 3 份 reference（intake 清單、報告範本、worked example）。內容為**自行撰寫的編排層**（非 PDF 蒸餾），故採直接撰寫＋一個 Opus 審查 agent＋一次實跑驗證。

**依賴：** core 已存在且 symlink；本分支 `feat/seetoo-strategy-analysis` 自 core 分支而來。

---

### Task 1：SKILL.md
- Create `skills/seetoo-strategy-analysis/SKILL.md`：frontmatter（觸發描述）、先載入 core、兩種不杜撰紀律＋三分區、十步驟程序、兩模式、消費 core 對照表、自檢清單。
- 驗證：`head -3` 看 frontmatter；人工讀過程序與 core 檔名一致。

### Task 2：intake 清單
- Create `references/intake-清單.md`：依六大構面（產市垂規地競）＋環條目（環境/條件/目標組合）列出「描述現狀」要蒐集的事實問題；缺漏標〔待問〕的規則。

### Task 3：分析報告範本
- Create `references/分析報告範本.md`：固定區段對應十步驟；每段註明用【事實】/【框架】(附 core 出處)/【判斷】(標推測) 分區。

### Task 4：worked example（鬍鬚張）
- 先 Read core `references/10-案例庫.md`（必要時 01/02）取得鬍鬚張**真實事實**（不另編）。
- Create `references/worked-example-鬍鬚張.md`：用本技能完整走一遍，示範品質與三分區；框架處附 core 出處。

### Task 5：驗證
- 派 1 個 Opus 審查 agent：檢查 (a) 是否正確消費 core、(b) 紀律（三分區、術語鎖、不從 SWOT 起手）、(c) worked example 引用的 core 內容與 core 檔一致、(d) 無捏造事業事實。
- 實跑測試：對一個「資訊很少」的假想事業跑一次，確認走形態速寫並大量標〔待問〕、不編事實。

### Task 6：部署與 PR
- symlink `skills/seetoo-strategy-analysis` → `~/.claude/skills/`。
- 更新 CHANGELOG。commit、push、`gh pr create --base feat/seetoo-strategy-core`（stacked PR）。

---

## Self-Review（對照 spec）
| spec | task |
|---|---|
| §1 定位、§3 程序、§5 消費 core、§2 兩風險紀律 | Task 1 |
| §4 intake | Task 2 |
| §5 輸出三分區 | Task 3 |
| §6 worked example | Task 4 |
| §6 驗證/紀律測試 | Task 5 |
| §8 位置/分支/PR | Task 6 |
