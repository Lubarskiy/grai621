from __future__ import annotations
from typing import Any
import json
import os


def save_json(path: str, obj: Any) -> None:
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def load_json(path: str, default: Any = None) -> Any:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default
    except json.JSONDecodeError:
        return default


def export_items_to_json(path: str, items: list[dict[str, Any]]) -> None:
    save_json(path, items)


def import_items_from_json(path: str) -> list[dict[str, Any]]:
    data = load_json(path, default=[])
    if not isinstance(data, list):
        return []
    return [it for it in data if isinstance(it, dict)]


def save_state(path: str, items: list[dict[str, Any]], version: int = 1) -> None:
    state = {"version": version, "items": items}
    save_json(path, state)


def load_state(path: str) -> dict[str, Any]:
    state = load_json(path, default={"version": 1, "items": []})
    if not isinstance(state, dict):
        return {"version": 1, "items": []}

    version = state.get("version", 1)
    items = state.get("items", [])
    if not isinstance(items, list):
        items = []
    items = [it for it in items if isinstance(it, dict)]
    return {"version": version, "items": items}
