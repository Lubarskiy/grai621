from __future__ import annotations
from typing import Any


def project_passport(title: str, goal: str, user: str, risks: list[str]) -> dict[str, Any]:
    """Паспорт проекта (можно использовать в README/доках)."""
    return {"title": title, "goal": goal, "user": user, "risks": risks}


def validate_item(item: dict[str, Any]) -> list[str]:
    """
    Проверка сущности item.
    Минимальные поля: title(str, непустой), payload(dict), created_at(str с 'T' или ISO-like).
    Возвращает список ошибок (пустой = OK).
    """
    errors: list[str] = []

    title = item.get("title")
    if not isinstance(title, str) or title.strip() == "":
        errors.append("title: required non-empty string")

    payload = item.get("payload")
    if not isinstance(payload, dict):
        errors.append("payload: must be dict")

    created_at = item.get("created_at")
    if not isinstance(created_at, str) or "T" not in created_at:
        errors.append("created_at: must be ISO-like string containing 'T'")

    return errors


def add_item(items: list[dict[str, Any]], item: dict[str, Any]) -> list[dict[str, Any]]:
    """Добавить item (без мутации списка)."""
    return items + [item]


def remove_item_by_id(items: list[dict[str, Any]], item_id: int) -> list[dict[str, Any]]:
    """Удалить item по id (без мутации списка)."""
    return [it for it in items if it.get("id") != item_id]


def find_items_by_substring(items: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    """Поиск по подстроке в title (без учета регистра)."""
    q = str(query).lower()
    out: list[dict[str, Any]] = []
    for it in items:
        title = it.get("title", "")
        if isinstance(title, str) and q in title.lower():
            out.append(it)
    return out


def update_item(items: list[dict[str, Any]], item_id: int, patch: dict[str, Any]) -> list[dict[str, Any]]:
    """Обновить поля item по id (patch-словарь)."""
    out: list[dict[str, Any]] = []
    for it in items:
        if it.get("id") == item_id:
            updated = dict(it)
            updated.update(patch)
            out.append(updated)
        else:
            out.append(it)
    return out


def items_stats(items: list[dict[str, Any]]) -> dict[str, Any]:
    """Статистика по items: total, unique_titles, last_created_at."""
    total = len(items)
    titles = set()
    last_created_at = None

    for it in items:
        title = it.get("title", "")
        if isinstance(title, str):
            t = title.strip()
            if t:
                titles.add(t)

        ca = it.get("created_at")
        if isinstance(ca, str):
            if last_created_at is None or ca > last_created_at:
                last_created_at = ca

    return {"total": total, "unique_titles": len(titles), "last_created_at": last_created_at}
