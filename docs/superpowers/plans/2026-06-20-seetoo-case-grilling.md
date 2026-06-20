# seetoo-case-grilling 實作計畫

**Goal:** 在 `seetoo-strategy-core` 上，建一支「司徒達賢個案教學式拷問」技能：對使用者的事業/主張不斷追問、不放過含糊、扣回方法，逼出嚴謹思考。

**Architecture:** SKILL.md（拷問協定＋persona＋消費 core）＋ 3 份 reference（提問庫、拷問流程、worked-example 對話）。內容為自撰編排層；採直接撰寫＋ 1 個 Opus 審查＋紀律測試。

**依賴：** core 已存在且 symlink；分支 `feat/seetoo-case-grilling`（自 analysis，linear stack）。

---

### Task 1：SKILL.md
- frontmatter（觸發：拷問/challenge 我的策略、個案討論、壓力測試策略想法）、persona（司徒達賢個案教學）、拷問協定、不杜撰兩面、反主張攔截、消費 core 表、何時收、自檢。

### Task 2：references/提問庫.md
- 依核心概念分類的追問彈藥（六大構面/前提/因果/非答案/反主張/道理），每類附 core 錨。

### Task 3：references/拷問流程.md
- 一場拷問流程：開場→形態→構想/前提→因果壓力測試→反主張攔截→收斂與摘要。

### Task 4：references/worked-example-對話.md
- 一段示範拷問對話（拷問一個含糊策略主張），展示「不放過含糊／分辨事實vs推測／逼出前提／扣回 core」。

### Task 5：驗證
- 1 個 Opus 審查 agent：(a) 正確消費 core、(b) 紀律（蘇格拉底式不說教、不替使用者編事業事實、術語鎖、反主張攔截）、(c) 提問庫每類錨點對得上 core、(d) 與 grill-me 區隔清楚。
- 紙上紀律測試：含糊答案→是否會追問；SWOT 起手→是否攔截。

### Task 6：部署與 PR
- symlink；更新 CHANGELOG；commit、push、`gh pr create --base feat/seetoo-strategy-analysis`。

---

## Self-Review（對照 spec）
| spec | task |
|---|---|
| §1/§3 定位與拷問協定、§4 紀律、§5 消費 core | Task 1 |
| §6 提問庫 | Task 2 |
| §7 拷問流程 | Task 3 |
| §8 worked example | Task 4 |
| §8 驗證/紀律測試、§2 與 grill-me 區隔 | Task 5 |
| §10 位置/分支/PR | Task 6 |
