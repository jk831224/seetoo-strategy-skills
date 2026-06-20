# seetoo-strategy-tutor 實作計畫

**Goal:** 在 `seetoo-strategy-core` 上，建一支「講義學習助教」：講解、帶練、出題、批改，帶使用者學會並內化司徒達賢方法，全程扣回原文。

**Architecture:** SKILL.md（四模式＋教學紀律＋消費 core）＋ 3 份 reference（學習路徑、出題與批改規準、worked-example 教學）。自撰編排層；直接撰寫＋ 1 個 Opus 審查＋紀律測試。

**依賴：** core 已存在且 symlink；分支 `feat/seetoo-strategy-tutor`（自 grilling，linear stack）。

---

### Task 1：SKILL.md
- frontmatter（觸發：教我司徒達賢策略/講解六大構面/出題考我/批改我的答案/我想學策略形態分析法）、四模式（講解/帶練/出題/批改）、教學紀律（忠實、不杜撰、【講義】vs【教學鷹架】分層、鼓勵式）、消費 core 表、學習路徑入口、自檢。

### Task 2：references/學習路徑.md
- 10 階段學習順序＋各階段學習目標，扣 core 各檔。

### Task 3：references/出題與批改規準.md
- 題型（概念/應用/案例）範例＋評分檢核點（術語、六大構面、找前提、事實vs待驗證、不從 SWOT 起手、因果），回饋指回 core 出處。

### Task 4：references/worked-example-教學.md
- 一段示範：講解「策略構想」→ 帶練（鬍鬚張，用 core `10`）→ 出一題 → 批改一份示範答案；全程【講義】(附出處)/【教學鷹架】分層。

### Task 5：驗證
- 1 個 Opus 審查 agent：(a) 正確消費 core、(b) 紀律（忠實/不杜撰/分層/鼓勵式且與 grilling 區隔）、(c) 學習路徑與評分規準扣得上 core、(d) worked example 引用 core 內容一致。
- 紙上紀律測試：超綱問題（OKR）→ 是否答「講義未涵蓋」；批改是否對照檢核點。

### Task 6：部署與 PR
- symlink；更新 CHANGELOG；commit、push、`gh pr create --base feat/seetoo-case-grilling`。

---

## Self-Review（對照 spec）
| spec | task |
|---|---|
| §1/§3 定位與四模式、§4 紀律、§8 消費 core、§2 與他技能區隔 | Task 1 |
| §6 學習路徑 | Task 2 |
| §7 出題與批改 | Task 3 |
| §9 worked example | Task 4 |
| §9 驗證/紀律測試 | Task 5 |
| §11 位置/分支/PR | Task 6 |
