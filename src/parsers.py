from __future__ import annotations
from typing import Any
import re


def normalize_spaces(s: str) -> str:
    """Убрать лишние пробелы."""
    return " ".join(str(s).split())


def slugify(s: str) -> str:
    """Превратить строку в slug: lower + пробелы в '_' ."""
    return normalize_spaces(s).lower().replace(" ", "_")


def parse_kv_pairs(s: str) -> dict[str, str]:
    """Парсер формата: key1=val1;key2=val2"""
    out: dict[str, str] = {}
    text = str(s).strip()
    if not text:
        return out
    for part in text.split(";"):
        part = part.strip()
        if not part or "=" not in part:
            continue
        k, v = part.split("=", 1)
        k, v = k.strip(), v.strip()
        if k:
            out[k] = v
    return out


def find_ints_in_text(s: str) -> list[int]:
    """Найти все целые числа в тексте."""
    return [int(m) for m in re.findall(r"-?\d+", str(s))]


def to_int_safe(s: Any, default: int) -> int:
    try:
        return int(str(s).strip())
    except Exception:
        return default


def to_float_safe(s: Any, default: float) -> float:
    try:
        return float(str(s).strip())
    except Exception:
        return default


def normalize_user_input(d: dict[str, Any]) -> dict[str, Any]:
    """Нормализовать id/title/score."""
    raw_id = d.get("id")
    raw_title = d.get("title", "")
    raw_score = d.get("score")

    title = "" if raw_title is None else str(raw_title).strip()

    id_val = None
    if raw_id is not None:
        try:
            id_val = int(str(raw_id).strip())
        except Exception:
            id_val = None

    score_val = None
    if raw_score is not None:
        try:
            score_val = float(str(raw_score).strip())
        except Exception:
            score_val = None

    return {"id": id_val, "title": title, "score": score_val}


def parse_item_soft(raw: dict[str, Any]):
    """
    Мягкий парсинг item (возвращает нормализованный dict + список ошибок).
    Требования:
    - title обязателен и непустой
    - id (если есть) int >= 0
    - score (если есть) float в [0,1]
    """
    errors: list[str] = []
    norm = normalize_user_input(raw)

    if norm["title"] == "":
        errors.append("title: required")

    if raw.get("id") is not None:
        if norm["id"] is None:
            errors.append("id: must be int")
        elif norm["id"] < 0:
            errors.append("id: must be >= 0")

    if raw.get("score") is not None:
        if norm["score"] is None:
            errors.append("score: must be float")
        elif not (0.0 <= norm["score"] <= 1.0):
            errors.append("score: must be in [0,1]")

    return norm, errors


def parse_item_from_csv_line(line: str):
    """
    CSV строка: id,title,created_at
    Возвращает (item, errors)
    """
    errors: list[str] = []
    parts = [p.strip() for p in str(line).split(",")]
    if len(parts) != 3:
        return None, ["line: must have 3 comma-separated fields"]

    raw_id, title, created_at = parts

    try:
        item_id = int(raw_id)
        if item_id < 0:
            errors.append("id: must be >= 0")
    except ValueError:
        errors.append("id: must be int")
        item_id = None

    if title.strip() == "":
        errors.append("title: required")

    if "T" not in created_at:
        errors.append("created_at: must contain 'T'")

    if errors:
        return None, errors

    item = {"id": item_id, "title": title.strip(), "created_at": created_at, "payload": {}}
    return item, []
