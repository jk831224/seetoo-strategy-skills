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
