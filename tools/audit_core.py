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
