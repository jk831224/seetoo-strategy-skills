# 司徒達賢策略管理 Skills（Seetoo Strategy Skills）

> 以司徒達賢《策略管理講義》為本，打造一組「非常有紀律與脈絡」的 Claude Code 技能。
>
> A disciplined, source-grounded set of Claude Code skills distilled from
> Prof. Seetoo Dah-Hsian's (司徒達賢) strategic-management lectures.

## 這是什麼

把司徒達賢的策略管理「思維方式」，蒸餾成可被 AI **忠實、有紀律**地運用的技能組。
一切以講義原文為錨——不杜撰、不混入一般 MBA 術語。

## 架構

一個共用知識核心 + 三支獨立技能：

| 技能 | 角色 | 產物 |
|---|---|---|
| **seetoo-strategy-core** | 共用核心（雙層：忠實×操作） | 蒸餾版講義知識庫 |
| **seetoo-strategy-analysis** | 策略分析引擎 | 用策略形態分析法＋策略矩陣產出分析 |
| **seetoo-case-grilling** | 個案拷問教練 | 用個案教學的紀律追問你的事業/個案 |
| **seetoo-strategy-tutor** | 講義學習助教 | 教學、例題習題、出題批改 |

建造順序：**核心 → 分析 → 拷問 → 學習**。

## 核心紀律（三條保證）

1. **術語鎖** — 鎖死司徒達賢用詞，不替換為一般 MBA 術語。
2. **原文錨定** — 每個操作主張都錨回原文；錨不回則標〔待查〕或不寫。
3. **反主張邊界** — 守第十一章主張：**不**從 SWOT / mission / 環境分析 / 設定目標 起手。

## 目前狀態

🚧 **早期開發中。** 已完成 `seetoo-strategy-core` 的設計規格
（見 [`docs/superpowers/specs/`](docs/superpowers/specs/)）。技能尚未實作。

## 結構

```
.
├── docs/superpowers/specs/   # 設計規格（spec）
├── skills/                   # 技能本體（開發中）
├── sources/                  # 原始講義 PDF（第三方著作權，不隨本 repo 發佈）
├── README.md
├── CHANGELOG.md
├── LICENSE
└── NOTICE
```

## 來源與版權

本專案蒸餾自《司徒達賢策略管理講義》（2024 年版，2025 年 2 月修訂），
原著作權歸 **司徒達賢 教授** 所有。詳見 [`NOTICE`](NOTICE)。

- 本 repo 中標示〔原文〕之逐字引用與〔摘述〕之轉述，著作權仍歸原作者，以註明出處方式引用。
- 原始講義 PDF（`sources/`）**不隨本 repo 發佈**。

## 授權

本專案的**原創部分**（技能架構、操作層、程式碼、文件）採 **MIT License**（見 [`LICENSE`](LICENSE)）。
講義原文引用部分不在 MIT 授權範圍內，著作權歸司徒達賢教授。

## 致謝

策略管理思想：**司徒達賢** 教授。
