# Changelog

本專案所有重要變更都記錄於此。
格式依循 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/)，
版本依循 [Semantic Versioning](https://semver.org/lang/zh-TW/)。

## [Unreleased]

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

### Planned
- `seetoo-strategy-analysis`、`seetoo-case-grilling`、`seetoo-strategy-tutor` 三支技能。
