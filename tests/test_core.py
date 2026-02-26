from src.core import items_stats

def test_items_stats_empty():
    assert items_stats([]) == {"total": 0, "unique_titles": 0, "last_created_at": None}
