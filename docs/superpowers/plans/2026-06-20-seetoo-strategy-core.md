# seetoo-strategy-core 實作計畫

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把《司徒達賢策略管理講義》蒸餾成一個「雙層（原文依據×操作層）」的 Claude Code 共用知識核心 `seetoo-strategy-core`，鎖術語、每個操作主張錨回原文、守第十一章反主張邊界。

**Architecture:** 一個 skill 目錄＝`SKILL.md`（地圖＋檢索紀律）＋ `references/` 11 份雙層主題檔（對應講義章節）＋ `章節索引.md` ＋ `版本.md`。以 repo 層 `tools/` 的 Python 稽核腳本強制結構與可回溯性；各章 reference 檔彼此獨立、可平行產出。完成後 symlink 到 `~/.claude/skills/`。

**Tech Stack:** Markdown reference docs；Python 3（稽核/索引腳本，無第三方套件）；Claude Code skill（progressive disclosure）。來源 PDF 在 `sources/`（建置期輸入，不發佈）。

---

## 執行前置（execution preconditions）

1. **分支**：執行起點先開 `feat/seetoo-strategy-core`（或用 superpowers:using-git-worktrees 建 worktree），完成後發 PR；不要直接動 `main`。
2. **不杜撰鐵則（最高優先）**：所有〔原文〕逐字引用**必須**從 `sources/` 對應 PDF 複製，**嚴禁**憑記憶或推測編造；查不到就標〔待查〕或留空。〔摘述〕須忠實對應原文語意並附出處。任何非講義內容只能標〔延伸·非講義〕。
3. **引用份量（公開 repo 著作權）**：〔原文〕只摘關鍵定義與招牌語句，不整段照搬；其餘用〔摘述〕。
4. **語言**：繁體中文，鎖司徒達賢術語。
5. **PDF 讀取**：用 Read 工具讀 `sources/<檔>`，章節 PDF 以明確頁碼範圍讀取（皆 ≤17 頁，單次可讀完）。

---

## 檔案結構（建置完成後）

```
skills/seetoo-strategy-core/
├── SKILL.md                       # 地圖＋檢索紀律＋自檢規則（Task 2）
├── references/
│   ├── 00-術語表.md                # Task 3
│   ├── 01-觀念架構與六大構面.md      # Task 4
│   ├── 02-策略構想與前提驗證.md      # Task 5
│   ├── 03-策略方案-構思評估選擇.md    # Task 6
│   ├── 04-功能政策與組織.md          # Task 7
│   ├── 05-十步驟程序.md             # Task 8
│   ├── 06-策略矩陣與產業矩陣.md       # Task 9
│   ├── 07-道理庫-經濟與產業經濟.md     # Task 10
│   ├── 08-道理庫-組織與決策理論.md     # Task 11
│   ├── 09-反主張與方法比較.md         # Task 12
│   └── 10-案例庫.md                # Task 13
├── 章節索引.md                     # 由 tools/gen_index.py 生成（Task 14）
└── 版本.md                        # Task 1
tools/
├── audit_core.py                  # 可回溯稽核（Task 1）
└── gen_index.py                   # 由 reference 檔來源標頭生成索引（Task 1）
```

---

## 蒸餾 SOP（每份 reference 檔的標準作業 — Task 4~13 一律套用此 SOP）

> 這是「一份 reference 檔」的共用作業程序。各章任務只提供三個參數：**來源檔/頁**、
> **須涵蓋的節**、**目標檔名**；步驟一律照下面跑，不另複述。

每份 reference 檔內容固定兩層，檔頭含來源標頭：

```markdown
# <主題>　〔出處：第X章 …〕
> 來源：<pdf 檔名> p.<起>–<迄>

## 原文依據
- 〔原文〕「<逐字摘自 PDF 的關鍵句>」（第X章·節, p.NN）
- 〔摘述〕<忠實轉述>（第X章·節, p.NN）
- 術語鎖：<本主題的 canonical 詞> — 不可替換為「<禁用的一般 MBA 詞>」

## 操作層
- [O1] <可執行的清單/程序/判準一條> ⟵錨:原文1
- [O2] <…> ⟵錨:原文2
```

**SOP 步驟（每份檔）：**
- **S1 讀來源**：用 Read 讀該章參數列出的 PDF 頁範圍。
- **S2 填原文依據**：逐節摘出關鍵定義/招牌語句為〔原文〕（逐字、附頁碼）；補〔摘述〕；列該主題的「術語鎖」與禁用替換詞。**查不到 ⇒ 標〔待查〕，不得編。**
- **S3 填操作層**：把原文轉成可執行清單/程序/判準；**每條結尾標 `⟵錨:原文N`** 指回某條原文依據。
- **S4 來源標頭**：檔頭加 `> 來源：<檔> p.X–Y`。
- **S5 稽核**：`python3 tools/audit_core.py`，該檔須 PASS（結構/出處/錨點齊全）。
- **S6 人工抽查**：隨機挑 1~2 條〔原文〕回 PDF 對照逐字無誤、頁碼正確。
- **S7 Commit**。

---

### Task 1: Scaffold 骨架 ＋ 稽核工具

**Files:**
- Create: `skills/seetoo-strategy-core/版本.md`
- Create: `skills/seetoo-strategy-core/references/.gitkeep`
- Create: `tools/audit_core.py`
- Create: `tools/gen_index.py`

- [ ] **Step 1: 建目錄與 .gitkeep**

```bash
mkdir -p skills/seetoo-strategy-core/references
touch skills/seetoo-strategy-core/references/.gitkeep
```

- [ ] **Step 2: 寫 `版本.md`**

```markdown
# 版本對應

- 蒸餾來源：《司徒達賢策略管理講義》2024 年版（最近修訂 2025 年 2 月，含目錄與重點摘要）。
- 來源檔：本 repo `sources/`（不隨 repo 發佈）。
- 本核心版本：v0.1（初版蒸餾）。
- 原文著作權歸 司徒達賢 教授；本核心僅以註明出處方式引用，詳見 repo NOTICE。
```

- [ ] **Step 3: 寫稽核腳本 `tools/audit_core.py`**

```python
#!/usr/bin/env python3
"""可回溯稽核：檢查 seetoo-strategy-core 每份 reference 檔的結構與可回溯性。"""
import re
import sys
import pathlib

CORE = pathlib.Path(__file__).resolve().parent.parent / "skills" / "seetoo-strategy-core"
REF = CORE / "references"
errors = []

def check(path):
    name = path.name
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if "## 原文依據" not in text:
        errors.append(f"{name}: 缺『## 原文依據』段")
    if "## 操作層" not in text:
        errors.append(f"{name}: 缺『## 操作層』段")
    if not re.search(r"^> 來源：.+p\.", text, re.M):
        errors.append(f"{name}: 缺『> 來源：… p.』標頭")

    # 〔原文〕/〔摘述〕必須附出處（含 p. 頁碼或『章』）
    for ln in lines:
        s = ln.strip()
        if s.startswith("- 〔原文〕") or s.startswith("- 〔摘述〕"):
            if not re.search(r"p\.?\d|頁|第.{1,3}章", s):
                errors.append(f"{name}: 引用缺出處 -> {s[:36]}")

    # 操作層每條 [O..] 必須有錨點
    in_op = False
    for ln in lines:
        st = ln.strip()
        if st.startswith("## 操作層"):
            in_op = True
            continue
        if st.startswith("## ") and in_op:
            in_op = False
        if in_op and re.match(r"-\s*\[O\d", st) and "⟵錨" not in st:
            errors.append(f"{name}: 操作層缺錨點 -> {st[:36]}")

def main():
    docs = sorted(p for p in REF.glob("*.md"))
    if not docs:
        print("FAIL：references/ 下沒有 .md 檔")
        sys.exit(1)
    for p in docs:
        check(p)
    if errors:
        print("FAIL 可回溯稽核：")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"PASS 可回溯稽核：{len(docs)} 份 reference 檔全部通過")

if __name__ == "__main__":
    main()
```

- [ ] **Step 4: 寫索引生成腳本 `tools/gen_index.py`**

```python
#!/usr/bin/env python3
"""掃描每份 reference 檔的標題與『> 來源：』標頭，生成 章節索引.md。"""
import re
import pathlib

CORE = pathlib.Path(__file__).resolve().parent.parent / "skills" / "seetoo-strategy-core"
REF = CORE / "references"
OUT = CORE / "章節索引.md"

rows = []
for p in sorted(REF.glob("*.md")):
    text = p.read_text(encoding="utf-8")
    title = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), p.stem)
    m = re.search(r"^> 來源：(.+)$", text, re.M)
    src = m.group(1).strip() if m else "（缺來源標頭）"
    rows.append(f"| `{p.name}` | {title} | {src} |")

OUT.write_text(
    "# 章節索引\n\n"
    "由 `tools/gen_index.py` 自動生成，請勿手改。\n\n"
    "| 檔案 | 主題 | 來源 |\n|---|---|---|\n" + "\n".join(rows) + "\n",
    encoding="utf-8",
)
print(f"已生成 {OUT}（{len(rows)} 列）")
```

- [ ] **Step 5: 跑稽核確認「空集合」行為**

Run: `python3 tools/audit_core.py`
Expected: `FAIL：references/ 下沒有 .md 檔`（因為只有 .gitkeep，符合預期 — 稽核器正常運作）

- [ ] **Step 6: Commit**

```bash
git add skills/seetoo-strategy-core/版本.md tools/audit_core.py tools/gen_index.py skills/seetoo-strategy-core/references/.gitkeep
git commit -m "feat(core): scaffold 骨架與可回溯稽核工具"
```

---

### Task 2: SKILL.md（核心地圖＋檢索紀律）

**Files:**
- Create: `skills/seetoo-strategy-core/SKILL.md`

- [ ] **Step 1: 寫 `SKILL.md`**

````markdown
---
name: seetoo-strategy-core
description: 司徒達賢《策略管理講義》的蒸餾知識核心（雙層：原文依據×操作層）。當需要忠實、扣回原文地運用司徒達賢的策略形態分析法、六大構面（產市垂規地競）、環條目、策略構想、前提驗證、策略矩陣/產業矩陣，或查詢他對某策略議題的主張時使用；亦為 seetoo-strategy-analysis、seeto-case-grilling、seetoo-strategy-tutor 三支技能的共用底座。鎖術語、每個操作主張錨回原文、守第十一章反主張邊界（不從 SWOT/mission/環境/目標 起手）。
---

# seetoo-strategy-core

司徒達賢《策略管理講義》的蒸餾知識核心。兩個角色：①三支技能的共用底座；
②可被直接叫用做「忠實查詢」（附原文＋章節出處）。

## 檢索紀律（每次引用本核心都遵守）

1. **三標籤**：〔原文〕逐字引述、〔摘述〕忠實轉述、〔延伸·非講義〕外部補充。
   前兩者必附章節＋頁碼；第三者極少用且須明標非講義、不得與原文衝突。
2. **原文錨定**：任何操作主張都對應某條原文依據；錨不回 ⇒ 標〔待查〕或不寫。
3. **術語鎖**：輸出鎖死講義術語（見 `references/00-術語表.md`），不得替換為一般 MBA 詞。
4. **反主張攔截**：若分析想從 SWOT / mission / vision / 環境分析 / 設定目標 起手，
   撞 `references/09-反主張與方法比較.md` 的邊界並改回策略形態分析法路徑。
5. **不杜撰**：查不到的，標「講義未涵蓋」或〔待查〕，絕不編造看似真實的內容。

## 何時讀哪份（reference 地圖）

| 需求 | 讀 |
|---|---|
| 術語、禁用替換詞 | `references/00-術語表.md` |
| 整體觀念架構、六大構面、環條目、功能政策/組織總覽 | `references/01-觀念架構與六大構面.md` |
| 策略構想、前提與前提驗證 | `references/02-策略構想與前提驗證.md` |
| 產生/評估/選擇策略方案、排列組合、可行性 | `references/03-策略方案-構思評估選擇.md` |
| 功能政策（行銷/生產/財務/研發/人資/資訊）與組織 | `references/04-功能政策與組織.md` |
| 完整分析「怎麼做」的十步驟程序（主程序） | `references/05-十步驟程序.md` |
| 策略矩陣、產業矩陣、策略點、策略要素 | `references/06-策略矩陣與產業矩陣.md` |
| 道理：經濟學/產業經濟（價值鏈、規模範疇、賽局競合…） | `references/07-道理庫-經濟與產業經濟.md` |
| 道理：組織/決策理論（配適、能力資源、前提驗證、去私…） | `references/08-道理庫-組織與決策理論.md` |
| 為何「不」這樣做（反主張）、與五力/BSC等比較 | `references/09-反主張與方法比較.md` |
| 案例：鬍鬚張、A 貿易商、B 公司 | `references/10-案例庫.md` |

## 給三支技能的消費提示（後續技能各自細化）

- **分析引擎**：`05` 主程序 + `01/02/03/04/06` 框架 + `07/08` 道理透鏡。
- **拷問教練**：`02`（前提驗證）、`09`（反主張）、`01`（六大構面）為追問彈藥。
- **學習助教**：全部；例題/習題另由該技能處理（不在本核心）。

## 自檢（輸出前）

- [ ] 每個主張都有原文錨點或已標〔待查〕？
- [ ] 用詞是否踩術語鎖？
- [ ] 是否誤用了第十一章列為「反主張」的起手式？
````

- [ ] **Step 2: 確認 frontmatter 格式正確**

Run: `head -3 skills/seetoo-strategy-core/SKILL.md`
Expected: 第一行為 `---`，第二行為 `name: seetoo-strategy-core`

- [ ] **Step 3: Commit**

```bash
git add skills/seetoo-strategy-core/SKILL.md
git commit -m "feat(core): SKILL.md 地圖與檢索紀律"
```

---

### Task 3: `00-術語表.md`（術語鎖）

**Files:**
- Create: `skills/seetoo-strategy-core/references/00-術語表.md`

來源參數：`01重點摘要.pdf`（p.1–2）、`2＿第二章策略形態與競爭優勢.pdf`（六大構面）、
`3＿第三章策略構想.pdf`（策略構想）、`9＿第九章策略矩陣分析法.pdf`（策略點/要素）。

- [ ] **Step 1: 讀來源** — Read 上列 PDF 對應頁。
- [ ] **Step 2: 編 canonical 術語表**。每個術語一列：**術語｜定義（附出處）｜禁用替換詞**。
      至少涵蓋：策略形態、六大構面＝產市垂規地競（六個全名）、環條目（環境/條件/目標組合）、
      策略構想、前提/前提假設、功能政策、組織方式、策略矩陣、產業矩陣、策略點、策略要素、
      價值鏈/價值單元、道理、競爭優勢。**定義一律附章節頁碼；查不到標〔待查〕。**
- [ ] **Step 3: 格式遵循雙層模板**（術語表的「操作層」＝「使用規則」，例如
      `[O1] 輸出時『策略形態』不得寫成 positioning/定位 ⟵錨:原文N`）。加 `> 來源：` 標頭。
- [ ] **Step 4: 稽核** — `python3 tools/audit_core.py` 該檔 PASS。
- [ ] **Step 5: 人工抽查** 2 條定義回 PDF 對照。
- [ ] **Step 6: Commit** — `git commit -m "feat(core): 00-術語表（術語鎖）"`

---

### Task 4–13: 各章 reference 檔（套用《蒸餾 SOP》）

> 每個 Task 結構相同：依下表參數套用上方《蒸餾 SOP》S1–S7。每完成一份檔即
> `git commit -m "feat(core): <檔名>"`。**Task 3 與 Task 4–13 彼此獨立，可平行執行**
>（各只新增自己的檔，不互改；索引在 Task 14 統一生成，無寫入衝突）。

| Task | 目標檔 | 來源檔（`sources/`） | 須涵蓋的節（依目錄，逐字對照原文填寫） |
|---|---|---|---|
| 4 | `01-觀念架構與六大構面.md` | `01重點摘要.pdf` p.1–2、`1＿序言及第一章…pdf` p.1–13、`2＿第二章…pdf` p.1–17 | 第1章 一~六（策略重要性、決策範圍、形態分析法主張、思維程序、與企業家思維呼應、相關學理）；第2章 一~三（基礎觀念、六大策略形態構面、鬍鬚張） |
| 5 | `02-策略構想與前提驗證.md` | `3＿第三章策略構想.pdf` p.1–11 | 第3章 一~五（策略構想意義、A公司簡例、鬍鬚張創業期、策略彈性、小結）；前提＝待驗證假設 |
| 6 | `03-策略方案-構思評估選擇.md` | `4＿第四章…pdf` p.1–17 | 第4章 一~九（產生方案、六大構面排列組合、可行性檢驗、與環條目/功能政策配合、1979鬍鬚張簡例、B公司簡例、功能政策配合、策略會議組織過程、小結） |
| 7 | `04-功能政策與組織.md` | `5＿第五章…pdf` p.1–14、`01重點摘要.pdf` p.3（表二） | 第5章 一~二（功能政策：行銷/生產/財務/研發/人資/資訊；組織配合策略變化）＋工作底稿細項 |
| 8 | `05-十步驟程序.md` | `6＿第六章…pdf` p.1–5 | 第6章 一~十（描述現狀→分析現策略構想→從環條目檢討→構思選項→找出並驗證前提→決定未來形態→調整功能政策與組織→擬行動計畫→策略控制→因應行動） |
| 9 | `06-策略矩陣與產業矩陣.md` | `9＿第九章…pdf` p.1–5、`AA第九章附錄策略要素.pdf` p.1–2、`10＿第十章…pdf` p.1–5、`01重點摘要.pdf` p.3–4 | 第9章 一~四（矩陣內容、價值鏈變化、策略要素、作用與價值）；第10章 一~六（策略點＝產業環境前提、產業矩陣構面、與策略矩陣關係、產業趨勢、隨策略矩陣變化、作戰地圖） |
| 10 | `07-道理庫-經濟與產業經濟.md` | `7＿第七章…pdf` p.1–17 | 第7章 一~六（價值鏈、供給與需求、交易合作與內部化、規模與範疇經濟、賽局/競合、共創價值的產業網絡） |
| 11 | `08-道理庫-組織與決策理論.md` | `8＿第八章…pdf` p.1–17 | 第8章 一~十（配適fit與平衡、能力與資源、前提驗證、網絡、決策者≠組織、去私、見機而做、組織設計配合策略、若干名詞、道與術） |
| 12 | `09-反主張與方法比較.md` | `11＿第十一章…pdf` p.1–9 | 第11章 一~十；以「司徒達賢主張**不要**X，因為Y」格式萃取（不從分類/mission/環境/SWOT/目標起手、策略行動≠策略、價值鏈分析、五力、平衡計分卡、根本策略） |
| 13 | `10-案例庫.md` | 鬍鬚張：`2＿`第三節、`3＿`第三節、`4＿`第五節；A貿易商：`3＿`第二節；B公司：`4＿`第六節 | 各案例：背景、當時策略構想/六大構面、關鍵前提、後續演變；標清各自出處 |

> 注：`AA第九章附錄策略矩陣例題及習題簡報.ppsx`、`AA第十章附錄產業矩陣EX版.xls`、
> `AA第六章附錄…分析架構.pps` 為簡報/試算格式，主要服務日後「學習助教/分析引擎」技能，
> **不納入本核心**；若 Task 9 需要其圖例，僅以 PDF 既有內容為準，不強行解析 ppt/xls。

---

### Task 14: 整合驗證（稽核＋黃金查詢＋反杜撰＋生成索引）

**Files:**
- Generate: `skills/seetoo-strategy-core/章節索引.md`

- [ ] **Step 1: 全量可回溯稽核**

Run: `python3 tools/audit_core.py`
Expected: `PASS 可回溯稽核：11 份 reference 檔全部通過`

- [ ] **Step 2: 生成索引**

Run: `python3 tools/gen_index.py`
Expected: `已生成 …/章節索引.md（11 列）`

- [ ] **Step 3: 黃金查詢驗收（人工，逐題確認）**

對核心提下列問題，逐題核對：
1. 「司徒達賢的六大策略形態構面是哪六個？」→ 須答「產市垂規地競」六個全名，附 `01` 出處。
2. 「策略構想是什麼？」→ 須含「前提假設」用語，附 `02`／重點摘要出處。
3. 「為什麼策略不該從 SWOT 開始？」→ 須引 `09` 給出他的理由。
4. 「策略矩陣裡的『策略點』是什麼？」→ 須含價值鏈×六大構面、附 `06` 出處。

- [ ] **Step 4: 反杜撰驗收（人工）**

問「司徒達賢怎麼看 OKR？」→ 核心**必須**回「講義未涵蓋／僅能標〔延伸·非講義〕」，
不得編造。任一題若編造 ⇒ 回對應 Task 修正。

- [ ] **Step 5: 術語鎖驗收（人工）**

抽查任一輸出，確認未把「策略形態」說成「定位/positioning」等被禁替換詞。

- [ ] **Step 6: Commit**

```bash
git add skills/seetoo-strategy-core/章節索引.md
git commit -m "feat(core): 生成章節索引並通過整合驗證"
```

---

### Task 15: 部署、CHANGELOG、推送

- [ ] **Step 1: symlink 到全域 skills**

```bash
ln -s "/Users/shihchieh/Seetoo_Dah_Hsian-skills/skills/seetoo-strategy-core" "$HOME/.claude/skills/seetoo-strategy-core"
```

- [ ] **Step 2: 驗證連結與可讀**

Run: `ls -l "$HOME/.claude/skills/seetoo-strategy-core" && head -2 "$HOME/.claude/skills/seetoo-strategy-core/SKILL.md"`
Expected: 連結指向專案路徑；印出 `---` 與 `name: seetoo-strategy-core`
（註：新 skill 要被 Skill 工具列出，可能需重啟/重新掃描 `~/.claude/skills/`。）

- [ ] **Step 3: 更新 `CHANGELOG.md`** — 把 `seetoo-strategy-core 實作` 從 `Planned` 移到 `Added`，記下 v0.1。

- [ ] **Step 4: Commit ＋ 發 PR**

```bash
git add CHANGELOG.md
git commit -m "chore: 部署 seetoo-strategy-core 並更新 CHANGELOG"
git push -u origin feat/seetoo-strategy-core
gh pr create --fill --base main
```

---

## Self-Review（對照 spec 的覆蓋檢查）

| Spec 章節 / 要求 | 對應 Task |
|---|---|
| §1 定位（兩角色、三保證） | Task 2（SKILL.md 檢索紀律） |
| §2 來源講義（版本） | Task 1（版本.md） |
| §3 檔案結構＋內容地圖（11 份 reference） | Task 1–13 |
| §4 雙層模板（三標籤） | 《蒸餾 SOP》＋ audit_core.py 強制 |
| §5 紀律機制（錨定/術語鎖/反主張/可回溯） | Task 2 + audit_core.py + Task 14 |
| §6 消費契約（穩定檔名、地圖） | Task 2（reference 地圖＋消費提示） |
| §7 驗證（可回溯稽核/黃金查詢/反杜撰） | Task 1（腳本）＋ Task 14（驗收） |
| §8 建置流程（逐章、可平行） | Task 4–13（獨立、可平行）＋ Task 14 索引 |
| §3 安裝位置（專案＋symlink 全域） | Task 15 |
| §9 非目標（不做三支技能、不做 RAG、不納外部為事實） | 計畫範圍即只含核心；ppt/xls 明列不納入 |

**Placeholder 掃描**：各章 reference 檔的「內容」刻意不預寫（不杜撰鐵則）——改以「確切來源頁＋須涵蓋節（取自真實目錄）＋雙層模板＋audit 閘門」鎖死，屬設計上的正確處理，非 placeholder。腳本、SKILL.md、模板均為完整可執行內容。

**型別/命名一致性**：標籤〔原文〕/〔摘述〕/〔延伸·非講義〕、錨點 `⟵錨:原文N`、來源標頭 `> 來源：… p.`、檔名 `0X-…md` 在 SOP、audit_core.py、gen_index.py、各 Task 間一致。

---

## Execution Handoff

計畫完成。兩種執行方式：

1. **Subagent-Driven（推薦）** — 每個 Task 派新 subagent、任務間複審；Task 3–13 可平行（各自獨立檔），最適合這種逐章蒸餾。
2. **Inline Execution** — 在本 session 內分批執行、檢查點複審。

> 依你的指示：**現在先停，等你檢查這份計畫**。確認後再選執行方式；尚未動工。
