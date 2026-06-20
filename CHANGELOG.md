# Changelog

本專案所有重要變更都記錄於此。
格式依循 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/)，
版本依循 [Semantic Versioning](https://semver.org/lang/zh-TW/)。

## [0.1.0] - 2026-06-20

### Added
- 專案初始化：目錄結構、`README.md`、`CHANGELOG.md`、`LICENSE`、`NOTICE`、`.gitignore`。
- 以 brainstorming 完成整體拆解：一個共用核心 + 三支獨立技能
  （core / strategy-analysis / case-grilling / strategy-tutor），並定下建造順序。
- `seetoo-strategy-core` 設計規格：
  [`docs/superpowers/specs/2026-06-20-seetoo-strategy-core-design.md`](docs/superpowers/specs/2026-06-20-seetoo-strategy-core-design.md)
  （雙層「忠實×操作」取向、雙層模板、反杜撰紀律機制、驗證方式）。
- **`seetoo-strategy-core` v0.1 實作完成**：11 份雙層 reference 檔（`00-術語表`～`10-案例庫`）、
  `SKILL.md`（檢索紀律＋reference 地圖）、`tools/audit_core.py`＋`tools/gen_index.py`、
  `章節索引.md`、`版本.md`。逐章 implementer→spec審→品質審（全 Opus），全數通過可回溯稽核，
  並經最終全案審查（獨立開 PDF 逐字核對）：0 杜撰、0 待查，已修正 4 處逐字 typo。
- **`seetoo-strategy-analysis` v0.1 實作完成**：站在 core 上的策略分析引擎——`SKILL.md`（十步驟程序、
  兩模式、兩種不杜撰、三分區【事實】/【框架】/【判斷】、反主張起手紅線）、`intake-清單.md`、
  `分析報告範本.md`、`worked-example-鬍鬚張.md`（事實全可回溯 core 案例庫）。經 Opus 審查判定 READY。
- core `10-案例庫`：標註講義原文「開放加盟」年份不一致（內文 1984／表 1982 並陳，不擅自擇一）。
- **`seetoo-case-grilling` v0.1 實作完成**：站在 core 上的個案拷問教練——`SKILL.md`（拷問協定、
  司徒達賢個案教學 persona、反主張攔截、不腦補事業事實、蘇格拉底式以問為主）、`提問庫.md`、
  `拷問流程.md`、`worked-example-對話.md`。扣回 core；經 Opus 審查判定 READY。
- **`seetoo-strategy-tutor` v0.1 實作完成**：站在 core 上的講義學習助教——`SKILL.md`（講解/帶練/出題/批改
  四模式、忠實教學、不杜撰、【講義】vs【教學鷹架】分層、鼓勵式）、`學習路徑.md`、`出題與批改規準.md`、
  `worked-example-教學.md`。扣回 core；經 Opus 審查判定 READY。
- 命名修正：`seeto-case-grilling`（曾誤拼）已更正回 `seetoo-case-grilling`。
- `seetoo-strategy-tutor` 增強：解析第九章附錄《策略矩陣例題及習題》(`.ppsx`，387 張) 與第十章附錄
  《產業矩陣》(`.xls`)，新增 `references/例題習題庫.md`（用途與價值、產業矩陣範本、題號系列索引 101–207、
  103 系列 8 題習題）；經 Opus 忠實度審查、修正後對齊原文（原始檔仍不發佈）。

### 里程碑
- 四支技能（core／analysis／case-grilling／strategy-tutor）v0.1 全部完成並合併至 `main`。
