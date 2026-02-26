from __future__ import annotations
from datetime import datetime
from typing import Any

from src.core import add_item, items_stats, find_items_by_substring
from src.storage import load_state, save_state


STATE_PATH = "data/state.json"


def _now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def main() -> None:
    state = load_state(STATE_PATH)
    items: list[dict[str, Any]] = state["items"]

    print("AI Diploma CLI (минимальная версия)")
    print("Команды: add | list | search | stats | exit")

    while True:
        cmd = input("> ").strip().lower()

        if cmd == "add":
            title = input("title: ").strip()
            item = {"id": len(items) + 1, "title": title, "created_at": _now_iso(), "payload": {}}
            items = add_item(items, item)
            save_state(STATE_PATH, items, version=1)
            print("OK: added")


        elif cmd == "list":
            for it in items:
                print(f"{it.get('id')}: {it.get('title')} ({it.get('created_at')})")


        elif cmd == "search":
            q = input("query: ").strip()
            res = find_items_by_substring(items, q)
            for it in res:
                print(f"{it.get('id')}: {it.get('title')}")


        elif cmd == "stats":
            print(items_stats(items))


        elif cmd == "exit":
            print("bye")
            break


        else:
            print("Unknown command. Use: add | list | search | stats | exit")


if __name__ == "__main__":
    main()
